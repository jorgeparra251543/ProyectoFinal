from datetime import datetime

class Seguimiento:
    def __init__(self, id, idpedido, estadoid, ubicacion, comentario):
        self.setId(id)
        self.setIdPedido(idpedido)
        self.setEstadoId(estadoid)
        self.setUbicacion(ubicacion)
        self.setComentario(comentario)

    def getId(self):
        return self.__id

    def setId(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise ValueError("Id no válido")

    def getIdPedido(self):
        return self.__idpedido

    def setIdPedido(self, idpedido):
        if isinstance(idpedido, int):
            self.__idpedido = idpedido
        else:
            raise ValueError("Id no válido")


    def getEstadoId(self):
        return self.__estadoid

    def setEstadoId(self, estadoid):
        if isinstance(estadoid, int):
            self.__estadoid = estadoid
        else:
            raise ValueError("estado_id no válido")

    def getUbicacion(self):
        return self.__ubicacion

    def setUbicacion(self, ubicacion):
        if isinstance(ubicacion, str):
            self.__ubicacion = ubicacion
        else:
            raise ValueError("ubicación no válida")

    def getComentario(self):
        return self.__comentario

    def setComentario(self, comentario):
        if isinstance(comentario, str):
            self.__comentario = comentario
        else:
            raise ValueError("comentario no válido")
        
