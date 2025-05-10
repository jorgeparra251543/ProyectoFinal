#Importar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

#Cada entidad es una clase
class EstadosRepositorio:

    #Insertar Estados
    def Guardar(self, estados):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""INSERT INTO estados (id,nombre) VALUES ({estados.getId()},'{estados.getNombre()}')"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Insertado")
        return True
    
    #Actualizar Estados
    def Actualizar(self, estados):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""UPDATE estados SET nombre='{estados.getNombre()}' Where id= {estados.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Actualizado")
        return True
    
    #Eliminar Estados    
    def Eliminar(self, estados):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""DELETE FROM estados WHERE id={estados.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Eliminado")
        return True
    
    #Consultar Estados     
    def Consultar(self, estados):

        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""SELECT * FROM estados  WHERE id={estados.getId()}"""
        tabla=ObjConexion.ejecutarQuery(consulta)
        print("Dato Consultado")
        print(tabulate(tabla, headers=["id","nombre"], tablefmt="grid"))
        ObjConexion.desconectar()
        return True
