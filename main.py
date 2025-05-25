import jwt
from flask import Flask, request, jsonify
from functools import wraps

#Improtar clases de otras carpetas del proyecto
from Entidades import Conductores
from Entidades import Vehiculos
from Entidades import Tipo_Envio
from Entidades import Usuarios
from Entidades import Incidencias
from Entidades import MetodosPago
from Entidades import Pagos
from Entidades import Ciudades
from Entidades import Seguimiento

from Entidades import Estados
from Entidades import Pedido
from Entidades import Rutas
from Entidades import Zonas
from Entidades import Departamento


from Repositorios import ConductoresRepositorio
from Repositorios import VehiculosRepositorio
from Repositorios import TipoEnvioRepositorio
from Repositorios import UsuariosRepositorio
from Repositorios import IncidenciasRepositorio
from Repositorios import MetodosPagoRepositorio
from Repositorios import PagosRepositorio
from Repositorios import CiudadesRepositorio
from Repositorios import SeguimientoRepositorio
from Repositorios import EstadosRepositorio
from Repositorios import PedidosRepositorio
from Repositorios import RutasRepositorio
from Repositorios import ZonasRepositorio
from Repositorios import DepartamentoRepositorio
from Utilidades import EncriptarAES
from datetime import datetime
from Seguridad.JWT import SeguridadJWT as JWT


#Definicion metodo Main
def main():
   
   #--CONDUCTOR

   #Inicializacion de datos
   id=1
   nombre="Jorge luis parra"
   cedula="1003"
   telefono="301378973"

   #Insertar
   #Creo Objeto conductor
   #conductor = Conductores.Conductores(id,nombre,cedula,telefono)
   #Creo objeto de repositorio conductores 
   #repositorio = ConductoresRepositorio.ConductoresRepositorio()
   #Utilizo metodo guardar que me recibe el objeto conductor
   #repositorio.Guardar(conductor)
   
   #Actualizar
   #Creo Objeto conductor
   #conductor = Conductores.Conductores(id,nombre,cedula,telefono)
   #Creo objeto de repositorio conductores 
   #repositorio = ConductoresRepositorio.ConductoresRepositorio()
   #Utilizo metodo guardar que me recibe el objeto conductor
   #repositorio.Actualizar(conductor)

   #Eliminar
   #Creo Objeto conductor
   #conductor = Conductores.Conductores(id,nombre,cedula,telefono)
   #Creo objeto de repositorio conductores 
   #repositorio = ConductoresRepositorio.ConductoresRepositorio()
   #Utilizo metodo guardar que me recibe el objeto conductor
   #repositorio.Eliminar(conductor)

   #Consultar
   #Creo Objeto conductor
   #conductor = Conductores.Conductores(id,nombre,cedula,telefono)
   #Creo objeto de repositorio conductores 
   #repositorio = ConductoresRepositorio.ConductoresRepositorio()
   #Utilizo metodo guardar que me recibe el objeto conductor
   #repositorio.Consultar(conductor)

   #--VEHICULO

    #Inicializacion de datos
   id=2
   placa="GH1245"
   tipo="Moto BMW"
   capacidad=160

   #Insertar
   #Creo Objeto vehiculo
   #vehiculo = Vehiculos.Vehiculos(id,placa,tipo,capacidad)
   #Creo objeto de repositorio vehiculo
   #repositorio = VehiculosRepositorio.VehiculosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto vehiculo
   #repositorio.Guardar(vehiculo)

   #Actualizar
   #Creo Objeto vehiculo
   #vehiculo = Vehiculos.Vehiculos(id,placa,tipo,capacidad)
   #Creo objeto de repositorio vehiculo
   #repositorio = VehiculosRepositorio.VehiculosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto vehiculo
   #repositorio.Actualizar(vehiculo)

   #Eliminar
   #Creo Objeto vehiculo
   #vehiculo = Vehiculos.Vehiculos(id,placa,tipo,capacidad)
   #Creo objeto de repositorio vehiculo
   #repositorio = VehiculosRepositorio.VehiculosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto vehiculo
   #repositorio.Eliminar(vehiculo)

   #Consultar
   #Creo Objeto vehiculo
   #vehiculo = Vehiculos.Vehiculos(id,placa,tipo,capacidad)
   #Creo objeto de repositorio vehiculo
   #repositorio = VehiculosRepositorio.VehiculosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto vehiculo
   #repositorio.Consultar(vehiculo)


   #--TIPO ENVIO

    #Inicializacion de datos
   id=2
   nombre="Delicado2"

   #Insertar
   #Creo Objeto envio
   #tipoenvio = Tipo_Envio.Tipo_Envio(id,nombre)
   #Creo objeto de repositorio tipo envio 
   #repositorio = TipoEnvioRepositorio.TipoEnvioRepositorio()
   #Utilizo metodo guardar que me recibe el objeto envio
   #repositorio.Guardar(tipoenvio)

   #Actualizar
   #Creo Objeto envio
   #tipoenvio = Tipo_Envio.Tipo_Envio(id,nombre)
   #Creo objeto de repositorio envio
   #repositorio = TipoEnvioRepositorio.TipoEnvioRepositorio()
   #Utilizo metodo guardar que me recibe el objeto envio
   #repositorio.Actualizar(tipoenvio)

   #Eliminar
   #Creo Objeto envio
   #tipoenvio = Tipo_Envio.Tipo_Envio(id,nombre)
   #Creo objeto de repositorio envio
   #repositorio = TipoEnvioRepositorio.TipoEnvioRepositorio()
   #Utilizo metodo guardar que me recibe el objeto envio
   #repositorio.Eliminar(tipoenvio)

   #Consultar
   #Creo Objeto envio
   #tipoenvio = Tipo_Envio.Tipo_Envio(id,nombre)
   #Creo objeto de repositorio envio
   #repositorio = TipoEnvioRepositorio.TipoEnvioRepositorio()
   #Utilizo metodo guardar que me recibe el objeto envio
   #repositorio.Consultar(tipoenvio)


   #--USUARIOS

    #Inicializacion de datos
   id=2
   nombre="Jorge luis parra garcia"
   email="jorge123@gmail.com"
   telefono="3014784269"
   direccion="Calle 39 "
   rol="Administrador"
   fechaRegistro=datetime(2025, 4, 10, 16, 30, 0) 
   
   #Insertar
   #Creo Objeto usuario
   #usuario = Usuarios.Usuarios(id,nombre,email,telefono,direccion,rol,fechaRegistro)
   #Creo objeto de repositorio usuario
   #repositorio = UsuariosRepositorio.UsuariosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto usuario
   #repositorio.Guardar(usuario)

   #Actualizar
   #Creo Objeto usuario
   #usuario = Usuarios.Usuarios(id,nombre,email,telefono,direccion,rol,fechaRegistro)
   #Creo objeto de repositorio usuario
   #repositorio = UsuariosRepositorio.UsuariosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto usuario
   #repositorio.Actualizar(usuario)

   #Eliminar
   #Creo Objeto usuario
   #usuario = Usuarios.Usuarios(id,nombre,email,telefono,direccion,rol,fechaRegistro)
   #Creo objeto de repositorio usuario
   #repositorio = UsuariosRepositorio.UsuariosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto usuario
   #repositorio.Eliminar(usuario)

   #Consultar
   #Creo Objeto usuario
   #usuario = Usuarios.Usuarios(id,nombre,email,telefono,direccion,rol,fechaRegistro)
   #Creo objeto de repositorio usuario
   #repositorio = UsuariosRepositorio.UsuariosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto usuario
   #repositorio.Consultar(usuario)

   #--INCIDENCIAS

    #Inicializacion de datos
   id=2
   pedidoID="3"
   descripcion="paquete mal mal envuelto por usuario"
   fecha=datetime(2025, 4, 10, 16, 30, 30) 
   resuelta=0
   
   #Insertar
   #Creo Objeto incidencia
   #incidencia = Incidencias.Incidencias(id,pedidoID,descripcion,fecha,resuelta)
   #Creo objeto de repositorio incidencia
   #repositorio = IncidenciasRepositorio.IncidenciasRepositorio()
   #Utilizo metodo guardar que me recibe el objeto incidencia
   #repositorio.Guardar(incidencia)

   #Actualizar
   #Creo Objeto incidencia
   #incidencia = Incidencias.Incidencias(id,pedidoID,descripcion,fecha,resuelta)
   #Creo objeto de repositorio incidencia
   #repositorio = IncidenciasRepositorio.IncidenciasRepositorio()
   #Utilizo metodo guardar que me recibe el objeto incidencia
   #repositorio.Actualizar(incidencia)

   #Eliminar
   #Creo Objeto incidencia
   #incidencia = Incidencias.Incidencias(id,pedidoID,descripcion,fecha,resuelta)
   #Creo objeto de repositorio incidencia
   #repositorio = IncidenciasRepositorio.IncidenciasRepositorio()
   #Utilizo metodo guardar que me recibe el objeto incidencia
   #repositorio.Eliminar(incidencia)

   #Consultar
   #Creo Objeto usuario
   #incidencia = Incidencias.Incidencias(id,pedidoID,descripcion,fecha,resuelta)
   #Creo objeto de repositorio usuario
   #repositorio = IncidenciasRepositorio.IncidenciasRepositorio()
   #Utilizo metodo guardar que me recibe el objeto usuario
   #repositorio.Consultar(incidencia)


   #--METODO DE PAGO

   #Inicializacion de datos
   #id = 1
   #nombre = "Tarjeta de debito"

   #Insertar
   #Creo Objeto metodo de pago
   #metodo = MetodosPago.MetodosPago(id, nombre)
   #Creo objeto de repositorio metodo de pago 
   #repositorio = MetodosPagoRepositorio.MetodosPagoRepositorio()
   #Utilizo metodo guardar que me recibe el objeto metodo de pago
   #repositorio.Guardar(metodo)

   #Actualizar
   #Creo Objeto metodo de pago
   #metodo = MetodosPago.MetodosPago(id, nombre)
   #Creo objeto de repositorio metodo de pago 
   #repositorio = MetodosPagoRepositorio.MetodosPagoRepositorio()
   #Utilizo metodo actualizar que me recibe el objeto metodo de pago
   #repositorio.Actualizar(metodo)

   #Eliminar
   #Creo Objeto metodo de pago
   #metodo = MetodosPago.MetodosPago(id, nombre)
   #Creo objeto de repositorio metodo de pago 
   #repositorio = MetodosPagoRepositorio.MetodosPagoRepositorio()
   #Utilizo metodo eliminar que me recibe el objeto metodo de pago
   #repositorio.Eliminar(metodo)

   #Consultar
   #Creo Objeto metodo de pago
   #metodo = MetodosPago.MetodosPago(id, nombre)
   #Creo objeto de repositorio metodo de pago 
   #repositorio = MetodosPagoRepositorio.MetodosPagoRepositorio()
   #Utilizo metodo consultar que me recibe el objeto metodo de pago
   #repositorio.Consultar(metodo)

   #--PAGOS

   #Inicializacion de datos
   #id = 3
   #pedido_id = 3
   #metodo_pago_id= 3
   #valor = 350000.00
   #fecha_pago = datetime(2025, 4, 8, 6, 57)
   #estado_pago = "pagado"

   #Insertar
   #Creo Objeto pago
   #pago = Pagos.Pagos(id, pedido_id, metodo_pago_id, valor, fecha_pago, estado_pago)
   #Creo objeto de repositorio pago 
   #repositorio = PagosRepositorio.PagosRepositorio()
   #Utilizo metodo guardar que me recibe el objeto pago
   #repositorio.Guardar(pago)

   #Actualizar
   #Creo Objeto pago
   #pago = Pagos.Pagos(id, pedido_id, metodo_pago_id, valor, fecha_pago, estado_pago)
   #Creo objeto de repositorio pago 
   #repositorio = PagosRepositorio.PagosRepositorio()
   #Utilizo metodo actualizar que me recibe el objeto pago
   #repositorio.Actualizar(pago)

   #Eliminar
   #Creo Objeto pago
   #pago = Pagos.Pagos(id, pedido_id, metodo_pago_id, valor, fecha_pago, estado_pago)
   #Creo objeto de repositorio pago 
   #repositorio = PagosRepositorio.PagosRepositorio()
   #Utilizo metodo eliminar que me recibe el objeto pago
   #repositorio.Eliminar(pago)

   #Consultar
   #Creo Objeto pago
   #pago = Pagos.Pagos(id, pedido_id, metodo_pago_id, valor, fecha_pago, estado_pago)
   #Creo objeto de repositorio pago 
   #repositorio = PagosRepositorio.PagosRepositorio()
   #Utilizo metodo consultar que me recibe el objeto pago
   #repositorio.Consultar(pago)

   #--CIUDAD

   #Inicializacion de datos
   id = 1
   nombre = "Medellín"
   departamento_id= 1

   #Insertar
   #Creo Objeto ciudad
   #ciudad = Ciudades.Ciudades(id, nombre, departamento_id)
   #Creo objeto de repositorio ciudad 
   #repositorio = CiudadesRepositorio.CiudadesRepositorio()
   #Utilizo metodo guardar que me recibe el objeto ciudad
   #repositorio.Guardar(ciudad)

   #Actualizar
   #ciudad = Ciudades.Ciudades(id, nombre, departamento_id)
   #repositorio = CiudadesRepositorio.CiudadesRepositorio()
   #repositorio.Actualizar(ciudad)

   #Eliminar
   #ciudad = Ciudades.Ciudades(id, nombre, departamento_id)
   #repositorio = CiudadesRepositorio.CiudadesRepositorio()
   #repositorio.Eliminar(ciudad)

   #Consultar
   #ciudad = Ciudades.Ciudades(id, nombre, departamento_id)
   #repositorio = CiudadesRepositorio.CiudadesRepositorio()
   #repositorio.Consultar(ciudad)


   #--SEGUIMIENTO

   #Inicializacion de datos
   #id = 3
   #idpedido = 3
   #estadoid = 3
   #ubicacion = "Entregado"
   #comentario = "Sin inconvenientes"

   #Insertar
   #seguimiento = Seguimiento.Seguimiento(id, idpedido, estadoid, ubicacion, comentario, fechahora)
   #repositorio = SeguimientoRepositorio.SeguimientoRepositorio()
   #repositorio.Guardar(seguimiento)

   #Actualizar
   #seguimiento = Seguimiento.Seguimiento(id, idpedido, estadoid, ubicacion, comentario, fechahora)
   #repositorio = SeguimientoRepositorio.SeguimientoRepositorio()
   #repositorio.Actualizar(seguimiento)

   #Eliminar
   #seguimiento = Seguimiento.Seguimiento(id, idpedido, estadoid, ubicacion, comentario, fechahora)
   #repositorio = SeguimientoRepositorio.SeguimientoRepositorio()
   #repositorio.Eliminar(seguimiento)

   #Consultar
   #seguimiento = Seguimiento.Seguimiento(id, idpedido, estadoid, ubicacion, comentario, fechahora)
   #repositorio = SeguimientoRepositorio.SeguimientoRepositorio()
   #repositorio.Consultar(seguimiento)

   #--ESTADOS

   #Inicializacion de datos
   id = 1
   nombre = "Pendiente"

   #Insertar
   #estado = Estados.Estados(id, nombre)
   #repositorio = EstadosRepositorio.EstadosRepositorio()
   #repositorio.Guardar(estado)

   #Actualizar
   #estado = Estados.Estados(id, nombre)
   #repositorio = EstadosRepositorio.EstadosRepositorio()
   #repositorio.Actualizar(estado)

   #Eliminar
   #estado = Estados.Estados(id, nombre)
   #repositorio = EstadosRepositorio.EstadosRepositorio()
   #repositorio.Eliminar(estado)

   #Consultar
   #estado = Estados.Estados(id, nombre)
   #repositorio = EstadosRepositorio.EstadosRepositorio()
   #repositorio.Consultar(estado)


 # PEDIDOS

   #Inicializacion de datos
   id=1
   codigo='PED004'
   usuario_id=3
   destinatario='Jorge antonio parra'
   direccion_entrega='Avenida 45 #67-89'
   ciudad_id=3
   ruta_id=3
   vehiculo_id=3
   conductor_id=3
   tipo_envio_id=3
   estado_actual=3
   fecha_creacion=datetime(2025, 4, 8, 6, 57)

   #Insertar
   #pedido = Pedido.Pedido( id, codigo, usuario_id, destinatario, direccion_entrega, ciudad_id,ruta_id, vehiculo_id, conductor_id, tipo_envio_id, estado_actual, fecha_creacion)
   #Repositorio = PedidosRepositorio.PedidosRepositorio()
   #Repositorio.Guardar(pedido)

   #Actualizar
   #pedido = Pedido.Pedido( id, codigo, usuario_id, destinatario, direccion_entrega, ciudad_id,ruta_id, vehiculo_id, conductor_id, tipo_envio_id, estado_actual, fecha_creacion)
   #Repositorio = PedidosRepositorio.PedidosRepositorio()
   #Repositorio.Actualizar(pedido)

   #Eliminar
   #pedido = Pedido.Pedido( id, codigo, usuario_id, destinatario, direccion_entrega, ciudad_id,ruta_id, vehiculo_id, conductor_id, tipo_envio_id, estado_actual, fecha_creacion)
   #Repositorio = PedidosRepositorio.PedidosRepositorio()
   #Repositorio.Eliminar(pedido)

   #Consultar
   #pedido = Pedido.Pedido( id, codigo, usuario_id, destinatario, direccion_entrega, ciudad_id,ruta_id, vehiculo_id, conductor_id, tipo_envio_id, estado_actual, fecha_creacion)
   #Repositorio = PedidosRepositorio.PedidosRepositorio()
   #Repositorio.Consultar(pedido)


#Rutas
   #Inicializacion de datos
   id=4
   ciudad_origen_id=2
   ciudad_destino_id=3
   zona_id=2

   #Insertar
   #ruta = Rutas.Ruta(id, ciudad_origen_id, ciudad_destino_id, zona_id)
   #Repositorio = RutasRepositorio.RutasRepositorio()
   #Repositorio.Guardar(ruta)

   #Actualizar
   #ruta = Rutas.Ruta(id, ciudad_origen_id, ciudad_destino_id, zona_id)
   #Repositorio = RutasRepositorio.RutasRepositorio()
   #Repositorio.Actualizar(ruta)

   #Eliminar
   #ruta = Rutas.Ruta(id, ciudad_origen_id, ciudad_destino_id, zona_id)
   #Repositorio = RutasRepositorio.RutasRepositorio()
   #Repositorio.Eliminar(ruta)
   
   #Consultar
   #ruta = Rutas.Ruta(id, ciudad_origen_id, ciudad_destino_id, zona_id)
   #Repositorio = RutasRepositorio.RutasRepositorio()
   #Repositorio.Consultar(ruta)
 
#Zonas

   #Inicializacion de datos
   id=4
   nombre='Cafeteras'

   #Insertar
   #zona = Zonas.Zona(id, nombre)
   #Repositorio = ZonasRepositorio.ZonasRepositorio()
   #Repositorio.Guardar(zona)

   #Actualizar
   #zona = Zonas.Zona(id, nombre)
   #Repositorio = ZonasRepositorio.ZonasRepositorio()
   #Repositorio.Actualizar(zona)

   #Eliminar
   #zona = Zonas.Zona(id, nombre)
   #Repositorio = ZonasRepositorio.ZonasRepositorio()
   #Repositorio.Eliminar(zona)
   
   #Consultar
   #zona = Zonas.Zona(id, nombre)
   #Repositorio = ZonasRepositorio.ZonasRepositorio()
   #Repositorio.Consultar(zona)
  
 
#Departamento

   #Inicializacion de datos
   id=4
   nombre='Amazonas'

   #Insertar
   #departamento = Departamento.Departamento(id, nombre)
   #Repositorio = DepartamentoRepositorio.DepartamentosRepositorio()
   #Repositorio.Guardar(departamento)

   #Actualizar
   #departamento = Departamento.Departamento(id, nombre)
   #Repositorio = DepartamentoRepositorio.DepartamentosRepositorio()
   #Repositorio.Actualizar(departamento)

   #Eliminar
   #departamento = Departamento.Departamento(id, nombre)
   #Repositorio = DepartamentoRepositorio.DepartamentosRepositorio()
   #Repositorio.Eliminar(departamento)

   #Consultar
   #departamento = Departamento.Departamento(id, nombre)
   #Repositorio = DepartamentoRepositorio.DepartamentosRepositorio()
   #Repositorio.Consultar(departamento)
  
# Decorador para proteger los endpoints que necesitan autenticación
def token_requerido(f):
    @wraps(f)  # Aseguramos que la función mantenga su nombre original
    def decorador(*args, **kwargs):
        token = None  # Inicializamos la variable token con None

        # Revisamos si en las cabeceras de la solicitud hay un token
        if 'Authorization' in request.headers:
            # Extraemos el token, que está en el formato 'Bearer <token>'
            token = request.headers['Authorization'].split(" ")[1]  # Tomamos la parte después de "Bearer"
        
        if not token:  # Si no hay token, devolvemos un error
            return jsonify({'mensaje': 'Token faltante'}), 401
        
        try:
            # Verificamos si el token es válido
            JWT.verificar_token(token)
        except Exception as e:
            # Si el token es inválido o expiró, retornamos un error
            return jsonify({'mensaje': str(e)}), 401
        
        # Si el token es válido, ejecutamos la función original
        return f(*args, **kwargs)
    
    return decorador  # Retornamos el decorador

app = Flask(__name__)

@app.route('/loginJWT', methods=['POST'])  # Definimos la ruta para el loginJWT
def login():
    data = request.get_json()  # Obtenemos los datos enviados en el cuerpo de la solicitud (login)
    
    # Extraemos el usuario y la contraseña del cuerpo de la solicitud
    usuario = data.get("usuario")
    password = data.get("password")

    # Verificamos las credenciales (en este caso, las credenciales están codificadas, en un caso real deberíamos validarlas con una base de datos)
    if usuario == "admin" and password == "admin123":
        # Si las credenciales son correctas, generamos el token
        token = JWT.generar_token(usuario)
        return jsonify({"token": token})  # Retornamos el token al usuario
    else:
        # Si las credenciales son incorrectas, retornamos un error
        return jsonify({"mensaje": "Credenciales incorrectas"}), 401


#API CONDUCTOR

@app.route('/conductor/guardar', methods=["POST"])
@token_requerido
def GuardarConductor():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if not all(dato in datos for dato in ("id", "nombre", "cedula", "telefono")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto conductor
        conductor = Conductores.Conductores(datos["id"],datos["nombre"],datos["cedula"],datos["telefono"])

        #Creo el objeto para encriptar y desencriptar
        ObjAES=EncriptarAES.EncriptarAES()

        #Creo objeto para conductor
        repositorio = ConductoresRepositorio.ConductoresRepositorio()

        #Encripto los datos sensibles del conductor
        conductor.setCedula(ObjAES.Cifrar(conductor.getCedula()))
        conductor.setTelefono(ObjAES.Cifrar(conductor.getTelefono()))

        # Guardar en la base de datos usando el repositorio
        repositorio.Guardar(conductor)

        respuesta["Mensaje"] = "Conductor guardado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
@app.route('/conductor/actualizar', methods=["POST"])
@token_requerido
def ActualizarConductor():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if not all(dato in datos for dato in ("id","nombre", "cedula", "telefono")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto conductor
        conductor = Conductores.Conductores(datos["id"],datos["nombre"],datos["cedula"],datos["telefono"])

        #Creo el objeto para encriptar y desencriptar
        ObjAES=EncriptarAES.EncriptarAES()

        #Creo objeto para conductor
        repositorio = ConductoresRepositorio.ConductoresRepositorio()

        #Encripto los datos sensibles del conductor
        conductor.setCedula(ObjAES.Cifrar(conductor.getCedula()))
        conductor.setTelefono(ObjAES.Cifrar(conductor.getTelefono()))

        # Actualizar en la base de datos usando el repositorio
        repositorio.Actualizar(conductor)

        respuesta["Mensaje"] = "Conductor Actualizado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
@app.route('/conductor/consultar', methods=["POST"])
@token_requerido
def ConsultarConductor():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto conductor
        conductor = Conductores.Conductores(datos["id"],"","","")

        #Creo objeto para insertar conductor
        repositorio = ConductoresRepositorio.ConductoresRepositorio()

        # Consultar en la base de datos usando el repositorio
        repositorio.Consultar(conductor)

        respuesta["Mensaje"] = "Conductor Consultado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
@app.route('/conductor/eliminar', methods=["POST"])
@token_requerido
def EliminarConductor():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto conductor
        conductor = Conductores.Conductores(datos["id"],"","","")

        #Creo objeto para insertar conductor
        repositorio = ConductoresRepositorio.ConductoresRepositorio()

        # Consultar en la base de datos usando el repositorio
        repositorio.Eliminar(conductor)

        respuesta["Mensaje"] = "Conductor Eliminado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500

#API VEHICULO

@app.route('/vehiculo/guardar', methods=["POST"])
#@token_requerido
def GuardarVehiculo():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if not all(dato in datos for dato in ("id", "placa", "tipo", "capacidad")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto vehiculo
        vehiculo = Vehiculos.Vehiculos(datos["id"],datos["placa"],datos["tipo"],datos["capacidad"])

        #Creo el objeto para encriptar y desencriptar
        ObjAES=EncriptarAES.EncriptarAES()

        #Creo objeto para vehiculo
        repositorio = VehiculosRepositorio.VehiculosRepositorio()

        #Encripto los datos sensibles del vehiculo
        vehiculo.setPlaca(ObjAES.Cifrar(vehiculo.getPlaca()))

        # Guardar en la base de datos usando el repositorio
        repositorio.Guardar(vehiculo)

        respuesta["Mensaje"] = "Vehiculo guardado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
@app.route('/vehiculo/actualizar', methods=["POST"])
#@token_requerido
def ActualizarVehiculo():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el update
        if not all(dato in datos for dato in ("id", "placa", "tipo", "capacidad")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400
        
        # Crear objeto vehiculo
        vehiculo = Vehiculos.Vehiculos(datos["id"],datos["placa"],datos["tipo"],datos["capacidad"])

        #Creo el objeto para encriptar y desencriptar
        ObjAES=EncriptarAES.EncriptarAES()

        #Creo objeto para vehiculo
        repositorio = VehiculosRepositorio.VehiculosRepositorio()

        #Encripto los datos sensibles del vehiculo
        vehiculo.setPlaca(ObjAES.Cifrar(vehiculo.getPlaca()))

        # Guardar en la base de datos usando el repositorio
        repositorio.Actualizar(vehiculo)

        respuesta["Mensaje"] = "Vehiculo Actualizado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500

@app.route('/vehiculo/consultar', methods=["POST"])
@token_requerido
def ConsultarVehiculo():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar la consulta
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto vehiculo
        vehiculo = Vehiculos.Vehiculos(datos["id"],"","",0)

        #Creo objeto para consultar vehiculo
        repositorio = VehiculosRepositorio.VehiculosRepositorio()

        # Consultar en la base de datos usando el repositorio
        repositorio.Consultar(vehiculo)

        respuesta["Mensaje"] = "Vehiculo Consultado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500

@app.route('/vehiculo/eliminar', methods=["POST"])
@token_requerido
def EliminarVehiculo():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el delete
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto vehiculo
        vehiculo = Vehiculos.Vehiculos(datos["id"],"","",0)

        #Creo objeto para consultar vehiculo
        repositorio = VehiculosRepositorio.VehiculosRepositorio()

        # Consultar en la base de datos usando el repositorio
        repositorio.Eliminar(vehiculo)

        respuesta["Mensaje"] = "Vehiculo Eliminado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500

#API TIPO ENVIO

@app.route('/tipoenvio/guardar', methods=["POST"])
#@token_requerido
def GuardarTipoEnvio():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if not all(dato in datos for dato in ("id", "nombre")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto tipo envio
        tipoEnvio = Tipo_Envio.Tipo_Envio(datos["id"],datos["nombre"])

        #Creo objeto repositorio para tipo envio
        repositorio =  TipoEnvioRepositorio.TipoEnvioRepositorio()

        # Guardar en la base de datos usando el repositorio
        repositorio.Guardar(tipoEnvio)

        respuesta["Mensaje"] = "Tipo Envio guardado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500

@app.route('/tipoenvio/actualizar', methods=["POST"])
#@token_requerido
def ActualizarTipoEnvio():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar la actualizacion
        if not all(dato in datos for dato in ("id", "nombre")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto tipo envio
        tipoEnvio = Tipo_Envio.Tipo_Envio(datos["id"],datos["nombre"])

        #Creo objeto para tipo envio
        repositorio =  TipoEnvioRepositorio.TipoEnvioRepositorio()

        # Guardar en la base de datos usando el repositorio
        repositorio.Actualizar(tipoEnvio)

        respuesta["Mensaje"] = "Tipo Envio Actualizado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
@app.route('/tipoenvio/consultar', methods=["POST"])
#@token_requerido
def ConsultarTipoEnvio():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar la consulta
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto tipo envio
        tipoEnvio = Tipo_Envio.Tipo_Envio(datos["id"]," ")

        #Creo objeto para tipo envio
        repositorio =  TipoEnvioRepositorio.TipoEnvioRepositorio()

        # Guardar en la base de datos usando el repositorio
        repositorio.Consultar(tipoEnvio)

        respuesta["Mensaje"] = "Tipo Envio consultado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
@app.route('/tipoenvio/eliminar', methods=["POST"])
#@token_requerido
def EliminarTipoEnvio():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el eleminar
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto tipo envio
        tipoEnvio = Tipo_Envio.Tipo_Envio(datos["id"]," ")

        #Creo objeto para tipo envio
        repositorio =  TipoEnvioRepositorio.TipoEnvioRepositorio()

        # Guardar en la base de datos usando el repositorio
        repositorio.Eliminar(tipoEnvio)

        respuesta["Mensaje"] = "Tipo Envio eliminado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500

#API INCIDENCIAS

@app.route('/incidencia/guardar', methods=["POST"])
#@token_requerido
def GuardarIncidencia():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if not all(dato in datos for dato in ("id","pedido_id","descripcion","fecha","resuelta")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto tipo incidencia
        incidencia = Incidencias.Incidencias(datos["id"],datos["pedido_id"],datos["descripcion"],datos["fecha"],datos["resuelta"])

        #Creo objeto para tipo incidencia
        repositorio =  IncidenciasRepositorio.IncidenciasRepositorio()

        # Guardar en la base de datos usando el repositorio
        repositorio.Guardar(incidencia)

        respuesta["Mensaje"] = "Incidencia guardado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
@app.route('/incidencia/actualizar', methods=["POST"])
#@token_requerido
def ActualizarIncidencia():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if not all(dato in datos for dato in ("id","pedido_id","descripcion","fecha","resuelta")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto tipo incidencia
        incidencia = Incidencias.Incidencias(datos["id"],datos["pedido_id"],datos["descripcion"],datos["fecha"],datos["resuelta"])

        #Creo objeto para tipo incidencia
        repositorio =  IncidenciasRepositorio.IncidenciasRepositorio()

        # Guardar en la base de datos usando el repositorio
        repositorio.Actualizar(incidencia)

        respuesta["Mensaje"] = "Incidencia actualizada correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
@app.route('/incidencia/consultar', methods=["POST"])
#@token_requerido
def ConsultarIncidencia():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto tipo incidencia
        incidencia = Incidencias.Incidencias(datos["id"],0,"","0001-01-01T00:00:00",0)

        #Creo objeto para tipo incidencia
        repositorio =  IncidenciasRepositorio.IncidenciasRepositorio()

        # Guardar en la base de datos usando el repositorio
        repositorio.Consultar(incidencia)

        respuesta["Mensaje"] = "Incidencia consultada correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500

@app.route('/incidencia/eliminar', methods=["POST"])
#@token_requerido
def EliminarIncidencia():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto tipo incidencia
        incidencia = Incidencias.Incidencias(datos["id"],0,"","0001-01-01T00:00:00",0)

        #Creo objeto para tipo incidencia
        repositorio =  IncidenciasRepositorio.IncidenciasRepositorio()

        # Guardar en la base de datos usando el repositorio
        repositorio.Eliminar(incidencia)

        respuesta["Mensaje"] = "Incidencia eliminada correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500

#API USUARIOS


#API METODOS PAGO

@app.route('/metodos_pago/guardar', methods=["POST"])
#@token_requerido
def GuardarMetodosPago():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if not all(dato in datos for dato in ("id", "nombre")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400
        
        # Crear objeto tipo metodos pago
        metodopago = MetodosPago.MetodosPago(datos["id"],datos["nombre"])

        #Creo objeto para tipo metodos pago
        repositorio =  MetodosPagoRepositorio.MetodosPagoRepositorio()

        # Guardar en la base de datos usando el repositorio
        repositorio.Guardar(metodopago)

        respuesta["Mensaje"] = "Metodo de pago guardado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
@app.route('/metodos_pago/actualizar', methods=["POST"])
#@token_requerido
def ActualizarMetodosPago():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el actualizar
        if not all(dato in datos for dato in ("id","nombre")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto metodos pago
        metodopago = MetodosPago.MetodosPago(datos["id"],datos["nombre"])     

        #Creo objeto para metodos pago
        repositorio =  MetodosPagoRepositorio.MetodosPagoRepositorio()

        #Actualizar en la base de datos usando el repositorio
        repositorio.Actualizar(metodopago)

        respuesta["Mensaje"] = "Metodos Pago actualizado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
@app.route('/metodos_pago/consultar', methods=["POST"])
#@token_requerido
def ConsultarMetodosPago():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el actualizar
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto tipo metodo pago
        metodopago = MetodosPago.MetodosPago(datos["id"],"")     


        #Creo objeto para metodo pago
        repositorio =  MetodosPagoRepositorio.MetodosPagoRepositorio()

        #Consultar en la base de datos usando el repositorio
        repositorio.Consultar(metodopago)

        respuesta["Mensaje"] = "metodo de pago consultado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
    
@app.route('/metodos_pago/eliminar', methods=["POST"])
#@token_requerido
def EliminarMetodosPago():
    
    respuesta = {}    
    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el eleminar
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto tipo envio
        metodopago = MetodosPago.MetodosPago(datos["id"]," ")

        #Creo objeto para tipo envio
        repositorio =  MetodosPagoRepositorio.MetodosPagoRepositorio()

        #Eliminar en la base de datos usando el repositorio
        repositorio.Eliminar(metodopago)

        respuesta["Mensaje"] = "Metodo Pago eliminado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500

#API CIUDADES

@app.route('/ciudades/guardar', methods=["POST"])
#@token_requerido
def GuardarCiudades():
    
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if not all(dato in datos for dato in ("id", "nombre","departamento_id")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400
        
        # Crear objeto tipo ciudad
        ciudad = Ciudades.Ciudades(datos["id"], datos["nombre"], datos["departamento_id"])

        #Creo objeto repositorio para ciudad
        repositorio =  CiudadesRepositorio.CiudadesRepositorio()

        #Guardar en la base de datos usando el repositorio
        repositorio.Guardar(ciudad)

        respuesta["Mensaje"] = "Ciudad guardada correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
@app.route('/ciudades/actualizar', methods=["POST"])
#@token_requerido
def ActualizarCiudades():
    respuesta = {}
    try:
        datos = request.get_json()

        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if not all(dato in datos for dato in ("id", "nombre", "departamento_id")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400
        
        # Crear objeto tipo ciudad
        ciudad = Ciudades.Ciudades(datos["id"], datos["nombre"], datos["departamento_id"])

        #Creo objeto repositorio para ciudad
        repositorio = CiudadesRepositorio.CiudadesRepositorio()

        #Actualizar en la base de datos usando el repositorio
        repositorio.Actualizar(ciudad)

        respuesta["Mensaje"] = "Ciudad actualizada correctamente"
        return jsonify(respuesta), 201
    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
@app.route('/ciudades/consultar', methods=["POST"])
#@token_requerido
def ConsultarCiudades():
    respuesta = {}
    try:
        datos = request.get_json()
    
    # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400
        
        # Crear objeto tipo ciudad
        ciudad = Ciudades.Ciudades(datos["id"], "", 0)

        #Creo objeto repositorio para ciudad
        repositorio = CiudadesRepositorio.CiudadesRepositorio()
        
        #Consultar en la base de datos usando el repositorio
        repositorio.Consultar(ciudad)

        respuesta["Mensaje"] = "Ciudad consultada correctamente"
        return jsonify(respuesta), 201
    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500

@app.route('/ciudades/eliminar', methods=["POST"])
#@token_requerido
def EliminarCiudades():
    respuesta = {}
    try:
        datos = request.get_json()
        
        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400
        
        # Crear objeto tipo ciudad
        ciudad = Ciudades.Ciudades(datos["id"], "", 0)
        
        #Creo objeto repositorio para ciudad
        repositorio = CiudadesRepositorio.CiudadesRepositorio()

        #Eliminar en la base de datos usando el repositorio
        repositorio.Eliminar(ciudad)

        respuesta["Mensaje"] = "Ciudad eliminada correctamente"
        return jsonify(respuesta), 201
    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
#API ESTADOS
@app.route('/estados/guardar', methods=["POST"])
#@token_requerido
def GuardarEstados():
    respuesta = {}
    try:
        datos = request.get_json()
        
        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if not all(dato in datos for dato in ("id", "nombre")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400
        
        # Crear objeto tipo ciudad
        estado = Estados.Estados(datos["id"], datos["nombre"])
        
        #Creo objeto repositorio para ciudad
        repositorio = EstadosRepositorio.EstadosRepositorio()

        #Guardar en la base de datos usando el repositorio
        repositorio.Guardar(estado)

        respuesta["Mensaje"] = "Estado guardado correctamente"
        return jsonify(respuesta), 201
    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
@app.route('/estados/actualizar', methods=["POST"])
#@token_requerido
def ActualizarEstados():
    respuesta = {}
    try:
        datos = request.get_json()
        
        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if not all(dato in datos for dato in ("id", "nombre")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400
        
        #Crear objeto tipo ciudad
        estado = Estados.Estados(datos["id"], datos["nombre"])
        
        #Creo objeto repositorio para ciudad
        repositorio = EstadosRepositorio.EstadosRepositorio()

        #Actualizar en la base de datos usando el repositorio
        repositorio.Actualizar(estado)

        respuesta["Mensaje"] = "Estado actualizado correctamente"
        return jsonify(respuesta), 201
    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500

@app.route('/estados/eliminar', methods=["POST"])
#@token_requerido
def EliminarEstados():
    respuesta = {}
    try:
        datos = request.get_json()
        # Validaciones básicas para saber si estan todos los datos para realizar el insert
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400
        
        #Crear objeto tipo ciudad
        estado = Estados.Estados(datos["id"], "")

        #Creo objeto repositorio para ciudad
        repositorio = EstadosRepositorio.EstadosRepositorio()

        #Eliminar en la base de datos usando el repositorio
        repositorio.Eliminar(estado)

        respuesta["Mensaje"] = "Estado eliminado correctamente"
        return jsonify(respuesta), 201
    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
@app.route('/estados/consultar', methods=["POST"])
# @token_requerido  
def ConsultarEstados():
    respuesta = {}
    try:
        datos = request.get_json()

        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto Estado con solo el ID
        estado = Estados.Estados(datos["id"], "")

        # Crear repositorio
        repositorio = EstadosRepositorio.EstadosRepositorio()

        # Consultar estado
        resultado = repositorio.Consultar(estado)

        if not resultado:
            return jsonify({"Mensaje": "No se encontró el estado"}), 404

        respuesta["Mensaje"] = "Consulta realizada correctamente"
        return jsonify(respuesta), 200

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500

#API PAGOS
@app.route('/pagos/guardar', methods=["POST"])
@token_requerido
def GuardarPago():
    respuesta = {}

    try:
        datos = request.get_json()

        # Validaciones básicas
        if not all(dato in datos for dato in ("id", "pedido_id", "metodo_pago_id", "valor", "fecha_pago", "estado_pago")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto de tipo datetime
        fecha_pago = datetime.strptime(datos["fecha_pago"], "%Y-%m-%d %H:%M:%S")

        # Crear objeto pago
        pago = Pagos.Pagos(
            datos["id"],
            datos["pedido_id"],
            datos["metodo_pago_id"],
            datos["valor"],
            fecha_pago,
            datos["estado_pago"]
        )
        #Creo el objeto para encriptar y desencriptar
        ObjAES=EncriptarAES.EncriptarAES()

        # Usar repositorio
        repositorio = PagosRepositorio.PagosRepositorio()

        #Encripto los datos sensibles de pago
        pago.setValor(ObjAES.Cifrar(pago.getValor()))

        
        # Guardar en la base de datos usando el repositorio
        repositorio.Guardar(pago)
        respuesta["Mensaje"] = "Pago guardado correctamente"
        return jsonify(respuesta), 201
        
    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500
    
@app.route('/pagos/actualizar', methods=["POST"])
@token_requerido
def ActualizarPago():
    try:
        datos = request.get_json()
        if not all(k in datos for k in ("id", "pedido_id", "metodo_pago_id", "valor", "fecha_pago", "estado_pago")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        fecha_pago = datetime.strptime(datos["fecha_pago"], "%Y-%m-%d %H:%M:%S")
        pago = Pagos.Pagos(datos["id"], datos["pedido_id"], datos["metodo_pago_id"], datos["valor"], fecha_pago, datos["estado_pago"])

        # Encriptar valor antes de actualizar
        ObjAES = EncriptarAES.EncriptarAES()
        pago.setValor(ObjAES.Cifrar(pago.getValor()))

        repositorio = PagosRepositorio.PagosRepositorio()
        exito = repositorio.Actualizar(pago)

        if not exito:
            return jsonify({"Error": "Error al actualizar pago"}), 500

        return jsonify({"mensaje": "Pago actualizado correctamente"}), 200

    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    
@app.route('/pagos/consultar', methods=["POST"])
@token_requerido
def ConsultarPago():
    try:
        datos = request.get_json()
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        pago = Pagos.Pagos(datos["id"], 0, 0, "0", datetime.now(), "pendiente")
        repositorio = PagosRepositorio.PagosRepositorio()
        resultado = repositorio.Consultar(pago)

        if not resultado:
            return jsonify({"Error": "Pago no encontrado"}), 404

        fila = resultado[0]
        ObjAES = EncriptarAES.EncriptarAES()

        # Debug: imprime antes y después
        print("Valor encriptado:", fila[3])
        desencriptado = ObjAES.Decifrar(fila[3])
        print("Valor desencriptado:", desencriptado)

        respuesta = {
            "id": fila[0],
            "pedido_id": fila[1],
            "metodo_pago_id": fila[2],
            "valor": desencriptado,
            "fecha_pago": str(fila[4]),
            "estado_pago": fila[5],
            "mensaje": "Pago consultado correctamente"
        }
        return jsonify(respuesta), 200

    except Exception as e:
        return jsonify({"Error": str(e)}), 500



@app.route('/pagos/eliminar', methods=["POST"])
@token_requerido

def EliminarPago():
    respuesta = {}
    try:
        datos = request.get_json()

        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto pago
        pago = Pagos.Pagos(datos["id"], 0, 0,"0", datetime.now(), "pendiente")  

        #Creo objeto repositorio
        repositorio = PagosRepositorio.PagosRepositorio()
        
        # Consultar en la base de datos usando el repositorio
        repositorio.Eliminar(pago)

        respuesta["Mensaje"] = "Pago eliminado correctamente"
        return jsonify(respuesta), 200

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500


# API SEGUIMIENTO

# Ruta para guardar un nuevo seguimiento
@app.route('/seguimiento/guardar', methods=["POST"])
# @token_requerido
def GuardarSeguimiento():
    respuesta = {}
    try:
        datos = request.get_json()

        # Validación de campos obligatorios
        if not all(dato in datos for dato in ("id", "pedido_id", "estado_id", "ubicacion", "comentario")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto de tipo Seguimiento con los datos recibidos
        seguimientos = Seguimiento.Seguimiento(datos["id"], datos["pedido_id"], datos["estado_id"], datos["ubicacion"], datos["comentario"])

        # Crear repositorio y guardar en la base de datos
        repositorio = SeguimientoRepositorio.SeguimientoRepositorio()
        repositorio.Guardar(seguimientos)

        respuesta["Mensaje"] = "Seguimiento guardado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500


# Ruta para actualizar un seguimiento existente
@app.route('/seguimiento/actualizar', methods=["POST"])
# @token_requerido
def ActualizarSeguimiento():
    respuesta = {}
    try:
        datos = request.get_json()

        # Validación de campos obligatorios
        if not all(dato in datos for dato in ("id", "pedido_id", "estado_id", "ubicacion", "comentario")):
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto con los datos actualizados
        seguimiento = Seguimiento.Seguimiento(
            datos["id"],
            datos["pedido_id"],
            datos["estado_id"],
            datos["ubicacion"],
            datos["comentario"]
        )

        # Crear repositorio y actualizar en base de datos
        repositorio = SeguimientoRepositorio.SeguimientoRepositorio()
        repositorio.Actualizar(seguimiento)

        respuesta["Mensaje"] = "Seguimiento actualizado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500


# Ruta para eliminar un seguimiento por ID
@app.route('/seguimiento/eliminar', methods=["POST"])
# @token_requerido
def EliminarSeguimiento():
    respuesta = {}
    try:
        datos = request.get_json()

        # Validar que venga el ID
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

        # Crear objeto seguimiento con solo el ID
        seguimiento = Seguimiento.Seguimiento(datos["id"], 0, 0, "", "")

        # Crear repositorio y eliminar de la base de datos
        repositorio = SeguimientoRepositorio.SeguimientoRepositorio()
        repositorio.Eliminar(seguimiento)

        respuesta["Mensaje"] = "Seguimiento eliminado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500


@app.route("/seguimiento/consultar", methods=["POST"])
# @token_requerido  # Descomenta si estás usando autenticación
def ConsultarSeguimiento():
        
    respuesta = {}

    try:
        datos = request.get_json()
        if "id" not in datos:
            return jsonify({"Error": "Faltan datos obligatorios"}), 400

     # Crear objeto seguimiento
        seguimientos = Seguimiento.Seguimiento(datos["id"],0,0,"","")     


        #Creo objeto repositorio
        repositorio =  SeguimientoRepositorio.SeguimientoRepositorio()

        #Consultar en la base de datos usando el repositorio
        repositorio.Consultar(seguimientos)

        respuesta["Mensaje"] = "seguimiento consultado correctamente"
        return jsonify(respuesta), 201

    except Exception as e:
        respuesta["Error"] = str(e)
        return jsonify(respuesta), 500   
      


#Llamado metodo Main
if __name__ == "__main__":#
    app.run('localhost', 4041);