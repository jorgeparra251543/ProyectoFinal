from datetime import datetime

#Cada entidad es una clase
class Pagos:
    
    #Metodo constructor con parametros
    def __init__(self,id,pedido_id,metodo_pago_id,valor,fecha_pago,estado_pago):
        self.setId(id)
        self.setPedidoId(pedido_id)
        self.setMetodoPagoId(metodo_pago_id)
        self.setValor(valor)
        self.setFechaPago(fecha_pago)
        self.setEstadoPago(estado_pago)

    #Metodos Get y Set para acceder a los atributos

    def getId(self):
        return self.__id

    def setId(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise ValueError("Id no válido")

    def getPedidoId(self):
        return self.__pedido_id

    def setPedidoId(self, pedido_id):
        if isinstance(pedido_id, int):
            self.__pedido_id = pedido_id
        else:
            raise ValueError("pedidoId no válido")

    def getMetodoPagoId(self):
        return self.__metodo_pago_id

    def setMetodoPagoId(self, metodo_pago_id):
        if isinstance(metodo_pago_id, int):
            self.__metodo_pago_id = metodo_pago_id
        else:
            raise ValueError("metodo_pago_id no válido")

    def getValor(self):
        return self.__valor

    def setValor(self, valor):
        if isinstance(valor, (int, float)):
            self.__valor = valor
        else:
            raise ValueError("Valor no válido")

    def getFechaPago(self):
        return self.__fecha_pago

    def setFechaPago(self, fecha_pago):
        if isinstance(fecha_pago, datetime):
            self.__fecha_pago = fecha_pago
        else:
            raise ValueError("Fecha de pago no válida")

    def getEstadoPago(self):
        return self.__estado_pago

    def setEstadoPago(self, estado_pago):
        if estado_pago in ["pendiente", "pagado", "fallido"]:
            self.__estado_pago = estado_pago
        else:
            raise ValueError("estado_pago de pago no válido")
