from django.shortcuts import get_object_or_404, render
from tienda.models import Producto

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
        elif category == "Arriendos":
            products = Producto.objects.filter(servicio__nombre="Arriendo")
        elif category == "Reparaciones":
            products = Producto.objects.filter(servicio__nombre="Reparación")
        elif category == None:
            products = Producto.objects.filter(nombre__icontains=searchQuery)
        
        data = {
            "searchQ": searchQuery,
            "products": products,
            "category": category
        }

        return render(request, "finder.html", data)
    
def productView(request):
    return render(request, "product.html")