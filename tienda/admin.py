from django.contrib import admin

# Register your models here.
from .models import User, Bicicleta, Servicio, Accesorio,Marca, Producto, Boleta, DetalleBoleta, Delivery, Pago, Cart,CartItem,Pedido,PedidoItem


class UserAdmin(admin.ModelAdmin):
    list_display = '__all__'


class BicicletaAdmin(admin.ModelAdmin):
    list_display = '__all__'


class ServicioAdmin(admin.ModelAdmin):
    list_display = '__all__'


class AccesorioAdmin(admin.ModelAdmin):
    list_display = '__all__'


class MarcaAdmin(admin.ModelAdmin):
    list_display = '__all__'


class ProductoAdmin(admin.ModelAdmin):
    list_display = '__all__'


class BoletaAdmin(admin.ModelAdmin):
    list_display = '__all__'


class DetalleBoletaAdmin(admin.ModelAdmin):
    list_display = '__all__'


class DeliveryAdmin(admin.ModelAdmin):
    list_display = '__all__'


class PagoAdmin(admin.ModelAdmin):
    list_display = '__all__'


class CartAdmin(admin.ModelAdmin):
    list_display = '__all__'


class CartItemAdmin(admin.ModelAdmin):
    list_display = '__all__'


class PedidoAdmin(admin.ModelAdmin):
    list_display = '__all__'


class PedidoItemAdmin(admin.ModelAdmin):
    list_display = '__all__'

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
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Pedido)
admin.site.register(PedidoItem)



