#Improtar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

#Cada entidad es una clase
class IncidenciasRepositorio:

    #Insertar inicidencia
    def Guardar(self, incidencia):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""INSERT INTO Incidencias (id,pedido_id,descripcion,fecha,resuelta) VALUES ({incidencia.getId()},'{incidencia.getPedido()}','{incidencia.getDescripcion()}','{incidencia.getFecha()}','{incidencia.getResuelta()}')"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Insertado")
        return True
    
    #Actualizar incidencia
    def Actualizar(self, incidencia):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""UPDATE Incidencias SET pedido_id='{incidencia.getPedido()}',descripcion='{incidencia.getDescripcion()}',fecha='{incidencia.getFecha()}',resuelta='{incidencia.getResuelta()}' Where id= {incidencia.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Actualizado")
        return True
    
    #Eliminar incidenci    
    def Eliminar(self, incidencia):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""DELETE FROM Incidencias WHERE id={incidencia.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Eliminado")
        return True
    
    #Consultar incicencias     
    def Consultar(self, incidencias):

        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""SELECT * FROM Incidencias  WHERE id={incidencias.getId()}"""
        tabla=ObjConexion.ejecutarQuery(consulta)
        print("Dato Consultado")
        print(tabulate(tabla, headers=["ID","Pedido Id","Descripcion","Fecha","Resuelta"], tablefmt="grid"))
        ObjConexion.desconectar()
        return True