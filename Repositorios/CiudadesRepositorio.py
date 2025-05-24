# Importar clases de otras carpetas del proyecto
from Nucleo import Conexion
from Entidades.Ciudades import Ciudades  # Importar la clase

# Cada entidad es una clase
class CiudadesRepositorio:

    # Insertar ciudad
    def Guardar(self, ciudad: Ciudades):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL InsertarCiudad({ciudad.getId()}, '{ciudad.getNombre()}', {ciudad.getDepartamento()});"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Dato Insertado")
            return True
        except Exception as ex:
            print(str(ex))

    # Actualizar ciudad
    def Actualizar(self, ciudad: Ciudades):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL ActualizarCiudad({ciudad.getId()}, '{ciudad.getNombre()}', {ciudad.getDepartamento()});"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Dato Actualizado")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    # Eliminar ciudad
    def Eliminar(self, ciudad: Ciudades):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL EliminarCiudadPorId({ciudad.getId()});"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Dato Eliminado")
            return True
        except Exception as ex:
            print(str(ex))

    # Consultar ciudad por ID
    def Consultar(self, ciudad: Ciudades):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL ConsultarCiudadPorId({ciudad.getId()});"
            tabla = ObjConexion.ejecutarQuery(consulta)

            if not tabla:
                print("No se encontró ciudad")
                ObjConexion.desconectar()
                return False

            for elemento in tabla:
                id = elemento[0]
                nombre = elemento[1]
                departamento_id = elemento[2]
                print(f"ID: {id}, Nombre: {nombre}, Departamento ID: {departamento_id}")
            
            ObjConexion.desconectar()
            return True
        except Exception as ex:
            print(str(ex))
