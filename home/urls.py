from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from tienda.forms import CustomAuthenticationForm

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogue/', views.finder, name='finder'),
    path('catalogue/<str:category>/', views.finder, name='finderCategory'),
    path('product/<int:id>/', views.productView, name='product'),
    path('accounts/login/', auth_views.LoginView.as_view(authentication_form=CustomAuthenticationForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', views.register, name="register"),
    path('cart/', views.cartDetail, name='cartDetail'),
    path('cart/add/<int:product_id>/', views.cartAdd, name='cartAdd'),
    path('cart/remove/<int:item_id>/', views.cartRemove, name='cartRemove'),
]
