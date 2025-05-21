#Clase o entidad tipo envio

#Cada entidad es una clase
class Tipo_Envio:
    
    #Metodo constructor con parametros
    def __init__(self,id,nombre):
        self.setId(id)
        self.setNombre(nombre)
    
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