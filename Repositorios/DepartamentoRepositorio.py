from Nucleo import Conexion
from tabulate import tabulate

class DepartamentosRepositorio:

    def Guardar(self, departamento):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""
        INSERT INTO departamentos (id, nombre)
        VALUES ({departamento.getId()}, '{departamento.getNombre()}')
        """
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Departamento Insertado")
        return True

    def Actualizar(self, departamento):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""
        UPDATE departamentos SET nombre = '{departamento.getNombre()}'
        WHERE id = {departamento.getId()}
        """
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Departamento Actualizado")
        return True

    def Eliminar(self, departamento):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"DELETE FROM departamentos WHERE id = {departamento.getId()}"
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Departamento Eliminado")
        return True

    def Consultar(self, departamento):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"SELECT * FROM departamentos WHERE id = {departamento.getId()}"
        tabla = ObjConexion.ejecutarQuery(consulta)
        print("Departamento Consultado")
        print(tabulate(tabla, headers=["ID", "Nombre"], tablefmt="grid"))
        ObjConexion.desconectar()
        return True
