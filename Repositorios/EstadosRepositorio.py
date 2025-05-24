# Importar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate
from Entidades.Estados import Estados

# Cada entidad es una clase
class EstadosRepositorio:

    # Insertar Estado
    def Guardar(self, estado: Estados):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL InsertarEstado({estado.getId()}, '{estado.getNombre()}');"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Dato Insertado")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    # Actualizar Estado
    def Actualizar(self, estado: Estados):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL ActualizarEstado({estado.getId()}, '{estado.getNombre()}');"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Dato Actualizado")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    # Eliminar Estado
    def Eliminar(self, estado: Estados):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL EliminarEstadoPorId({estado.getId()});"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Dato Eliminado")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    # Consultar Estado por ID
    def Consultar(self, estado: Estados):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL ConsultarEstadoPorId({estado.getId()});"
            tabla = ObjConexion.ejecutarQuery(consulta)

            if not tabla:
                print("No se encontró estado")
                ObjConexion.desconectar()
                return False

            print("Dato Consultado")
            print(tabulate(tabla, headers=["id", "nombre"], tablefmt="grid"))
            ObjConexion.desconectar()
            return True
        except Exception as ex:
            print(str(ex))
            return False
