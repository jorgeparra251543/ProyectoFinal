from datetime import datetime

class Pedido:
    def __init__(self, id, codigo=None, usuario_id=None, destinatario=None,
                 direccion_entrega=None, ciudad_id=None, ruta_id=None, vehiculo_id=None,
                 conductor_id=None, tipo_envio_id=None, estado_actual=None, fecha_creacion=None):

        self.setId(id)

        if codigo is not None:
            self.setCodigo(codigo)
        if usuario_id is not None:
            self.setUsuarioId(usuario_id)
        if destinatario is not None:
            self.setDestinatario(destinatario)
        if direccion_entrega is not None:
            self.setDireccionEntrega(direccion_entrega)
        if ciudad_id is not None:
            self.setCiudadId(ciudad_id)
        if ruta_id is not None:
            self.setRutaId(ruta_id)
        if vehiculo_id is not None:
            self.setVehiculoId(vehiculo_id)
        if conductor_id is not None:
            self.setConductorId(conductor_id)
        if tipo_envio_id is not None:
            self.setTipoEnvioId(tipo_envio_id)
        if estado_actual is not None:
            self.setEstadoActual(estado_actual)
        if fecha_creacion is not None:
            self.setFechaCreacion(fecha_creacion)

    def setId(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise ValueError("Id no válido")

    def getId(self):
        return self.__id

    def setCodigo(self, codigo):
        if isinstance(codigo, str) and codigo.strip():
            self.__codigo = codigo
        else:
            raise ValueError("Código no válido")

    def getCodigo(self):
        return self.__codigo

    def setUsuarioId(self, usuario_id):
        if isinstance(usuario_id, int):
            self.__usuario_id = usuario_id
        else:
            raise ValueError("Usuario ID no válido")

    def getUsuarioId(self):
        return self.__usuario_id

    def setDestinatario(self, destinatario):
        if isinstance(destinatario, str) and destinatario.strip():
            self.__destinatario = destinatario
        else:
            raise ValueError("Destinatario no válido")

    def getDestinatario(self):
        return self.__destinatario

    def setDireccionEntrega(self, direccion_entrega):
        if isinstance(direccion_entrega, str) and direccion_entrega.strip():
            self.__direccion_entrega = direccion_entrega
        else:
            raise ValueError("Dirección de entrega no válida")

    def getDireccionEntrega(self):
        return self.__direccion_entrega

    def setCiudadId(self, ciudad_id):
        if isinstance(ciudad_id, int):
            self.__ciudad_id = ciudad_id
        else:
            raise ValueError("Ciudad ID no válido")

    def getCiudadId(self):
        return self.__ciudad_id

    def setRutaId(self, ruta_id):
        if isinstance(ruta_id, int):
            self.__ruta_id = ruta_id
        else:
            raise ValueError("Ruta ID no válido")

    def getRutaId(self):
        return self.__ruta_id

    def setVehiculoId(self, vehiculo_id):
        if isinstance(vehiculo_id, int):
            self.__vehiculo_id = vehiculo_id
        else:
            raise ValueError("Vehículo ID no válido")

    def getVehiculoId(self):
        return self.__vehiculo_id

    def setConductorId(self, conductor_id):
        if isinstance(conductor_id, int):
            self.__conductor_id = conductor_id
        else:
            raise ValueError("Conductor ID no válido")

    def getConductorId(self):
        return self.__conductor_id

    def setTipoEnvioId(self, tipo_envio_id):
        if isinstance(tipo_envio_id, int):
            self.__tipo_envio_id = tipo_envio_id
        else:
            raise ValueError("Tipo de envío ID no válido")

    def getTipoEnvioId(self):
        return self.__tipo_envio_id

    def setEstadoActual(self, estado_actual):
        if isinstance(estado_actual, int):
            self.__estado_actual = estado_actual
        else:
            raise ValueError("Estado actual no válido")

    def getEstadoActual(self):
        return self.__estado_actual

    def setFechaCreacion(self, fecha_creacion):
        if isinstance(fecha_creacion, datetime):
            self.__fecha_creacion = fecha_creacion
        else:
            raise ValueError("Fecha de creación no válida")

    def getFechaCreacion(self):
        return self.__fecha_creacion