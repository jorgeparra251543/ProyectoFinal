class Departamento:
    def __init__(self, id, nombre):
        self.setId(id)
        self.setNombre(nombre)

    def getId(self):
        return self.__id

    def setId(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise ValueError("ID de departamento no válido")

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        if isinstance(nombre, str) and nombre.strip():
            self.__nombre = nombre
        else:
            raise ValueError("Nombre de departamento no válido")
