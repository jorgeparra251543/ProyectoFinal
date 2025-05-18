#Clase o entidad conductores

#Cada entidad es una clase
class Conductores:
    #Metodo constructor con parametros
    def __init__(self,id,nombre, cedula, telefono):
        self.setId(id)
        self.setNombre(nombre)
        self.setCedula(cedula)
        self.setTelefono(telefono)

    #Metodos Get y Set para acceder a los atributos

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

    def getCedula(self):
        return self.__cedula

    def setCedula(self, cedula):
        if isinstance(cedula, str):
            self.__cedula = cedula
        else:
            raise ValueError("Cédula no válida")
        
    def getTelefono(self):
        return self.__telefono

    def setTelefono(self, telefono):
        if isinstance(telefono, str):
            self.__telefono = telefono
        else:
            raise ValueError("Telefono no valido")