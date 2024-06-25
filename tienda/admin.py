from django.contrib import admin

# Register your models here.
from .models import User, Bicicleta, Servicio, Accesorio,Marca, Producto, Boleta, DetalleBoleta, Delivery, Pago
admin.site.register(User)
admin.site.register(Bicicleta)
admin.site.register(Servicio)
admin.site.register(Accesorio)
admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Boleta)
admin.site.register(DetalleBoleta)
admin.site.register(Delivery)
admin.site.register(Pago)

