#Improtar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

#Cada entidad es una clase
class PagosRepositorio:

    #Insertar pagos
    def Guardar(self, Pagos):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""INSERT INTO pagos (id,pedido_id,metodo_pago_id,valor,fecha_pago,estado_pago) VALUES ({Pagos.getId()},{Pagos.getPedidoId()} ,{Pagos.getMetodoPagoId()} ,'{Pagos.getValor()}','{Pagos.getFechaPago()}','{Pagos.getEstadoPago()}')"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Insertado")
        return True
    
    
    #Actualizar pagos
    def Actualizar(self, Pagos):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""UPDATE pagos SET id={Pagos.getId()} ,pedido_id={Pagos.getPedidoId()},metodo_pago_id={Pagos.getMetodoPagoId()},valor='{Pagos.getValor()}',fecha_pago='{Pagos.getFechaPago()}',estado_pago='{Pagos.getEstadoPago()}' Where id= {Pagos.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Actualizado")
        return True
    
    #Eliminar pagos    
    def Eliminar(self, Pagos):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""DELETE FROM pagos WHERE id={Pagos.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Eliminado")
        return True
    
    #Consultar pagos     
    def Consultar(self, Pagos):

        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""SELECT * FROM pagos WHERE id={Pagos.getId()}"""
        tabla=ObjConexion.ejecutarQuery(consulta)
        print("Dato Consultado")
        print(tabulate(tabla, headers=["id","pedido_id","metodo_pago_id","valor","fecha_pago","estado_pago"], tablefmt="grid"))
        ObjConexion.desconectar()
        return True
    