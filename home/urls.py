from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogue/', views.finder, name='finder'),
    path('catalogue/<str:category>/', views.finder, name='finderCategory'),
    path('product/<uuid:id>/', views.productView, name='product'),
]
