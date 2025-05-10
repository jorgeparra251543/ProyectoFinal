#Importar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

#Cada entidad es una clase
class SeguimientoRepositorio:

    #Insertar Seguimiento
    def Guardar(self, Seguimiento):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""INSERT INTO seguimiento (id,pedido_id,estado_id,ubicacion,comentario,fecha_hora) VALUES ({Seguimiento.getId()},{Seguimiento.getIdPedido()},{Seguimiento.getEstadoId()},'{Seguimiento.getUbicacion()}','{Seguimiento.getComentario()}','{Seguimiento.getFechaHora()}')"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Insertado")
        return True
    
    #Actualizar Seguimiento
    def Actualizar(self, Seguimiento):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""UPDATE seguimiento SET pedido_id={Seguimiento.getIdPedido()},estado_id={Seguimiento.getEstadoId()},ubicacion='{Seguimiento.getUbicacion()}',comentario='{Seguimiento.getComentario()}',fecha_hora='{Seguimiento.getFechaHora()}' Where id= {Seguimiento.getIdPedido()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Actualizado")
        return True
    
    #Eliminar Seguimiento    
    def Eliminar(self, Seguimiento):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""DELETE FROM seguimiento WHERE id={Seguimiento.getIdPedido()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Eliminado")
        return True
    
    #Consultar Seguimiento     
    def Consultar(self, Seguimiento):

        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""SELECT * FROM seguimiento  WHERE id={Seguimiento.getIdPedido()}"""
        tabla=ObjConexion.ejecutarQuery(consulta)
        print("Dato Consultado")
        print(tabulate(tabla, headers=["id","pedido_id","estado_id","ubicacion","comentario","fecha_hora"], tablefmt="grid"))
        ObjConexion.desconectar()
        return True
