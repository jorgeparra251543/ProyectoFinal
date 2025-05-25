# Importar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate
from Entidades.Pagos import Pagos  # Asegúrate de que esta clase exista y tenga getters

class PagosRepositorio:

    # Insertar Pago
    def Guardar(self, pago: Pagos):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()

            consulta = f"""
                CALL InsertarPago(
                    {pago.getId()},
                    {pago.getPedidoId()},
                    {pago.getMetodoPagoId()},
                    '{pago.getValor()}',
                    '{pago.getFechaPago()}',
                    '{pago.getEstadoPago()}'
                );
            """

            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Pago insertado correctamente")
            return True
        except Exception as ex:
            print("Error en Guardar:", str(ex))
            return False

    # Actualizar Pago
    def Actualizar(self, pago: Pagos):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()

            fecha_str = pago.getFechaPago().strftime("%Y-%m-%d %H:%M:%S")
            valor_escapado = pago.getValor().replace("'", "''")  # Escapar comillas simples si es necesario

            consulta = f"""
                CALL ActualizarPago(
                    {pago.getId()},
                    {pago.getPedidoId()},
                    {pago.getMetodoPagoId()},
                    '{valor_escapado}',
                    '{fecha_str}',
                    '{pago.getEstadoPago()}'
                );
            """

            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Pago actualizado correctamente")
            return True
        except Exception as ex:
            print("Error en Actualizar:", str(ex))
            return False
    


    # Eliminar Pago
    def Eliminar(self, pago: Pagos):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()

            consulta = f"CALL EliminarPagoPorId({pago.getId()});"
            ObjConexion.ejecutarNoQuery(consulta)
            ObjConexion.desconectar()
            print("Pago eliminado correctamente")
            return True
        except Exception as ex:
            print("Error en Eliminar:", str(ex))
            return False

    # Consultar Pago por ID
    def Consultar(self, pago: Pagos):
        try:
            ObjConexion = Conexion.Conexion()
            ObjConexion.conectar()
            consulta = f"CALL ConsultarPagoPorId({pago.getId()});"
            tabla = ObjConexion.ejecutarQuery(consulta)
            ObjConexion.desconectar()
            if not tabla:
                return None
            return tabla
        except Exception as ex:
            print("Error en Consultar:", str(ex))
            return None