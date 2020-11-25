from django.shortcuts import render, HttpResponse

html_base = """
    <h1>Mi empresa</h1>
    <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/empresas/">Empresas</a></li>
        <li><a href="/productoServicios">Productos y Servicios</a></li>
        <li><a href="/reportes/">Reportes</a></li>
    </ul>
"""

def home(request):
    return render(request,"core/home.html")

def empresas(request):
    return render(request,"core/empresas.html")

def productoServicios(request):
    return render(request,"core/productoServicios.html")

def reportes(request):
    return render(request,"core/reportes.html")