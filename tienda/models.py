from django.db import models
import uuid
import datetime
from django.contrib.auth.models import AbstractBaseUser, User, UserManager, PermissionsMixin
from PIL import Image
from django.contrib.auth import get_user_model

# Create your models here.


class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    rut = models.CharField(max_length=12, unique=True, primary_key=True, verbose_name='RUT')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


# Modelos de productos tienda
class Bicicleta(models.Model):

    SUSPENSION = {
        "DELANTERA": "DELANTERA",
        "TRASERA": "TRASERA",
        "DOBLE": "DOBLE",
    }

    MARCO = {
        "ACERO": "ACERO",
        "ALUMINIO": "ALUMINIO",
        "CARBON": "CARBON",
    }

    TIPO = {
        "MONTAÑA": "MONTAÑA",
        "RUTA": "RUTA",
        "BMX": "BMX",
        "HIBRIDA": "HIBRIDA",
        "CICLOCROSS": "CICLOCROSS",
        "GRAVEL": "GRAVEL",
        "ENDURO": "ENDURO",
        "DOWNHILL": "DOWNHILL",}

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    tamanioaro = models.IntegerField(default=26)
    suspension = models.CharField(default='DELANTERA', max_length=9, choices=SUSPENSION)
    marco = models.CharField(default='ACERO', max_length=8, choices=MARCO)
    tipobicicleta = models.CharField(default='MONTAÑA',max_length=100,choices=TIPO)


    def __str__(self):
        return self.nombre


class Servicio(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Accesorio(models.Model):


    TIPO = {
        "BICICLETA": "BICICLETA",
        "CASCOS": "CASCOS",
        "ROPA": "ROPA",
        "ZAPATILLAS": "ZAPATILLAS",
        "LUCES": "LUCES",
        "CANDADOS": "CANDADOS",
        "PORTA BICICLETAS": "PORTA BICICLETAS",
        "OTROS": "OTROS",}

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    tipoaccesorio = models.CharField(default='BICICLETA',max_length=100,choices=TIPO)
    

    def __str__(self):
        return self.nombre


class Marca(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    bicicleta = models.ForeignKey(Bicicleta, on_delete=models.SET_NULL, null=True, blank=True)
    servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True, blank=True)
    accesorio = models.ForeignKey(Accesorio, on_delete=models.SET_NULL, null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True, blank=True)
    stock = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='static/media/productos/', null=False, blank=True)

    def __str__(self):
        return self.nombre

    @property
    def getImage(self):
        try:
            return self.imagen.url
        except:
            return ""


class Boleta(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=False)
    id_transaccion = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id) + '-' + self.cliente.email


class DetalleBoleta(models.Model):

    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return str(self.boleta.id) + '-' + self.producto.name


class Delivery(models.Model):

    ESTADO = {
        "P": "PENDIENTE",
        "E": "ENVIADO",
        "R": "RECIBIDO",
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    boleta = models.OneToOneField(Boleta, on_delete=models.CASCADE, null=True, blank=True)
    comentarios = models.TextField(max_length=100, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    ciudad = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    codigo_postal = models.CharField(max_length=10, null=True, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADO, default='P')

    def __str__(self):
        return str(self.id) + '-' + self.boleta.cliente.email


class Pago(models.Model):

    ESTADO = {
        "P": "PENDIENTE",
        "A": "ACEPTADO",
        "R": "RECHAZADO",
    }

    TIPO = {
        "T": "TRANSFERENCIA",
        "C": "CREDITO",
        "D": "DEBITO",
    }

    estado = models.BooleanField(default=False)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    tipo_pago = models.CharField(max_length=1, choices=TIPO)
    boleta = models.OneToOneField(Boleta, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADO, default='P')
    codigo_autorizacion = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.boleta.id)
    


User = get_user_model()

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Cart {self.id} for {self.user.email}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.producto.nombre}'