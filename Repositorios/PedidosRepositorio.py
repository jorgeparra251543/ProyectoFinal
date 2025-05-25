# Importar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

# Cada entidad es una clase
class PedidosRepositorio:

    # Insertar pedido
    def Guardar(self, pedido):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()

            fecha_str = pedido.getFechaCreacion().strftime("%Y-%m-%d %H:%M:%S")

            consulta = f"""
            CALL InsertarPedido(
                {pedido.getId()}, '{pedido.getCodigo()}', {pedido.getUsuarioId()},
                '{pedido.getDestinatario()}', '{pedido.getDireccionEntrega()}',
                {pedido.getCiudadId()}, {pedido.getRutaId()}, {pedido.getVehiculoId()},
                {pedido.getConductorId()}, {pedido.getTipoEnvioId()},
                {pedido.getEstadoActual()}, '{fecha_str}'
            );
            """

            ObjConexion.ejecutarNoQuery(consulta)

            # Asegurarse que haya commit, si no está en ejecutarNoQuery
            ObjConexion.commit()

            ObjConexion.desconectar()
            print("Pedido Insertado")
            return True

        except Exception as ex:
            print(str(ex))
            return False


    # Actualizar pedido
    def Actualizar(self, pedido):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"""
            CALL ActualizarPedido(
                {pedido.getId()}, '{pedido.getCodigo()}', {pedido.getUsuarioId()},
                '{pedido.getDestinatario()}', '{pedido.getDireccionEntrega()}',
                {pedido.getCiudadId()}, {pedido.getRutaId()}, {pedido.getVehiculoId()},
                {pedido.getConductorId()}, {pedido.getTipoEnvioId()},
                {pedido.getEstadoActual()}, '{pedido.getFechaCreacion()}'
            );
            """
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Pedido Actualizado")
            return True
        except Exception as ex:
            print(str(ex))
            return False


    # Eliminar pedido
    def Eliminar(self, pedidoId):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL EliminarPedidoPorId({pedidoId});"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Pedido Eliminado")
            return True
        except Exception as ex:
            print(str(ex))
            return False


    # Consultar pedido
    def Consultar(self, pedidoId):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL ConsultarPedidoPorId({pedidoId});"
            tabla = ObjConexion.ejecutarQuery(consulta)

            if not tabla:
                print("No se encontró el pedido")
                ObjConexion.desconectar()
                return False

            print("Pedido Consultado")
            print(tabulate(tabla, headers=[
                "ID", "Código", "Usuario ID", "Destinatario", "Dirección Entrega",
                "Ciudad ID", "Ruta ID", "Vehículo ID", "Conductor ID",
                "Tipo Envío ID", "Estado Actual", "Fecha Creación"
            ], tablefmt="grid"))

            ObjConexion.desconectar()
            return tabla  
        except Exception as ex:
            print(str(ex))
            return False
