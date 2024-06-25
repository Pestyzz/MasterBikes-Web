from django.shortcuts import get_object_or_404, render
from tienda.models import Producto

# Create your views here.

def product_list():
    return Producto.objects.all

def home(request):
    products = product_list()
    print(products)
    
    return render(request, "index.html", {"products": products})

def finder(request):
    if request.method == "GET":
        searchQuery = request.GET.get("search")
        
        data = {
            "search": searchQuery
        }
        print(request.GET)
        return render(request, "finder.html", data)