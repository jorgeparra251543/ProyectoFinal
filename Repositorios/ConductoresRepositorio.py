#Improtar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

from Entidades import Conductores;
from Utilidades import EncriptarAES;

#Cada entidad es una clase
class ConductoresRepositorio:

    #Insertar conductor     
    def Guardar(self, conductor):
        try: 
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL InsertarConductor({conductor.getId()}, '{conductor.getNombre()}', '{conductor.getCedula()}', '{conductor.getTelefono()}');"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Dato Insertado")
            return True
        except Exception as ex:
            print(str(ex));
		
    #Actualizar conductor     
    def Actualizar(self, conductor):
        try:
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL ActualizarConductor({conductor.getId()}, '{conductor.getNombre()}', '{conductor.getCedula()}', '{conductor.getTelefono()}');"
           ObjConexion.ejecutarNoQuery(consulta)
           ObjConexion.desconectar()
           print("Dato Actualizado")
           return True
        except Exception as ex:
            print(str(ex));
    
    #Eliminar conductor     
    def Eliminar(self, conductor):
        try:
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL EliminarConductorPorId({conductor.getId()})"
           ObjConexion.ejecutarNoQuery(consulta)
           ObjConexion.desconectar()
           print("Dato Eliminado")
           return True
        except Exception as ex:
            print(str(ex));
    
    def Consultar(self, conductor):
        try:
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL ConsultarConductorPorId({conductor.getId()})"
           tabla = ObjConexion.ejecutarQuery(consulta)

           if not tabla:
               print("No se encontraro conductor")
               ObjConexion.desconectar()

           ObjAES=EncriptarAES.EncriptarAES()

           for elemento in tabla:
               id = elemento[0]
               nombre = elemento[1]
               cedula = ObjAES.Decifrar(elemento[2])  # Desencriptamos la cedula
               telefono = ObjAES.Decifrar(elemento[3])  # Desencriptamos el telefono
               print(f"ID: {id}, Nombre: {nombre}, Cédula: {cedula}, Teléfono: {telefono}")
        
           ObjConexion.desconectar()
           return True
        except Exception as ex:
          print(str(ex))

