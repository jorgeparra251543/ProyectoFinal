#Importar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

#Cada entidad es una clase
class CiudadesRepositorio:

    #Insertar ciudad
    def Guardar(self, Ciudades):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""INSERT INTO ciudades (id,nombre,departamento_id) VALUES ({Ciudades.getId()},'{Ciudades.getNombre()}',{Ciudades.getDepartamento()})"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Insertado")
        return True
    
    #Actualizar ciudad
    def Actualizar(self, Ciudades):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""UPDATE ciudades SET id={Ciudades.getId()},nombre='{Ciudades.getNombre()}',departamento_id={Ciudades.getDepartamento()} Where id= {Ciudades.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Actualizado")
        return True
    
    #Eliminar ciudad    
    def Eliminar(self, Ciudades):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""DELETE FROM ciudades WHERE id={Ciudades.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Eliminado")
        return True
    
    #Consultar ciudades 
    def Consultar(self, Ciudades):

        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""SELECT * FROM ciudades  WHERE id={Ciudades.getId()}"""
        tabla=ObjConexion.ejecutarQuery(consulta)
        print("Dato Consultado")
        print(tabulate(tabla, headers=["id","nombre","departamento_id"], tablefmt="grid"))
        ObjConexion.desconectar()
        return True
    