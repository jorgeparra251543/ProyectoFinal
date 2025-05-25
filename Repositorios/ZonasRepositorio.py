from Nucleo import Conexion
from tabulate import tabulate

class ZonasRepositorio:

    def Guardar(self, zona):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL InsertarZona({zona.getId()}, '{zona.getNombre()}');"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.commit()
            ObjConexion.desconectar()
            print("Zona Insertada")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    def Actualizar(self, zona):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL ActualizarZona({zona.getId()}, '{zona.getNombre()}');"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Zona Actualizada")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    def Eliminar(self, zonaId):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL EliminarZonaPorId({zonaId});"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Zona Eliminada")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    def Consultar(self, zonaId):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL ConsultarZonaPorId({zonaId});"
            tabla = ObjConexion.ejecutarQuery(consulta)

            if not tabla:
                print("No se encontró la zona")
                ObjConexion.desconectar()
                return False

            print("Zona Consultada")
            print(tabulate(tabla, headers=["ID", "Nombre"], tablefmt="grid"))

            ObjConexion.desconectar()
            return tabla
        except Exception as ex:
            print(str(ex))
            return False
