from django.shortcuts import render, HttpResponse
import mysql.connector as mcdb
import datetime 
from core.models import Empresa
from core.models import Usuario
from core.models import Usuariorol

#aqui creamos la conexion con la base
conn =mcdb.connect(host="localhost", user="root", passwd="cuenca", database="promoscuencav2")

print('conexion exitosa a la base promoshop')
cur=conn.cursor()


# Gestion empresas
def home(request):
    return render(request,"core/home.html")

def editarEmpresa(request, id):
    
    cur.execute("select * from empresa where id = {}".format(id))
    editarEmpresa = cur.fetchone()
    #return list(data)
    print ("Datos de edicion:")
    print(list(editarEmpresa))
    #mpresas= Empresa.
    return render(request,"core/editarEmpresa.html",{'editarEmpresa':editarEmpresa})


def empresas(request):
    cur.execute("select co.id, co.nombre, co.fechaCreacion, co.estado from empresa as co ")
    datos= cur.fetchall()     
    return render(request,'core/empresas.html',{'empresa':datos})

def RecuperarEmpresas(request):
    cur.execute("select co.id, co.nombre, co.fechaCreacion, co.estado from empresa as co ")
    datos= cur.fetchall()    
    ## print(list(datos)) 
    return render(request,'core/reportes.html',{'reporte':datos})    

def editarContrasenia(request, id):
    
    cur.execute("select us.Usuario_id from usuarioempresa as us where us.empresa_id = {}".format(id))
    usuarioEmpresa = cur.fetchall()
    idUserEmpr=usuarioEmpresa
    print("datos encontrados")
    print(idUserEmpr)
    ##cur.execute("select * from usuario as u where u.id = {}".format(usuarioEmpresa))
    ##usuarioCorreo = cur.fetchone()
    #return list(data)
    print ("Datos de edicion:")
    ##print(usuarioCorreo)
    #mpresas= Empresa.
    return render(request,"core/editarEmpresa.html",{'editarEmpresa':editarEmpresa})


def crearEmpresa(request):
    cur.execute("select co.id, co.nombre from categoriaempresa as co ")
    datos= cur.fetchall()    
    # print(list(datos) ,'\n')   
    if request.method == 'POST':

        if bool(request.FILES.get('image',False))==True:
            logo=request.FILES['image']
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

        
        fechaActual = datetime.datetime.now()

        #insertar datos
        empresa = Empresa(descripcion=descripcion,eslogan=slogan,facebook=facebook,nombre=empres,twitter=twritter,web=pagWeb,
        fechacreacion=fechaActual ,fechafin=fechaActual, top=0, vecesvisitada=0,servicios= 0, slug=catServicio,comision=porcetComision,
        estado=estado, horaapertura=HoraAbre,horacierre=HoraCierra, urlfotoperfil=logo)
        
        empresa.save()
        print("empresa creada")


    return render(request,'core/crearEmpresa.html',{'categoriaempresa':datos})
     
#Gestion Productos
def productoServicios(request):
    cur.execute("select prod.id, prod.nombre, prod.estado, em.nombre from promocionproducto as prod, empresa as em where prod.Empresa_idEmpresa = em.id")
    datosProductos= cur.fetchall() 
       
      
    return render(request,"core/productoServicios.html",{'promocionproducto':datosProductos})

def CrearProductos(request):
    return render(request,"core/CrearProductos.html")

def editarProductoServicio(request, id):
    cur.execute("select * from empresa where id = {}".format(id))
    editarEmpresa = cur.fetchone()
    #return list(data)
    print ("Datos de edicion:")
    print(list(editarEmpresa))
    #mpresas= Empresa.
    return render(request,"core/editarEmpresa.html",{'editarEmpresa':editarEmpresa})
    
    return render(request,"core/editarProductoServicio.html")

#Gestion Login y Registro de Users
def login(request):

    if request.method == 'POST':
        usuario = request.POST['correo']
        password= request.POST['pass']
        print("datos : ",usuario, "  : ",password)  

 
    
    
    return render(request,"core/login.html")

def registrarse(request):
    return render(request,"core/registrarse.html")

def recuperarContrasenia(request):
    return render(request,"core/recuperarContrasenia.html")

#Gestion Reportes
def reportes(request):
    return render(request,"core/reportes.html")




#metodo para leer la base y hacer consultas
