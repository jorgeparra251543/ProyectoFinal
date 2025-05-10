#Importar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

#Cada entidad es una clase
class MetodosPagoRepositorio:

    #Insertar Metodos Pago
    def Guardar(self, MetodosPago):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""INSERT INTO metodos_pago(id,nombre) VALUES ({MetodosPago.getId()},'{MetodosPago.getNombre()}')"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Insertado")
        return True
    
    #Actualizar Metodos Pago
    def Actualizar(self, MetodosPago):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""UPDATE metodos_pago SET id='{MetodosPago.getId()}',nombre='{MetodosPago.getNombre()}' WHERE id={MetodosPago.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Actualizado")
        return True
    
    #Eliminar Metodos Pago    
    def Eliminar(self, MetodosPago):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""DELETE FROM metodos_pago WHERE id={MetodosPago.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Eliminado")
        return True
    
    #Consultar Metodos Pago     
    def Consultar(self, MetodosPagos):

        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""SELECT * FROM metodos_pago WHERE id={MetodosPagos.getId()}"""
        tabla=ObjConexion.ejecutarQuery(consulta)
        print("Dato Consultado")
        print(tabulate(tabla, headers=["ID","nombre"], tablefmt="grid"))
        ObjConexion.desconectar()
        return True