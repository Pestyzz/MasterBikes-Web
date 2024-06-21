from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *

#Funciones
def lista_bicicleta():
    return Bicicleta.objects.all()

def lista_servicio():
    return Servicio.objects.all()

def lista_accesorio():
    return Accesorio.objects.all()

def lista_boleta():
    return Boleta.objects.all()

def lista_delivery():
    return Delivery.objects.all()

def lista_pago():
    return Pago.objects.all()


# Create your views here.
def prueba(request):
    bicicletas = lista_bicicleta()
    servicios = lista_servicio()
    accesorios = lista_accesorio()
    boletas = lista_boleta()
    deliverys = lista_delivery()
    pagos = lista_pago()

    datos = {
        'bicicletas': bicicletas,
        'servicios': servicios,
        'accesorios': accesorios,
        'boletas': boletas,
        'deliverys': deliverys,
        'pagos': pagos,
    }

    return render(request, 'tienda/prueba.html', datos)

def crearproducto(request):
    if request.method == 'POST':
        form = BicicletaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prueba')
    else:
        form = BicicletaForm()
    
    return render(request, "tienda/crear_producto.html", {'form': form})

def modificarbici(request, pk):
    producto = get_object_or_404(Bicicleta, pk=pk)
    if request.method == 'POST':
        form = BicicletaForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('prueba')
    else:
        form = BicicletaForm(instance=producto)
    
    return render(request, 'tienda/modificarbici.html', {'form': form})

def eliminarbici(request, pk):
    producto = get_object_or_404(Bicicleta, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('prueba')
    return render(request, 'tienda/eliminarbici.html', {'producto': producto})