# Importar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate
# Cada entidad es una clase
class PedidosRepositorio:

    # Insertar pedido
    def Guardar(self, pedido):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""
        INSERT INTO pedidos (
            id, codigo, usuario_id, destinatario, direccion_entrega, ciudad_id, 
            ruta_id, vehiculo_id, conductor_id, tipo_envio_id, estado_actual, fecha_creacion
        ) VALUES (
            {pedido.getId()},'{pedido.getCodigo()}','{pedido.getUsuarioId()}','{pedido.getDestinatario()}','{pedido.getDireccionEntrega()}',' {pedido.getCiudadId()}','{pedido.getRutaId()}','{pedido.getVehiculoId()}','{pedido.getConductorId()}','{pedido.getTipoEnvioId()}','{pedido.getEstadoActual()}','{pedido.getFechaCreacion()}'
        )
        """
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Pedido Insertado")
        return True
    

    

    # Actualizar pedido
    def Actualizar(self, pedido):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""
        UPDATE pedidos SET 
            codigo = '{pedido.getCodigo()}',
            usuario_id = {pedido.getUsuarioId()},
            destinatario = '{pedido.getDestinatario()}',
            direccion_entrega = '{pedido.getDireccionEntrega()}',
            ciudad_id = {pedido.getCiudadId()},
            ruta_id = {pedido.getRutaId()},
            vehiculo_id = {pedido.getVehiculoId()},
            conductor_id = {pedido.getConductorId()},
            tipo_envio_id = {pedido.getTipoEnvioId()},
            estado_actual = {pedido.getEstadoActual()},
            fecha_creacion = '{pedido.getFechaCreacion()}'
        WHERE id = {pedido.getId()}
        """
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Pedido Actualizado")
        return True

    # Eliminar pedido
    def Eliminar(self, pedido):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"DELETE FROM pedidos WHERE id = {pedido.getId()}"
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Pedido Eliminado")
        return True

    # Consultar pedido
    def Consultar(self, pedido):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"SELECT * FROM pedidos WHERE id = {pedido.getId()}"
        tabla = ObjConexion.ejecutarQuery(consulta)
        print("Pedido Consultado")
        print(tabulate(tabla, headers=[
            "ID", "Código", "Usuario ID", "Destinatario", "Dirección Entrega",
            "Ciudad ID", "Ruta ID", "Vehículo ID", "Conductor ID",
            "Tipo Envío ID", "Estado Actual", "Fecha Creación"
        ], tablefmt="grid"))
        ObjConexion.desconectar()
        return True
