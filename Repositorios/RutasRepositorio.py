from Nucleo import Conexion
from tabulate import tabulate

class RutasRepositorio:

    def Guardar(self, ruta):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""
        INSERT INTO rutas (id, ciudad_origen_id, ciudad_destino_id, zona_id)
        VALUES ({ruta.getId()}, {ruta.getCiudadOrigenId()}, {ruta.getCiudadDestinoId()}, {ruta.getZonaId()})
        """
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Ruta Insertada")
        return True

    def Actualizar(self, ruta):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""
        UPDATE rutas SET
            ciudad_origen_id = {ruta.getCiudadOrigenId()},
            ciudad_destino_id = {ruta.getCiudadDestinoId()},
            zona_id = {ruta.getZonaId()}
        WHERE id = {ruta.getId()}
        """
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Ruta Actualizada")
        return True

    def Eliminar(self, ruta):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"DELETE FROM rutas WHERE id = {ruta.getId()}"
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Ruta Eliminada")
        return True

    def Consultar(self, ruta):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"SELECT * FROM rutas WHERE id = {ruta.getId()}"
        tabla = ObjConexion.ejecutarQuery(consulta)
        print("Ruta Consultada")
        print(tabulate(tabla, headers=["ID", "Ciudad Origen ID", "Ciudad Destino ID", "Zona ID"], tablefmt="grid"))
        ObjConexion.desconectar()
        return True
