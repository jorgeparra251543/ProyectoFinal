#Improtar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

from Utilidades import EncriptarAES;

#Cada entidad es una clase
class VehiculosRepositorio:

    #Insertar vehiculo    
    def Guardar(self, vehiculo):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL InsertarVehiculo({vehiculo.getId()},'{vehiculo.getPlaca()}','{vehiculo.getTipo()}','{vehiculo.getCapacidad()}')"""
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Dato Insertado")
            return True
        except Exception as ex:
            print(str(ex));
    
    #Actualizar vehiculo   
    def Actualizar(self, vehiculo):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL ActualizarVehiculo({vehiculo.getId()}, '{vehiculo.getPlaca()}', '{vehiculo.getTipo()}', '{vehiculo.getCapacidad()}');"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Dato Actualizado")
            return True
        except Exception as ex:
            print(str(ex));
    
    #Eliminar vehiculo   
    def Eliminar(self, vehiculo):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL EliminarVehiculoPorId({vehiculo.getId()})"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Dato Eliminado")
            return True
        except Exception as ex:
            print(str(ex));
    
    #Consultar vehiculo     
    def Consultar(self, vehiculo):
        try:
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL ConsultarVehiculoPorId({vehiculo.getId()})"
           tabla=ObjConexion.ejecutarQuery(consulta)

           if not tabla:
               print("No se encontraro vehiculo")
               ObjConexion.desconectar()

           ObjAES=EncriptarAES.EncriptarAES()

           for elemento in tabla:
               id = elemento[0]
               placa = ObjAES.Decifrar(elemento[1])
               tipo = elemento[2] 
               capacidad = elemento[3] 
               print(f"ID: {id}, Placa: {placa}, Tipo: {tipo}, Capacidad: {capacidad}")

           ObjConexion.desconectar()
           return True
        except Exception as ex:
            print(str(ex));