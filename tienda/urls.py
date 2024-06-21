from django.urls import path
from .views import *


urlpatterns = [
    path('',prueba, name='prueba'),
    path('crearproducto/', crearproducto, name="crearproducto"),
    path('modificarbici/<uuid:pk>', modificarbici, name="modificarbici"),
    path('eliminarbici/<uuid:pk>', eliminarbici, name="eliminarbici")
]