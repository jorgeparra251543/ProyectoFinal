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

from datetime import datetime

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
   id = 1
   nombre = "Tarjeta de debito"

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
   id = 3
   pedido_id = 3
   metodo_pago_id= 3
   valor = 350000.00
   fecha_pago = datetime(2025, 4, 8, 6, 57)
   estado_pago = "pagado"

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
   id = 3
   idpedido = 3
   estadoid = 3
   ubicacion = "Entregado"
   comentario = "Sin inconvenientes"
   fechahora= datetime(2025, 4, 8, 6, 57)

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
  
#Llamado metodo Main
if __name__ == "__main__":#
    main()