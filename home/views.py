from django.shortcuts import get_object_or_404, redirect, render
from tienda.forms import CustomUserCreationForm
from tienda.models import Cart, CartItem, Producto
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from tienda.models import Producto, Cart, CartItem
from tienda.forms import CartAddProductForm
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.urls import reverse

import json

# Create your views here.

def product_list():
    return Producto.objects.all

def home(request):
    products = product_list()
    
    return render(request, "index.html", {"products": products})

def finder(request, category=None):
    products = None
    
    if request.method == "GET":
        searchQuery = request.GET.get("search", "")
        
        if category == "Bicicletas":
            products = Producto.objects.filter(bicicleta__isnull=False, nombre__icontains=searchQuery)
        elif category == "Accesorios":
            products = Producto.objects.filter(accesorio__isnull=False, nombre__icontains=searchQuery)
        elif category == "Servicios":
            products = Producto.objects.filter(servicio__isnull=False, nombre__icontains=searchQuery)
        else:
            products = Producto.objects.filter(nombre__icontains=searchQuery) or Producto.objects.filter(marca__nombre__icontains=searchQuery)
        
        data = {
            "searchQ": searchQuery,
            "products": products,
            "category": category
        }

        return render(request, "finder.html", data)
    
def productView(request, id):
    product = get_object_or_404(Producto,id=id)
    return render(request, "product.html", {"product": product})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart/detail.html', {'cart': cart, 'items': items})

# @login_required
# def cart_add(request, product_id):
#     product = get_object_or_404(Producto, id=product_id)
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         item, created = CartItem.objects.get_or_create(cart=cart, producto=product)
#         item.quantity += cd['quantity']
#         item.save()
#     return redirect('cart_detail')

# @login_required
# def cart_remove(request, item_id):
#     item = get_object_or_404(CartItem, id=item_id)
#     item.delete()
#     return redirect('cart_detail')

@login_required
def cart_remove_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item_id = data.get('item_id')
            item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
            item.delete()

            cart = Cart.objects.get(user=request.user)
            items = CartItem.objects.filter(cart=cart)
            cart_items = [{'id': i.id, 'product_name': i.producto.nombre, 'quantity': i.quantity} for i in items]

            return JsonResponse({'success': True, 'cart_items_count': items.count(), 'cart_items': cart_items})
        except CartItem.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Item not found'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request'})


@login_required
def cart_add(request, product_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            quantity = data.get('quantity', 1)
            product = get_object_or_404(Producto, id=product_id)
            cart, created = Cart.objects.get_or_create(user=request.user)
            item, created = CartItem.objects.get_or_create(cart=cart, producto=product)
            if created:
                item.quantity = quantity
            else:
                item.quantity += quantity
            item.save()

            items = CartItem.objects.filter(cart=cart)
            cart_items = [{'id': i.id, 'product_name': i.producto.nombre, 'quantity': i.quantity} for i in items]

            return JsonResponse({'success': True, 'cart_items_count': items.count(), 'cart_items': cart_items})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

