# Importar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate
from Entidades.Seguimiento import Seguimiento

# Cada entidad es una clase
class SeguimientoRepositorio:

    # Insertar Seguimiento
    def Guardar(self, seguimiento: Seguimiento):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL InsertarSeguimiento({seguimiento.getIdPedido()}, {seguimiento.getEstadoId()},'{seguimiento.getUbicacion()}', '{seguimiento.getComentario()}');"

            print("Consulta SQL:", consulta)

            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()

            print("Dato Insertado")
            return True

        except Exception as ex:
            print("Error en Guardar:", str(ex))
            return False



    # Actualizar Seguimiento
    def Actualizar(self, seguimiento: Seguimiento):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"""CALL ActualizarSeguimiento(
                {seguimiento.getId()},
                {seguimiento.getPedidoId()},
                {seguimiento.getEstadoId()},
                '{seguimiento.getUbicacion()}',
                '{seguimiento.getComentario()}',
                '{seguimiento.getFechaHora()}'
            );"""
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Dato Actualizado")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    # Eliminar Seguimiento
    def Eliminar(self, seguimiento: Seguimiento):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL EliminarSeguimientoPorId({seguimiento.getId()});"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Dato Eliminado")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    # Consultar Seguimiento por ID
    def Consultar(self, seguimiento: Seguimiento):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL ConsultarSeguimientoPorId({seguimiento.getId()});"
            tabla = ObjConexion.ejecutarQuery(consulta)     

            if not tabla or len(tabla) == 0:
                print("No se encontró seguimiento")
                return None

            # Suponiendo que la SP devuelve columnas: id, pedido_id, estado_id, ubicacion, comentario, fecha_hora
            elemento = tabla[0]
            resultado = {
                "id": elemento[0],
                "pedido_id": elemento[1],
                "estado_id": elemento[2],
                "ubicacion": elemento[3],
                "comentario": elemento[4],
                "fecha_hora": elemento[5] if len(elemento) > 5 else None
            }

            return resultado

        except Exception as ex:
            print("Error en Consultar:", str(ex))
            return None

        finally:
            try:
                ObjConexion.desconectar()
            except:
                pass
