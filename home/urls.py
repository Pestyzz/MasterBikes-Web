from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.finder, name='finder'),
    path('catalog/<str:category>/', views.finder, name='finderCategory'),
    path('product/', views.productView, name='product'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name="register"),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<uuid:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
]
