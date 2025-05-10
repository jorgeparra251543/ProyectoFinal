#Improtar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

#Cada entidad es una clase
class TipoEnvioRepositorio:

    #Insertar tipo envio    
    def Guardar(self, envio):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""INSERT INTO tipo_envio (id,nombre) VALUES ({envio.getId()},'{envio.getNombre()}')"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Insertado")
        return True
    
    #Actualizar tipo envio   
    def Actualizar(self, envio):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""UPDATE tipo_envio SET nombre='{envio.getNombre()}' Where id= {envio.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Actualizado")
        return True
    
    #Eliminar tipo envio
    def Eliminar(self, envio):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""DELETE FROM tipo_envio  WHERE id={envio.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Eliminado")
        return True
    
    #Consultar tipo envio 
    def Consultar(self, envio):

        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""SELECT * FROM tipo_envio WHERE id={envio.getId()}"""
        tabla=ObjConexion.ejecutarQuery(consulta)
        print("Dato Consultado")
        print(tabulate(tabla, headers=["ID","Nombre"], tablefmt="grid"))
        ObjConexion.desconectar()
        return True