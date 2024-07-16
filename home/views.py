from django.shortcuts import get_object_or_404, redirect, render
from tienda.forms import CustomUserCreationForm, CartAddProductForm, EstadoPedidoForm
from tienda.models import Cart, CartItem, Producto
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from tienda.models import Pedido, PedidoItem
from django.http import JsonResponse, HttpResponseRedirect

# Create your views here.

def product_list():
    return Producto.objects.all()

def home(request):
    
    return render(request, "index.html")


def finder(request, category=None):
    products = None

    if request.method == "GET":
        searchQuery = request.GET.get("search", "")
        
        products = Producto.objects.all()
        
        data = {
            "searchQ": searchQuery,
            "products": products,
            "category": category
        }

        return render(request, "finder.html", data)

def productView(request, id):
    product = get_object_or_404(Producto, id=id)
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
def pedidos(request):
    if request.user.is_staff:
        pedidos = Pedido.objects.all()
    else:
        pedidos = Pedido.objects.filter(user=request.user)
    
    return render(request, "pedidos.html",  {'pedidos': pedidos})

def detallepedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    detalle_pedido = PedidoItem.objects.filter(pedido_id = pedido_id)
    
    if request.user.is_staff:
        if request.method == 'POST':
            form = EstadoPedidoForm(request.POST, instance=pedido)
            if form.is_valid():
                form.save()
                return redirect('detallepedido', pedido_id=pedido.id)
        else:
            form = EstadoPedidoForm(instance=pedido)
    else:
        form = None

    return render(request, 'detallepedido.html', {'pedido': pedido, 'productos': detalle_pedido, 'form': form})

def cartDetail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart).select_related('producto')
    
    if not items.exists():
        messages.warning(request, 'No tienes ningún producto en tu carrito.')
        return redirect('finder')
    
    total = sum(item.producto.precio * item.quantity for item in items)
    
    if request.method == 'POST':
        with transaction.atomic():
            # Crear el objeto Pedido
            pedido = Pedido.objects.create(
                user=request.user,
                total=total,
                estado='pendiente'
            )
            
            # Iterar sobre los items del carrito y agregarlos al pedido
            for item in items:
                # Verificar si hay suficiente stock disponible
                if item.producto.stock >= item.quantity:
                    PedidoItem.objects.create(
                        pedido=pedido,
                        producto=item.producto,
                        cantidad=item.quantity
                    )
                    # Reducir la cantidad en el stock del producto
                    item.producto.stock -= item.quantity
                    item.producto.save()
                else:
                    messages.error(request, f'No hay suficiente stock disponible para {item.producto.nombre}.')
                    return redirect('cartDetail')
            
            # Vaciar el carrito después de completar el pedido
            cart.cartitem_set.all().delete()
            cart.delete()
            messages.success(request, 'Pedido realizado, espere actualizaciones de estado.')
        return redirect('pedidos')
    return render(request, 'cart/detail.html', {'cart': cart, 'items': items, 'total': total})

@login_required
def cartAdd(request, product_id):
    product = get_object_or_404(Producto, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        item, created = CartItem.objects.get_or_create(cart=cart, producto=product)
        item.quantity += cd['quantity']
        item.save()

    # Capturar la URL anterior del usuario
    previous_url = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(previous_url)

@login_required
def cartRemove(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cartDetail')

@login_required
def cartUpdate(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'incrementar':
            if item.quantity < item.producto.stock:
                item.quantity += 1
                item.save()
            else:
                messages.error(request, 'No hay suficiente stock disponible')
        elif action == 'decrementar':
            if item.quantity > 1:
                item.quantity -= 1
                item.save()
            else:
                # Si la cantidad es 1 y se intenta decrementar, eliminar el producto del carrito
                item.delete()

    previous_url = request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(previous_url)
