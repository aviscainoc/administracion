from django.shortcuts import render, HttpResponse

def home(request):
    return render(request,"core/home.html")

def empresas(request):
    return render(request,"core/empresas.html")

def productoServicios(request):
    return render(request,"core/productoServicios.html")

def reportes(request):
    return render(request,"core/reportes.html")


def register(request):
    return render(request, "core/register.html")
  