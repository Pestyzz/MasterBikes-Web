from django.db import models
import uuid, datetime
from django.contrib.auth.models import AbstractBaseUser, User, UserManager, PermissionsMixin
from PIL import Image

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

    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tamanioaro = models.IntegerField(default=26)
    suspension = models.CharField(default='DELANTERA',max_length=9, choices=SUSPENSION)
    marco = models.CharField(default='ACERO',max_length=8, choices=MARCO)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='static/media/productos/', null=True, blank=True)


    def __str__(self):
        return self.nombre
    
    @property
    def getImage(self):
        try:
            return self.imagen.url
        except:
            return ""