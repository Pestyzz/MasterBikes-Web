from django.shortcuts import render
from .models import *

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