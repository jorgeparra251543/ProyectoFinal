from datetime import datetime

#Cada entidad es una clase
class Incidencias:
    
    #Metodo constructor con parametros
    def __init__(self,id,pedido,descripcion,fecha,resuelta):
        self.setId(id)
        self.setPedido(pedido)
        self.setDescripcion(descripcion)
        self.setFecha(fecha)
        self.setResuelta(resuelta)

    #Metodos Get y Set para acceder a los atributos

    def getId(self):
        return self.__id

    def setId(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise ValueError("Id no válido")

    def getPedido(self):
        return self.__pedido

    def setPedido(self, pedido):
        if isinstance(pedido, str) and pedido.strip():
            self.__pedido = pedido
        else:
            raise ValueError("Pedido no válido")
        
    def getDescripcion(self):
        return self.__descripcion

    def setDescripcion(self, descripcion):
        if isinstance(descripcion, str) and descripcion.strip():
            self.__descripcion = descripcion
        else:
            raise ValueError("Descripcion no válido")
        
    def getFecha(self):
        return self.__fecha

    def setFecha(self, fecha):
        if isinstance(fecha,datetime):
            self.__fecha = fecha
        else:
            raise ValueError("Fecha  no válido")

    def getResuelta(self):
        return self.__resuelta

    def setResuelta(self, resuelta):
        if isinstance(resuelta, int):
            self.__resuelta = resuelta
        else:
            raise ValueError("Resuelta no válido")