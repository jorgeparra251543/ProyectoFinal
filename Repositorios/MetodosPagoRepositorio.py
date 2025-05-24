#Importar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate
from Entidades.MetodosPago import MetodosPago  # Importar la clase


#Cada entidad es una clase
class MetodosPagoRepositorio:

    #Insertar Metodos Pago
    def Guardar(self, metodo_pago: MetodosPago):
        try: 
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL InsertarMetodoPago('{metodo_pago.getNombre()}');"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Dato Insertado")
            return True
        except Exception as ex:
            print(str(ex));
    
    #Actualizar Metodos Pago
    def Actualizar(self, MetodosPago):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            
            consulta = f"CALL ActualizarMetodoPago( '{MetodosPago.getNombre()}');"
            
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Dato Actualizado")
            return True
        except Exception as ex:
            print(str(ex))
            return False

    
    #Eliminar Metodos Pago    
    def Eliminar(self, MetodosPago):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL EliminarMetodoPagoPorId({MetodosPago.getId()});"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Dato Eliminado")
            return True
        except Exception as ex:
            print(str(ex));
    
    #Consultar Metodos Pago     
    def Consultar(self, MetodosPago):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL ConsultarMetodoPagoPorId({MetodosPago.getId()});"
            tabla=ObjConexion.ejecutarQuery(consulta)     

            if not tabla:
               print("No se encontro conductor")
               ObjConexion.desconectar()

            for elemento in tabla:
               id = elemento[0]
               nombre = elemento[1]
               print(f"ID:{id},nombre: {nombre}")
        
               ObjConexion.desconectar()
               return True
        except Exception as ex:
               print(str(ex))
