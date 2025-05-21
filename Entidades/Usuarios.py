from datetime import datetime

#Clase o entidad usuarios

#Cada entidad es una clase
class Usuarios:
    
    #Metodo constructor con parametros
    def __init__(self,id,nombre,email,telefono,direccion,rol,fechaRegistro):
        self.setId(id)
        self.setNombre(nombre)
        self.setEmail(email)
        self.setTelefono(telefono)
        self.setDireccion(direccion)
        self.setRol(rol)
        self.setFechaRegistro(fechaRegistro)
    
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
        
    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        if isinstance(email, str):
            self.__email = email
        else:
            raise ValueError("Email no válido")

    def getTelefono(self):
        return self.__telefono

    def setTelefono(self, telefono):
        if isinstance(telefono, str):
            self.__telefono = telefono
        else:
            raise ValueError("Telefono no válido")
        
    def getDireccion(self):
        return self.__direccion

    def setDireccion(self, direccion):
        if isinstance(direccion, str):
            self.__direccion = direccion
        else:
            raise ValueError("Direccion no válido")
        
    def getRol(self):
        return self.__rol

    def setRol(self, rol):
        if isinstance(rol, str):
            self.__rol = rol
        else:
            raise ValueError("Rol no válido")
        
    def getFechaRegistro(self):
        return self.__fechaRegistro
    
    def setFechaRegistro(self, fechaRegistro):
        if isinstance(fechaRegistro, str):
            try:
                # Intenta convertir usando formato ISO 8601
                fechaRegistro = datetime.fromisoformat(fechaRegistro)
            except ValueError:
                raise ValueError("Formato de fecha inválido. Usa 'YYYY-MM-DDTHH:MM:SS'")
        
        if isinstance(fechaRegistro, datetime):
            self.__fechaRegistro = fechaRegistro
        else:
            raise ValueError("Fecha no válida")

    