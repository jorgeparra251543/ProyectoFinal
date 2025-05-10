#Improtar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

#Cada entidad es una clase
class VehiculosRepositorio:

    #Insertar vehiculo    
    def Guardar(self, vehiculo):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""INSERT INTO vehiculos (id,tipo,placa,capacidad) VALUES ({vehiculo.getId()},'{vehiculo.getTipo()}','{vehiculo.getPlaca()}','{vehiculo.getCapacidad()}')"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Insertado")
        return True
    
    #Actualizar vehiculo   
    def Actualizar(self, vehiculo):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""UPDATE vehiculos SET placa='{vehiculo.getPlaca()}',tipo='{vehiculo.getTipo()}',capacidad='{vehiculo.getCapacidad()}' Where id= {vehiculo.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Actualizado")
        return True
    
    #Eliminar vehiculo   
    def Eliminar(self, vehiculo):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""DELETE FROM Vehiculos  WHERE id={vehiculo.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Eliminado")
        return True
    
    #Consultar vehiculo     
    def Consultar(self, vehiculo):

        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""SELECT * FROM Vehiculos  WHERE id={vehiculo.getId()}"""
        tabla=ObjConexion.ejecutarQuery(consulta)
        print("Dato Consultado")
        print(tabulate(tabla, headers=["ID","Placa","Tipo","Capacidad",], tablefmt="grid"))
        ObjConexion.desconectar()
        return True