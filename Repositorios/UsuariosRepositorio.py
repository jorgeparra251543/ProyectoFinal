#Improtar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate

#Cada entidad es una clase
class UsuariosRepositorio:

    #Insertar usuario     
    def Guardar(self, usuario):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""INSERT INTO Usuarios (id,nombre,email,telefono,direccion,rol,fecha_registro) VALUES ({usuario.getId()},'{usuario.getNombre()}','{usuario.getEmail()}','{usuario.getTelefono()}','{usuario.getDireccion()}','{usuario.getRol()}','{usuario.getFechaRegistro()}')"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Insertado")
        return True
    
    #Actualizar usuarios 
    def Actualizar(self, usuario):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""UPDATE Usuarios SET nombre='{usuario.getNombre()}',email='{usuario.getEmail()}',telefono='{usuario.getTelefono()}',direccion='{usuario.getDireccion()}',rol='{usuario.getRol()}',fecha_registro='{usuario.getFechaRegistro()}' Where id= {usuario.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Actualizado")
        return True
    
    #Eliminar usuarios     
    def Eliminar(self, usuario):
        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""DELETE FROM Usuarios WHERE id={usuario.getId()}"""
        ObjConexion.ejecutarNoQuery(consulta)
        ObjConexion.desconectar()
        print("Dato Eliminado")
        return True
    
    #Consultar usuarios     
    def Consultar(self, usuarios):

        ObjConexion = Conexion.Conexion()
        ObjConexion.conectar()
        consulta = f"""SELECT * FROM Conductores  WHERE id={usuarios.getId()}"""
        tabla=ObjConexion.ejecutarQuery(consulta)
        print("Dato Consultado")
        print(tabulate(tabla, headers=["ID","Nombre","Email","Telefono","Direccion","Rol","FechaRegistro"], tablefmt="grid"))
        ObjConexion.desconectar()
        return True