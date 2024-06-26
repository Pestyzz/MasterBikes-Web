from django import forms
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

""" class BicicletaForm(forms.ModelForm):
    class Meta:
        model = Bicicleta
        fields = ['nombre','descripcion','tamanioaro','suspension','marco']
        """
        
User = get_user_model()

class BicicletaForm(forms.ModelForm):
    class Meta:
        model = Bicicleta
        fields = '__all__'

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class AccesorioForm(forms.ModelForm):
    class Meta:
        model = Accesorio
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class BoletaForm(forms.ModelForm):
    class Meta:
        model = Boleta
        fields = '__all__'

class DetalleBoletaForm(forms.ModelForm):
    class Meta:
        model = DetalleBoleta
        fields = '__all__'

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    rut = forms.CharField(max_length=12, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('email', 'rut', 'first_name', 'last_name', 'password1', 'password2')


class CartAddProductForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']