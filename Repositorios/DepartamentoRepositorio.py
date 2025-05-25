from Nucleo import Conexion
from tabulate import tabulate

class DepartamentosRepositorio:

    def Guardar(self, departamento):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL InsertarDepartamento({departamento.getId()}, '{departamento.getNombre()}');"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.commit()
            ObjConexion.desconectar()
            print("Departamento Insertado")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    def Actualizar(self, departamento):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL ActualizarDepartamento({departamento.getId()}, '{departamento.getNombre()}');"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Departamento Actualizado")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    def Eliminar(self, departamentoId):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL EliminarDepartamentoPorId({departamentoId});"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Departamento Eliminado")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    def Consultar(self, departamentoId):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL ConsultarDepartamentoPorId({departamentoId});"
            tabla = ObjConexion.ejecutarQuery(consulta)

            if not tabla:
                print("No se encontró el departamento")
                ObjConexion.desconectar()
                return False

            print("Departamento Consultado")
            print(tabulate(tabla, headers=["ID", "Nombre"], tablefmt="grid"))

            ObjConexion.desconectar()
            return tabla
        except Exception as ex:
            print(str(ex))
            return False
