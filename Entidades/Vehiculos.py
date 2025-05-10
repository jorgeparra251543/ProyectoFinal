#Clase o entidad vehiculos

#Cada entidad es una clase
class Vehiculos:
    #Metodo constructor con parametros
    def __init__(self,id,placa,tipo,capacidad):
        self.setId(id)
        self.setPlaca(placa)
        self.setTipo(tipo)
        self.setCapacidad(capacidad)
    
    #Metodos Get y Set para acceder a los atributos

    def getId(self):
        return self.__id

    def setId(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            raise ValueError("Id no válido")

    def getPlaca(self):
        return self.__placa

    def setPlaca(self, placa):
        if isinstance(placa, str) and placa.strip():
            self.__placa = placa
        else:
            raise ValueError("Placa no válido")

    def getTipo(self):
        return self.__tipo

    def setTipo(self, tipo):
        if isinstance(tipo, str) and tipo.strip():
            self.__tipo = tipo
        else:
            raise ValueError("Tipo no válido")
        
    def getCapacidad(self):
        return self.__capacidad

    def setCapacidad(self, capacidad):
        if isinstance(capacidad, int):
            self.__capacidad = capacidad
        else:
            raise ValueError("Vehiculo no valido")