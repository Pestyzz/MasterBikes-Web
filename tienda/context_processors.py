# tienda/context_processors.py
from .models import Cart, CartItem

def cart_items(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        items = CartItem.objects.filter(cart=cart)
    else:
        items = []
        print(items)
    return {'cart_items': items}
