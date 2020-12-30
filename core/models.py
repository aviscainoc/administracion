# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Afiliacion(models.Model):
    codigo = models.CharField(primary_key=True, max_length=30)
    estado = models.CharField(max_length=10)
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='fechaFin', blank=True, null=True)  # Field name made lowercase.
    fechavalidacion = models.DateTimeField(db_column='fechaValidacion', blank=True, null=True)  # Field name made lowercase.
    usuarioafiliadoid = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioafiliadoid', related_name='usuarioafiliadoid')
    usuariovalidadorid = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuariovalidadorid', blank=True, null=True)
    comentariosaprobacion = models.CharField(max_length=500, blank=True, null=True)
    urlcombprobante1 = models.CharField(max_length=200, blank=True, null=True)
    urlcombprobante2 = models.CharField(max_length=200, blank=True, null=True)
    costoafiliacion = models.FloatField()
    referenciaafiliacioncodigo = models.ForeignKey('self', models.DO_NOTHING, db_column='referenciaafiliacioncodigo', blank=True, null=True)
    precioafiliacion = models.ForeignKey('Precioafiliacion', models.DO_NOTHING, blank=True, null=True)
    pagonivel1 = models.IntegerField(blank=True, null=True)
    pagonivel2 = models.IntegerField(blank=True, null=True)
    cuentapagocomision = models.CharField(max_length=100, blank=True, null=True)
    bancopagocomision = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'afiliacion'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categoria(models.Model):
    activa = models.IntegerField()
    icono = models.CharField(max_length=200, blank=True, null=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    categoriapadre = models.ForeignKey('self', models.DO_NOTHING, db_column='categoriapadre', blank=True, null=True)
    esprincipal = models.IntegerField()
    logo = models.CharField(max_length=200, blank=True, null=True)
    tienehijos = models.IntegerField()
    mall = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categoria'


class Categoriaempresa(models.Model):
    activa = models.IntegerField()
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    icono = models.CharField(max_length=200, blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    categoriaempresapadre = models.ForeignKey('self', models.DO_NOTHING, db_column='categoriaempresapadre', blank=True, null=True)
    esprincipal = models.IntegerField()
    logo = models.CharField(max_length=200, blank=True, null=True)
    tienehijos = models.IntegerField()
    esservicio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categoriaempresa'


class Compra(models.Model):
    id = models.BigAutoField(primary_key=True)
    idusuariocliente = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuariocliente',related_name='idusuariocliente')
    particionmes = models.CharField(max_length=10)
    fechacompra = models.DateTimeField()
    codigomotorizado = models.CharField(max_length=20)
    fechadespachado = models.DateTimeField(blank=True, null=True)
    codigoentregacliente = models.CharField(max_length=20)
    iva = models.CharField(max_length=45)
    subtotal = models.FloatField()
    total = models.FloatField()
    comisionventa = models.FloatField()
    descuento = models.FloatField()
    latitudentrega = models.FloatField()
    longitudentrega = models.FloatField()
    costoentrega = models.FloatField()
    fechaentrega = models.DateTimeField(blank=True, null=True)
    distanciaentrega = models.FloatField()
    direccionentrega = models.CharField(max_length=200)
    telefonocontactoentrega = models.CharField(max_length=12)
    cedulafactura = models.CharField(max_length=20)
    nombrefactura = models.CharField(max_length=100)
    direccionfactura = models.CharField(max_length=200)
    telefonofactura = models.CharField(max_length=12, blank=True, null=True)
    despachado = models.IntegerField()
    entregado = models.IntegerField()
    reversado = models.IntegerField()
    pagovendedor = models.IntegerField()
    idusuariomotorizado = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='idusuariomotorizado', related_name='idusuariomotorizado', blank=True, null=True)
    observacionescliente = models.CharField(max_length=200, blank=True, null=True)
    referenciapago = models.CharField(max_length=100, blank=True, null=True)
    direccionposible = models.CharField(max_length=300, blank=True, null=True)
    metodopago = models.CharField(max_length=30)
    estado = models.CharField(max_length=45)
    idempresa = models.IntegerField()
    fechareverso = models.DateTimeField(blank=True, null=True)
    motivoreverso = models.CharField(max_length=500, blank=True, null=True)
    diacompra = models.DateField()
    idsucursal = models.IntegerField()
    aceptacionvendedor = models.IntegerField(blank=True, null=True)
    fechaaceptacionvendedor = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compra'


class Compradetalle(models.Model):
    id = models.BigAutoField(primary_key=True)
    idcompra = models.BigIntegerField()
    idproducto = models.ForeignKey('Promocionproducto', models.DO_NOTHING, db_column='idproducto')
    preciounitario = models.FloatField()
    cantidad = models.IntegerField()
    subtotal = models.FloatField()
    particionmes = models.CharField(max_length=10)
    observacionescliente = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compradetalle'


class Creditcard(models.Model):
    id = models.BigIntegerField(primary_key=True)
    usuarioid = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioid',related_name='usuarioid')
    token = models.CharField(max_length=200)
    transaction_reference = models.CharField(max_length=200)
    bin = models.CharField(max_length=45)
    binenmascarado = models.CharField(max_length=100)
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    message = models.CharField(max_length=45)
    number = models.CharField(max_length=45)
    origin = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    fechainicio = models.DateTimeField()
    fechafin = models.DateTimeField()
    imeiregistro = models.CharField(max_length=50, blank=True, null=True)
    ipregistro = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'creditcard'


class Cupon(models.Model):
    id = models.BigAutoField(primary_key=True)
    activa = models.IntegerField()
    codigo = models.CharField(max_length=200)
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    fechaeliminacion = models.DateTimeField(db_column='fechaEliminacion', blank=True, null=True)  # Field name made lowercase.
    fechareclamacion = models.DateTimeField(db_column='fechaReclamacion', blank=True, null=True)  # Field name made lowercase.
    fechavalidez = models.DateTimeField(db_column='fechaValidez')  # Field name made lowercase.
    reclamado = models.IntegerField()
    usuariovalidador = models.BigIntegerField(db_column='usuarioValidador', blank=True, null=True)  # Field name made lowercase.
    vecesreclamado = models.IntegerField(blank=True, null=True)
    promocion_idpromocion = models.ForeignKey('Promocionproducto', models.DO_NOTHING, db_column='Promocion_idPromocion')  # Field name made lowercase.
    usuario_idusuarioreclamador = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_idUsuarioReclamador', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cupon'


class Dia(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dia'


class Diaatencion(models.Model):
    horaapertura = models.CharField(db_column='horaApertura', max_length=10, blank=True, null=True)  # Field name made lowercase.
    horacierre = models.CharField(db_column='horaCierre', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dia_iddia = models.ForeignKey(Dia, models.DO_NOTHING, db_column='Dia_idDia')  # Field name made lowercase.
    sucursal_idsucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='Sucursal_idSucursal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'diaatencion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empresa(models.Model):
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    eslogan = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='fechaFin')  # Field name made lowercase.
    nombre = models.CharField(max_length=100)
    top = models.IntegerField()
    twitter = models.CharField(max_length=200, blank=True, null=True)
    urlbaner = models.CharField(db_column='urlBaner', max_length=200, blank=True, null=True)  # Field name made lowercase.
    urlfotoperfil = models.ImageField(upload_to="ftperfil", db_column='urlFotoPerfil', blank=True, null=True)  # Field name made lowercase.
    vecesvisitada = models.IntegerField(db_column='vecesVisitada')  # Field name made lowercase.
    web = models.CharField(max_length=200, blank=True, null=True)
    usuariocomision = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='UsuarioComision_id', blank=True, null=True)  # Field name made lowercase.
    slug = models.CharField(max_length=150, blank=True, null=True)
    estado = models.CharField(max_length=10)
    comision = models.FloatField(blank=True, null=True)
    servicios = models.IntegerField()
    horaapertura = models.CharField(max_length=5)
    horacierre = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'empresa'


class EmpresaEmpresacategoria(models.Model):
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id')  # Field name made lowercase.
    empresacategorialist = models.OneToOneField('Empresacategoria', models.DO_NOTHING, db_column='empresacategoriaList_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresa_empresacategoria'


class Empresacategoria(models.Model):
    activa = models.IntegerField()
    categoriaempresa_idcategoriaempresa = models.ForeignKey(Categoriaempresa, models.DO_NOTHING, db_column='CategoriaEmpresa_idCategoriaEmpresa')  # Field name made lowercase.
    empresa_idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_idEmpresa')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empresacategoria'


class IdGen(models.Model):
    gen_name = models.CharField(primary_key=True, max_length=255)
    gen_val = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'id_gen'


class Multimedia(models.Model):
    activa = models.IntegerField()
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    esimagen = models.IntegerField(db_column='esImagen')  # Field name made lowercase.
    esprincipal = models.IntegerField(db_column='esPrincipal')  # Field name made lowercase.
    fechacreado = models.DateTimeField(db_column='fechaCreado')  # Field name made lowercase.
    fechamodificado = models.DateTimeField(db_column='fechaModificado', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=200, blank=True, null=True)
    thumb = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100)
    urlinterna = models.IntegerField(db_column='urlInterna')  # Field name made lowercase.
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_id', blank=True, null=True)  # Field name made lowercase.
    promocion_idpromocion = models.ForeignKey('Promocionproducto', models.DO_NOTHING, db_column='Promocion_idPromocion', blank=True, null=True)  # Field name made lowercase.
    web = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'multimedia'


class Notificacion(models.Model):
    activa = models.IntegerField()
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    notificacioncol = models.CharField(max_length=45, blank=True, null=True)
    vista = models.SmallIntegerField()
    promocionproducto = models.ForeignKey('Promocionproducto', models.DO_NOTHING, db_column='PromocionProducto_id')  # Field name made lowercase.
    tiponotificacion_idtiponotificacion = models.ForeignKey('Tiponotificacion', models.DO_NOTHING, db_column='TipoNotificacion_idTipoNotificacion')  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_idUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notificacion'


class Pago(models.Model):
    fecha = models.DateTimeField()
    iva = models.FloatField()
    numerofactura = models.CharField(db_column='numeroFactura', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tienefactura = models.SmallIntegerField(db_column='tieneFactura')  # Field name made lowercase.
    urlfactura = models.CharField(db_column='urlFactura', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField()
    promocionproducto = models.ForeignKey('Promocionproducto', models.DO_NOTHING, db_column='PromocionProducto_id')  # Field name made lowercase.
    usuario_registrador = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_Registrador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pago'


class Pagocomisionafiliacion(models.Model):
    id = models.IntegerField(primary_key=True)
    comentario = models.CharField(max_length=200)
    total = models.FloatField()
    nivel = models.IntegerField()
    fechapago = models.DateTimeField()
    estado = models.CharField(max_length=10)
    afiliacion_codigo = models.ForeignKey(Afiliacion, models.DO_NOTHING, db_column='afiliacion_codigo')

    class Meta:
        managed = False
        db_table = 'pagocomisionafiliacion'


class Parametros(models.Model):
    clave = models.CharField(primary_key=True, max_length=255)
    fechavigente = models.DateTimeField(db_column='fechaVigente')  # Field name made lowercase.
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    fechamodificacion = models.DateTimeField(db_column='fechaModificacion')  # Field name made lowercase.
    valor = models.CharField(max_length=2000, blank=True, null=True)
    usuariocreacion = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioCreacion',related_name='usuarioCreacion')  # Field name made lowercase.
    usuariomodificacion = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioModificacion',related_name='usuarioModificacion')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'parametros'
        unique_together = (('clave', 'fechavigente'),)


class Passwordrecover(models.Model):
    id = models.BigAutoField(primary_key=True)
    activo = models.IntegerField()
    fechacaducidad = models.DateTimeField(db_column='fechaCaducidad')  # Field name made lowercase.
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    fechaultimocorreoenviado = models.DateTimeField(db_column='fechaUltimoCorreoEnviado', blank=True, null=True)  # Field name made lowercase.
    fechauso = models.DateTimeField(db_column='fechaUso', blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(max_length=200)
    usado = models.IntegerField()
    vecescorreoenviado = models.IntegerField(db_column='vecesCorreoEnviado')  # Field name made lowercase.
    verificationcode = models.CharField(max_length=100)
    usuario_solicitud = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_Solicitud')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'passwordrecover'


class Planpromo(models.Model):
    activo = models.IntegerField()
    descripcion = models.CharField(max_length=1000)
    dias = models.IntegerField()
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    ganaciaporcomision = models.IntegerField(db_column='ganaciaPorComision')  # Field name made lowercase.
    nombre = models.CharField(max_length=200)
    porcentajeganancia = models.FloatField(db_column='porcentajeGanancia')  # Field name made lowercase.
    precio = models.FloatField()
    prioridad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'planpromo'


class Precioafiliacion(models.Model):
    nombre = models.CharField(unique=True, max_length=100)
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=10)
    fechainicio = models.DateTimeField(db_column='fechaInicio')  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='fechaFin')  # Field name made lowercase.
    precio = models.FloatField()
    usuariocreacionid = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuariocreacionid')
    precioreferido = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'precioafiliacion'


class Productocategoria(models.Model):
    activa = models.IntegerField()
    categoria_idcategoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='Categoria_idCategoria')  # Field name made lowercase.
    promocionproducto = models.ForeignKey('Promocionproducto', models.DO_NOTHING, db_column='PromocionProducto_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productocategoria'


class Promocionproducto(models.Model):
    id = models.BigIntegerField(primary_key=True)
    comentarios = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=600)
    esbaner = models.IntegerField(db_column='esBaner')  # Field name made lowercase.
    estado = models.CharField(max_length=10)
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    fechafinenlaplataforma = models.DateTimeField(db_column='fechaFinEnLaPlataforma')  # Field name made lowercase.
    fechafinpromocion = models.DateTimeField(db_column='fechaFinPromocion')  # Field name made lowercase.
    fechainiciopromocion = models.DateTimeField(db_column='fechaInicioPromocion')  # Field name made lowercase.
    fechamodificacion = models.DateTimeField()
    gananciacupon = models.FloatField(db_column='gananciaCupon')  # Field name made lowercase.
    mostrarprecio = models.IntegerField()
    mostrarprocentajedescuento = models.IntegerField()
    nombre = models.CharField(max_length=200)
    numerocuponespromo = models.IntegerField(db_column='numeroCuponesPromo')  # Field name made lowercase.
    numerocuponesusados = models.IntegerField(db_column='numeroCuponesUsados', blank=True, null=True)  # Field name made lowercase.
    porcentajedescuentoparaclientes = models.FloatField(db_column='porcentajeDescuentoParaClientes', blank=True, null=True)  # Field name made lowercase.
    precioactual = models.FloatField(db_column='precioActual', blank=True, null=True)  # Field name made lowercase.
    precioinicial = models.FloatField(db_column='precioInicial', blank=True, null=True)  # Field name made lowercase.
    prioridad = models.IntegerField(blank=True, null=True)
    restricciones = models.CharField(max_length=200, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    tienecupones = models.IntegerField(db_column='tieneCupones')  # Field name made lowercase.
    valorahorro = models.FloatField(db_column='valorAhorro')  # Field name made lowercase.
    vecesvista = models.IntegerField(db_column='vecesVista')  # Field name made lowercase.
    empresa_idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_idEmpresa')  # Field name made lowercase.
    usuariomodificador = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='UsuarioModificador_id',related_name='UsuarioModificador_id')  # Field name made lowercase.
    usuarioregistrador = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='UsuarioRegistrador_id')  # Field name made lowercase.
    cabecera = models.CharField(max_length=200, blank=True, null=True)
    fondo = models.CharField(max_length=200, blank=True, null=True)
    pie = models.CharField(max_length=200, blank=True, null=True)
    tienefondo = models.IntegerField()
    tipo = models.CharField(max_length=200, blank=True, null=True)
    servicio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'promocionproducto'


class Promocionproductohistorial(models.Model):
    id = models.BigAutoField(primary_key=True)
    comentarios = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=200)
    esbaner = models.IntegerField(db_column='esBaner')  # Field name made lowercase.
    estado = models.CharField(max_length=255)
    fdesde = models.DateTimeField()
    fechacreacion = models.DateTimeField(db_column='fechaCreacion', blank=True, null=True)  # Field name made lowercase.
    fechafinenlaplataforma = models.DateTimeField(db_column='fechaFinEnLaPlataforma')  # Field name made lowercase.
    fechafinpromocion = models.DateTimeField(db_column='fechaFinPromocion')  # Field name made lowercase.
    fechainiciopromocion = models.DateTimeField(db_column='fechaInicioPromocion')  # Field name made lowercase.
    fechamodificacion = models.DateTimeField()
    gananciacupon = models.FloatField(db_column='gananciaCupon')  # Field name made lowercase.
    idpromocion = models.BigIntegerField()
    mostrarprecio = models.IntegerField()
    mostrarprocentajedescuento = models.IntegerField()
    nombre = models.CharField(max_length=200)
    numerocuponespromo = models.IntegerField(db_column='numeroCuponesPromo')  # Field name made lowercase.
    numerocuponesusados = models.IntegerField(db_column='numeroCuponesUsados', blank=True, null=True)  # Field name made lowercase.
    porcentajedescuentoparaclientes = models.FloatField(db_column='porcentajeDescuentoParaClientes', blank=True, null=True)  # Field name made lowercase.
    precioactual = models.FloatField(db_column='precioActual', blank=True, null=True)  # Field name made lowercase.
    precioinicial = models.FloatField(db_column='precioInicial', blank=True, null=True)  # Field name made lowercase.
    prioridad = models.IntegerField(blank=True, null=True)
    restricciones = models.CharField(max_length=200, blank=True, null=True)
    tienecupones = models.IntegerField(db_column='tieneCupones')  # Field name made lowercase.
    valorahorro = models.FloatField(db_column='valorAhorro')  # Field name made lowercase.
    vecesvista = models.IntegerField(db_column='vecesVista')  # Field name made lowercase.
    empresa_idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_idEmpresa')  # Field name made lowercase.
    usuariomodificador = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='UsuarioModificador_id')  # Field name made lowercase.
    usuarioregistrador = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='UsuarioRegistrador_id',related_name='UsuarioRegistrador_id')  # Field name made lowercase.
    slug = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promocionproductohistorial'


class Rol(models.Model):
    activo = models.IntegerField()
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'rol'


class Seccion(models.Model):
    activa = models.IntegerField()
    descripcion = models.CharField(max_length=1000)
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    nombre = models.CharField(max_length=100)
    empresa_idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_idEmpresa')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seccion'


class Sesion(models.Model):
    id = models.BigAutoField(primary_key=True)
    agente = models.CharField(max_length=500, blank=True, null=True)
    dispositivo = models.CharField(max_length=45, blank=True, null=True)
    estado = models.CharField(max_length=45)
    fechamodificacion = models.DateTimeField(db_column='fechaModificacion', blank=True, null=True)  # Field name made lowercase.
    fechacreacion = models.DateTimeField()
    fechaexpiracion = models.DateTimeField()
    fechainicio = models.DateTimeField()
    firebase = models.CharField(max_length=500, blank=True, null=True)
    ip = models.CharField(max_length=45)
    token = models.CharField(max_length=500)
    usuarioid = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioid')

    class Meta:
        managed = False
        db_table = 'sesion'


class Sucursal(models.Model):
    activa = models.IntegerField()
    direccion = models.CharField(max_length=100)
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    horaapertura = models.CharField(db_column='horaApertura', max_length=5, blank=True, null=True)  # Field name made lowercase.
    horacierre = models.CharField(db_column='horaCierre', max_length=5, blank=True, null=True)  # Field name made lowercase.
    latitud = models.CharField(max_length=45, blank=True, null=True)
    longitud = models.CharField(max_length=45, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    telefono1 = models.CharField(max_length=10, blank=True, null=True)
    telefono2 = models.CharField(max_length=10, blank=True, null=True)
    urlfotoperfil = models.CharField(db_column='urlFotoPerfil', max_length=200, blank=True, null=True)  # Field name made lowercase.
    empresa_idempresa = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='Empresa_idEmpresa')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sucursal'


class Tarjeta(models.Model):
    id = models.BigAutoField(primary_key=True)
    activa = models.IntegerField()
    codigo = models.CharField(unique=True, max_length=200)
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    fechaeliminacion = models.DateTimeField(db_column='fechaEliminacion', blank=True, null=True)  # Field name made lowercase.
    fechavalidez = models.DateTimeField(db_column='fechaValidez')  # Field name made lowercase.
    usuarioreclamador = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuarioReclamador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tarjeta'


class Tiponotificacion(models.Model):
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiponotificacion'


class Usariopublicacionguardada(models.Model):
    activa = models.IntegerField()
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    promocionproducto = models.ForeignKey(Promocionproducto, models.DO_NOTHING, db_column='PromocionProducto_id')  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_idUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usariopublicacionguardada'


class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    activo = models.IntegerField()
    apellidos = models.CharField(max_length=60)
    cedula = models.CharField(max_length=10, blank=True, null=True)
    celular = models.CharField(max_length=10, blank=True, null=True)
    codigoactivacion = models.CharField(db_column='codigoActivacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comentarios = models.CharField(max_length=200, blank=True, null=True)
    correo = models.CharField(unique=True, max_length=45)
    cuentaconfb = models.IntegerField(db_column='cuentaConFb')  # Field name made lowercase.
    cuentaconfirmada = models.IntegerField(db_column='cuentaConfirmada')  # Field name made lowercase.
    facebookid = models.CharField(db_column='facebookId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    fechanacimiento = models.DateTimeField(db_column='fechaNacimiento', blank=True, null=True)  # Field name made lowercase.
    fechaultimologin = models.DateTimeField(db_column='fechaUltimoLogin', blank=True, null=True)  # Field name made lowercase.
    genero = models.CharField(max_length=255, blank=True, null=True)
    intentosfallidos = models.IntegerField(db_column='intentosFallidos', blank=True, null=True)  # Field name made lowercase.
    nombres = models.CharField(max_length=60)
    password = models.CharField(max_length=100)
    passwordtemporal = models.CharField(db_column='passwordTemporal', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(max_length=10, blank=True, null=True)
    tokenfb = models.CharField(db_column='tokenFB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    urlfoto = models.CharField(db_column='urlFoto', max_length=200, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Usuarioempresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    activa = models.IntegerField()
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='Usuario_id')  # Field name made lowercase.
    puedeeditarpromociones = models.IntegerField()
    puedevalidarcupon = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuarioempresa'


class Usuariorol(models.Model):
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    rol_idrol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='Rol_idRol')  # Field name made lowercase.
    usuario_idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='Usuario_idUsuario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuariorol'


class Validacuenta(models.Model):
    idvalidacuenta = models.BigIntegerField(primary_key=True)
    correo = models.CharField(max_length=45)
    uuid = models.CharField(max_length=100)
    fechacreacion = models.DateTimeField(db_column='fechaCreacion')  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='fechaFin')  # Field name made lowercase.
    validado = models.IntegerField()
    fechavalidacion = models.DateTimeField(db_column='fechaValidacion')  # Field name made lowercase.
    ip = models.CharField(max_length=45, blank=True, null=True)
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING)
    token = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'validacuenta'
