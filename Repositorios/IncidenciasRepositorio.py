#Improtar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

#Cada entidad es una clase
class IncidenciasRepositorio:

    #Insertar inicidencia
    def Guardar(self, incidencia):
        try:
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL InsertarIncidencia({incidencia.getId()},'{incidencia.getPedido()}','{incidencia.getDescripcion()}','{incidencia.getFecha()}','{incidencia.getResuelta()}');"
           ObjConexion.ejecutarNoQuery(consulta)
           ObjConexion.desconectar()
           print("Dato Insertado")
           return True
        except Exception as ex:
            print(str(ex));
    
    #Actualizar incidencia
    def Actualizar(self, incidencia):
        try:
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL ActualizarIncidencia({incidencia.getId()},'{incidencia.getPedido()}','{incidencia.getDescripcion()}','{incidencia.getFecha()}','{incidencia.getResuelta()}');"
           ObjConexion.ejecutarNoQuery(consulta)
           ObjConexion.desconectar()
           print("Dato Actualizado")
           return True
        except Exception as ex:
            print(str(ex));
    
    #Eliminar incidencia    
    def Eliminar(self, incidencia):
        try:
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL EliminarIncidenciPorId({incidencia.getId()});"
           ObjConexion.ejecutarNoQuery(consulta)
           ObjConexion.desconectar()
           print("Dato Eliminado")
           return True
        except Exception as ex:
            print(str(ex));
    
    #Consultar incicencias     
    def Consultar(self, incidencias):
        try:
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL ConsultarIncidenciaPorId({incidencias.getId()});"
           tabla=ObjConexion.ejecutarQuery(consulta)

           if not tabla:
               print("No se encontraro incidencia")
               ObjConexion.desconectar()

           for elemento in tabla:
               id = elemento[0]
               pedidoid = elemento[1]
               descripcion = elemento[2]
               fecha = elemento[3]
               resuelta = elemento[4]
               print(f"ID: {id},PedidoId: {pedidoid} ,Descripcion: {descripcion},Fecha: {fecha},Resuelta: {resuelta}")
           ObjConexion.desconectar()
           return True
        except Exception as ex:
            print(str(ex));