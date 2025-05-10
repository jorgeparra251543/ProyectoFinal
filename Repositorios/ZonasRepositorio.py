from Nucleo import Conexion
from tabulate import tabulate

class ZonasRepositorio:

    def Guardar(self, zona):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""
        INSERT INTO zonas (id, nombre) VALUES ({zona.getId()}, '{zona.getNombre()}')
        """
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Zona Insertada")
        return True

    def Actualizar(self, zona):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""
        UPDATE zonas SET nombre = '{zona.getNombre()}' WHERE id = {zona.getId()}
        """
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Zona Actualizada")
        return True

    def Eliminar(self, zona):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"DELETE FROM zonas WHERE id = {zona.getId()}"
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Zona Eliminada")
        return True

    def Consultar(self, zona):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"SELECT * FROM zonas WHERE id = {zona.getId()}"
        tabla = ObjConexion.ejecutarQuery(consulta)
        print("Zona Consultada")
        print(tabulate(tabla, headers=["ID", "Nombre"], tablefmt="grid"))
        ObjConexion.desconectar()
        return True
