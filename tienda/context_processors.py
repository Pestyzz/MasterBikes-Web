from .models import Cart, CartItem

def cart_context(request):
    

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart).select_related('producto')
        cart_item_count = sum(item.quantity for item in cart_items)
        items = cart_items
        total = sum(item.producto.precio * item.quantity for item in items)
    else:
        cart = None
        cart_item_count = 0
        items = []
        total = 0

    return {
        'cart_item_count': cart_item_count,
        'cart': cart,
        'items': items,
        'total': total,
    }
    