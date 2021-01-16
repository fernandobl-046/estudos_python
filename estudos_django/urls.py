from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/calcular', views.calcular, name='calcular'),
    path('accounts/login/', views.logar, name='logar'),
    path('produtos/', views.produtos, name='produtos'),
    path('empresa/', views.empresa, name='empresa'),
    path('contato/', views.contato, name='contato'),
    path('admin/', admin.site.urls, name='admin'),
]
