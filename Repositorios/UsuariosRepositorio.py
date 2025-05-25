#Improtar clases de otras carpetas del proyecto
from Nucleo import Conexion
from tabulate import tabulate
from Utilidades import EncriptarAES
from Entidades.Usuarios import Usuarios  # Asegúrate de que esta clase exista y tenga getters

#Cada entidad es una clase
class UsuariosRepositorio:

    #Insertar usuario     
    def Guardar(self, usuario):
        try:
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL InsertarUsuarios({usuario.getId()},'{usuario.getNombre()}','{usuario.getEmail()}','{usuario.getTelefono()}','{usuario.getDireccion()}','{usuario.getRol()}','{usuario.getFechaRegistro()}');"
           ObjConexion.ejecutarNoQuery(consulta)
           ObjConexion.desconectar()
           print("Dato Insertado")
           return True
        except Exception as ex:
            print(str(ex));
    
    #Actualizar usuarios 
    def Actualizar(self, usuario):
        try:
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL ActualizarUsuarios({usuario.getId()},'{usuario.getNombre()}','{usuario.getEmail()}','{usuario.getTelefono()}','{usuario.getDireccion()}','{usuario.getRol()}','{usuario.getFechaRegistro()}');"
           ObjConexion.ejecutarNoQuery(consulta)
           ObjConexion.desconectar()
           print("Dato Actualizado")
           return True
        except Exception as ex:
            print(str(ex));
    
    #Eliminar usuarios     
    def Eliminar(self, usuario:Usuarios):
        try:
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL EliminarUsuariosPorId({usuario.getId()});"
           ObjConexion.ejecutarNoQuery(consulta)
           ObjConexion.desconectar()
           print("Dato Eliminado")
           return True
        except Exception as ex:
            print(str(ex));
    
    #Consultar usuarios     
    def Consultar(self, usuarios):
        try:
           ObjConexion = Conexion.Conexion()
           ObjConexion.conectar()
           consulta = f"CALL ConsultarUsuariosPorId({usuarios.getId()});"
           tabla=ObjConexion.ejecutarQuery(consulta)

           if not tabla:
               print("No se encontraro usuario")
               ObjConexion.desconectar()

           ObjAES=EncriptarAES.EncriptarAES()

           for elemento in tabla:
               id = elemento[0]
               nombre=elemento[1]
               email=ObjAES.Decifrar(elemento[2])
               telefono=ObjAES.Decifrar(elemento[3])
               direccion=ObjAES.Decifrar(elemento[4])
               rol = elemento[5]
               fecharegistro= elemento[6]
               print(f"ID: {id}, Nombre: {nombre}, Email: {email}, Telefono: {telefono},Direccion: {direccion},Rol: {rol},FechaRegistro: {fecharegistro}")

           ObjConexion.desconectar()
           return True
        except Exception as ex:
            print(str(ex));