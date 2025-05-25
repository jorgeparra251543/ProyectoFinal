# Importar clases necesarias
from Nucleo import Conexion
from tabulate import tabulate
from Entidades.Seguimiento import Seguimiento

class SeguimientoRepositorio:

    # Guardar nuevo seguimiento
    def Guardar(self, seguimiento: Seguimiento):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL insertar_seguimiento({seguimiento.getId()}, {seguimiento.getIdPedido()}, {seguimiento.getEstadoId()}, '{seguimiento.getUbicacion()}', '{seguimiento.getComentario()}');"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Seguimiento insertado")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    # Actualizar seguimiento existente
    def Actualizar(self, seguimiento: Seguimiento):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL actualizar_seguimiento({seguimiento.getId()}, {seguimiento.getIdPedido()}, {seguimiento.getEstadoId()}, '{seguimiento.getUbicacion()}', '{seguimiento.getComentario()}');"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Seguimiento actualizado")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    # Eliminar seguimiento por ID
    def Eliminar(self, seguimiento: Seguimiento):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL eliminar_seguimiento({seguimiento.getId()});"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Seguimiento eliminado")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    def Consultar(self, seguimiento: Seguimiento):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()

            consulta = f"CALL consultar_seguimiento({seguimiento.getId()});"
            print("Consulta:", consulta)  # Debug opcional

            tabla = ObjConexion.ejecutarQuery(consulta)

            if not tabla:
                print("No se encontró seguimiento")
                ObjConexion.desconectar()

            for elemento in tabla:
               id = elemento[0]
               pedido_id = elemento[1]
               estado_id=elemento[2]
               ubicacion=elemento[3]
               comentario=elemento[4]

               print(f"id:{id}, pedido_id:{pedido_id},estado_id:{estado_id},ubicacion:{ubicacion},comentario:{comentario}")
        
               ObjConexion.desconectar()
               return True
        except Exception as ex:
               print(str(ex))
