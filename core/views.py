from django.shortcuts import render, HttpResponse
import mysql.connector as mcdb
import datetime 
  



from core.models import Empresa

#aqui creamos la conexion con la base
conn =mcdb.connect(host="localhost", user="root", passwd="cuenca", database="promoscuencav2")

print('conexion exitosa a la base promoshop')
cur=conn.cursor()


# Gestion empresas
def home(request):
    return render(request,"core/home.html")

def editarEmpresa(request, id):
    
    print("Llega al metodo y su id es: ",id)
    cur.execute("select * from empresa where id = {}".format(id))
    empresas = cur.fetchone()
    #return list(data)
    print(list(empresas))
    #empresas= Empresa.
    return render(request,"core/editarEmpresa.html",{'editarEmpresa':empresas})


def empresas(request):
    cur.execute("select co.id, co.nombre, co.fechaCreacion, co.estado from empresa as co ")
    datos= cur.fetchall()     
    return render(request,'core/empresas.html',{'empresa':datos})

def crearEmpresa(request):
    cur.execute("select co.id, co.nombre from categoriaempresa as co ")
    datos= cur.fetchall()    
    # print(list(datos) ,'\n')   
    if request.method == 'POST':
        logo = request.POST["image"]
        empres = request.POST['empresa']
        slogan = request.POST['slogan']
        descripcion = request.POST['desc']
        facebook = request.POST['face']
        twritter = request.POST['twritter']
        pagWeb = request.POST['web']
        catServicio=request.POST['opcion1']
        porcetComision = request.POST['porcentaje']
        HoraAbre=request.POST['abre']
        HoraCierra=request.POST['cierra']

        estado="PEN"

        d = datetime.date(2020, 12, 17) 

        #insertar datos
        empr = Empresa(descripcion=descripcion,eslogan=slogan,facebook=facebook,nombre=empres,twitter=twritter,web=pagWeb,
        fechacreacion=d ,fechafin=d, top=0, vecesvisitada=10,servicios= 0, slug=catServicio,comision=porcetComision,
        estado=estado, horaapertura=HoraAbre,horacierre=HoraCierra )
        
        empr.save()
        print("datos de empresa: ",empr)
        print("empresa creada")

    return render(request,'core/crearEmpresa.html',{'categoriaempresa':datos})
     
#Gestion Productos
def productoServicios(request):
    cur.execute("select prod.id, prod.nombre, prod.estado, em.nombre from promocionproducto as prod, empresa as em where prod.Empresa_idEmpresa = em.id")
    datosProductos= cur.fetchall()    
      
    return render(request,"core/productoServicios.html",{'promocionproducto':datosProductos})

def CrearProductos(request):
    return render(request,"core/CrearProductos.html")

def editarProductoServicio(request):
    return render(request,"core/editarProductoServicio.html")

#Gestion Login y Registro de Users
def login(request):
    return render(request,"core/login.html")

def registrarse(request):
    return render(request,"core/registrarse.html")

def recuperarContrasenia(request):
    return render(request,"core/recuperarContrasenia.html")

#Gestion Reportes
def reportes(request):
    return render(request,"core/reportes.html")




#metodo para leer la base y hacer consultas
