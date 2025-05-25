class Ruta:
    def __init__(self, id, ciudad_origen_id=None, ciudad_destino_id=None, zona_id=None):
        self.setId(id)

        if ciudad_origen_id is not None:
            self.setCiudadOrigenId(ciudad_origen_id)
        if ciudad_destino_id is not None:
            self.setCiudadDestinoId(ciudad_destino_id)
        if zona_id is not None:
            self.setZonaId(zona_id)

    def setId(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise ValueError("ID de ruta no válido")

    def getId(self):
        return self.__id

    def setCiudadOrigenId(self, ciudad_origen_id):
        if isinstance(ciudad_origen_id, int):
            self.__ciudad_origen_id = ciudad_origen_id
        else:
            raise ValueError("ID de ciudad origen no válido")

    def getCiudadOrigenId(self):
        return self.__ciudad_origen_id

    def setCiudadDestinoId(self, ciudad_destino_id):
        if isinstance(ciudad_destino_id, int):
            self.__ciudad_destino_id = ciudad_destino_id
        else:
            raise ValueError("ID de ciudad destino no válido")

    def getCiudadDestinoId(self):
        return self.__ciudad_destino_id

    def setZonaId(self, zona_id):
        if isinstance(zona_id, int):
            self.__zona_id = zona_id
        else:
            raise ValueError("ID de zona no válido")

    def getZonaId(self):
        return self.__zona_id
