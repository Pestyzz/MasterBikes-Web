from django.shortcuts import get_object_or_404, redirect, render
from tienda.forms import CustomUserCreationForm, PagoForm, DeliveryForm
from tienda.models import Cart, CartItem, Producto, Pago, Boleta, DetalleBoleta
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from tienda.models import Producto, Cart, CartItem
from django.http import JsonResponse
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
def cartAdd(request, product_id):
    product = get_object_or_404(Producto, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
    else:
        quantity = 1
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if created:
        cart_item.quantity = quantity
    else:
         cart_item.quantity += quantity
         
    cart_item.save()
    return redirect('home')

@login_required
def cartRemove(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('home')

@login_required
def cartDetail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'index.html', {'cart_items': cart_items})

@login_required
def payment(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    cart_items = CartItem.objects.filter(cart=cart)

    if request.method == 'POST':
        pago_form = PagoForm(request.POST)
        delivery_form = DeliveryForm(request.POST)
        if pago_form.is_valid() and (delivery_form.is_valid() or pago_form.cleaned_data['tipo_entrega'] == 'R'):
            # Crear Boleta
            boleta = Boleta.objects.create(cliente=user)
            
            # Crear DetalleBoleta
            for item in cart_items:
                DetalleBoleta.objects.create(
                    boleta=boleta,
                    producto=item.product,
                    cantidad=item.quantity
                )
            
            # Crear Pago
            pago = pago_form.save(commit=False)
            pago.boleta = boleta
            pago.estado = 'P'
            # Aquí manejarías la lógica de procesar el pago con la tarjeta
            pago.save()

            if pago_form.cleaned_data['tipo_entrega'] == 'D':
                # Crear Delivery
                delivery = delivery_form.save(commit=False)
                delivery.boleta = boleta
                delivery.save()
            
            # Limpiar el carrito
            cart_items.delete()

            return redirect('home')  # Redirigir a una página de éxito

    else:
        pago_form = PagoForm()
        delivery_form = DeliveryForm()

    context = {
        'cart_items': cart_items,
        'pago_form': pago_form,
        'delivery_form': delivery_form,
    }
    return render(request, 'payment.html', context)