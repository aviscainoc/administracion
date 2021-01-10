"""administracion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('registrase/', views.registrarse, name="registrarse"),
    path('recuperarContrasenia/', views.recuperarContrasenia, name="recuperarContrasenia"),
    path('empresas/', views.empresas, name="empresas"),
    path('crearEmpresa/',views.crearEmpresa, name="crearEmpresa"),
    path('empresas/editarEmpresa/<int:id>',views.editarEmpresa, name="editarEmpresa"),
    path('productoServicios/', views.productoServicios, name="productoServicios"),
    path('CrearProductos/',views.CrearProductos, name="CrearProductos"),
    path('editarProductoServicio/',views.editarProductoServicio , name="editarProductoServicio"),
    path('reportes/', views.reportes, name="reportes"),
    path('admin/', admin.site.urls), 
    path('register/', views.register, name="register"),
]
  