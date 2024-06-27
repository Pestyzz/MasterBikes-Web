from django import forms
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True, label='Email')
    rut = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=12, required=True, label='RUT')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=True, label='Primer Nombre')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=30, required=True, label='Apellido')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, label='Confirmar Contraseña')

    class Meta:
        model = User
        fields = ('email', 'rut', 'first_name', 'last_name', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Contraseña')

class CartAddProductForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']