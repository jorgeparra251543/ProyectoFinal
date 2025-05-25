# Importar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

class RutasRepositorio:

    # Insertar ruta
    def Guardar(self, ruta):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()

            consulta = f"""
            CALL InsertarRuta(
                {ruta.getId()}, {ruta.getCiudadOrigenId()}, {ruta.getCiudadDestinoId()}, {ruta.getZonaId()}
            );
            """
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.commit()
            ObjConexion.desconectar()
            print("Ruta Insertada")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    # Actualizar ruta
    def Actualizar(self, ruta):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()

            consulta = f"""
            CALL ActualizarRuta(
                {ruta.getId()}, {ruta.getCiudadOrigenId()}, {ruta.getCiudadDestinoId()}, {ruta.getZonaId()}
            );
            """
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Ruta Actualizada")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    # Eliminar ruta
    def Eliminar(self, rutaId):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL EliminarRutaPorId({rutaId});"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Ruta Eliminada")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    # Consultar ruta
    def Consultar(self, rutaId):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL ConsultarRutaPorId({rutaId});"
            tabla = ObjConexion.ejecutarQuery(consulta)

            if not tabla:
                print("No se encontró la ruta")
                ObjConexion.desconectar()
                return False

            print("Ruta Consultada")
            print(tabulate(tabla, headers=[
                "ID", "Ciudad Origen ID", "Ciudad Destino ID", "Zona ID"
            ], tablefmt="grid"))

            ObjConexion.desconectar()
            return tabla
        except Exception as ex:
            print(str(ex))
            return False
