from django.shortcuts import render, HttpResponse
import mysql.connector as mcdb


#aqui creamos la conexion con la base
conn =mcdb.connect(host="localhost", user="root", passwd="cuenca", database="promoscuencav2")

print('conexion exitosa a la base promoshop')
cur=conn.cursor()


# recordar siempre debo instalar  pip install mysql-connector
html_base = """
    <h1>Mi empresa</h1>
    <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/empresas/">Empresas</a></li>
        <li><a href="/productoServicios">Productos y Servicios</a></li>
        <li><a href="/reportes/">Reportes</a></li>
        <li><a href="/login/">Iniciar Sesion</a></li>
    </ul>
"""


def home(request):
    return render(request,"core/home.html")

def empresas(request):

    cur.execute()

    cur.execute("select pro.id, pro.nombre, co.fechaCreacion from empresa as co ")
    datos= cur.fetchall()    
    print(list(datos) ,'\n')    
    return render(request,'core/empresas.html',{'empresa':datos})


def productoServicios(request):
    return render(request,"core/productoServicios.html")

def reportes(request):
    return render(request,"core/reportes.html")



def register(request):
    return render(request, "core/register.html")
  

def login(request):
    return render(request,"core/login.html")


#metodo para leer la base y hacer consultas
