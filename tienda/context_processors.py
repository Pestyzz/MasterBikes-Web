from tienda.models import Cart, CartItem

def cart_context(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        items = CartItem.objects.filter(cart=cart)
        cart_item_count = items.count()
    else:
        items = []
        cart_item_count = 0

    return {
        'cart_items': items,
        'cart_item_count': cart_item_count,
    }
