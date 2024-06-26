from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.finder, name='finder'),
    path('catalog/<str:category>/', views.finder, name='finderCategory'),
    path('product/', views.productView, name='product'),
]
