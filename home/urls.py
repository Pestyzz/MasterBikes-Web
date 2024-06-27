from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from tienda.forms import CustomAuthenticationForm

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogue/', views.finder, name='finder'),
    path('catalogue/<str:category>/', views.finder, name='finderCategory'),
    path('product/<uuid:id>/', views.productView, name='product'),
    path('login/', auth_views.LoginView.as_view(authentication_form=CustomAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name="register"),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<uuid:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
]
