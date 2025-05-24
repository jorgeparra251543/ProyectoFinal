class Ciudades:
    def __init__(self, id, nombre, departamento_id):
        self.setId(id)
        self.setNombre(nombre)
        self.setDepartamento(departamento_id)

    def getId(self):
        return self.__id

    def setId(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise ValueError("Id no válido")

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            raise ValueError("Nombre no válido")

    def getDepartamento(self):
        return self.__departamento_id

    def setDepartamento(self, departamento_id):
        if isinstance(departamento_id, int):
            self.__departamento_id = departamento_id
        else:
            raise ValueError("Id departamento no válido")