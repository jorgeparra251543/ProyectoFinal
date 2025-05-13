#Improtar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

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
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""UPDATE Conductores SET nombre='{conductor.getNombre()}',cedula='{conductor.getCedula()}',telefono='{conductor.getTelefono()}' Where id= {conductor.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Actualizado")
        return True
    
    #Eliminar conductor     
    def Eliminar(self, conductor):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""DELETE FROM Conductores  WHERE id={conductor.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Eliminado")
        return True
    
    #Consultar conductor     
    def Consultar(self, conductor):

        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""SELECT * FROM Conductores  WHERE id={conductor.getId()}"""
        tabla=ObjConexion.ejecutarQuery(consulta)
        print("Dato Consultado")
        print(tabulate(tabla, headers=["ID","Nombre","Cedula","Telefono",], tablefmt="grid"))
        ObjConexion.desconectar()
        return True
    