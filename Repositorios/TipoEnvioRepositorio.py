#Improtar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

#Cada entidad es una clase
class TipoEnvioRepositorio:

    #Insertar tipo envio    
    def Guardar(self, envio):
        try: 
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL InsertarTipoEnvio({envio.getId()},'{envio.getNombre()}');"
           ObjConexion.ejecutarNoQuery(consulta)
           ObjConexion.desconectar()
           print("Dato Insertado")
           return True
        except Exception as ex:
            print(str(ex));
    
    #Actualizar tipo envio   
    def Actualizar(self, envio):
        try:
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL ActualizarTipoEnvio({envio.getId()},'{envio.getNombre()}');"
           ObjConexion.ejecutarNoQuery(consulta)
           ObjConexion.desconectar()
           print("Dato Actualizado")
           return True
        except Exception as ex:
            print(str(ex));
    
    #Eliminar tipo envio
    def Eliminar(self, envio):
        try:
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL EliminarTipoEnvioPorId({envio.getId()});"
           ObjConexion.ejecutarNoQuery(consulta)
           ObjConexion.desconectar()
           print("Dato Eliminado")
           return True
        except Exception as ex:
            print(str(ex));
    
    #Consultar tipo envio 
    def Consultar(self, envio):
        try:
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL ConsultarTipoEnvioPorId({envio.getId()});"
           tabla=ObjConexion.ejecutarQuery(consulta)

           if not tabla:
               print("No se encontraro conductor")
               ObjConexion.desconectar()

           for elemento in tabla:
               id = elemento[0]
               nombre = elemento[1]
               print(f"ID: {id}, Nombre: {nombre}")

           ObjConexion.desconectar()
           return True
        except Exception as ex:
            print(str(ex));