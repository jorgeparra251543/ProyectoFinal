
import pyodbc  # Para conectar a la BD

#Cada entidad(conductores) debe tener su conexion, en base de datos, y aca es donde deberia estar el string que se arma para enviar a sql

#esta clase debe estar exisiendo y otra clase que use esta clase para conectar o insertar, la otra clase me concatena el string que se ejecuta en base de datos
class Conexion:

    #Metodo constructor
    def __init__(self):

        #Cadena de conexion 
        self.__CadenaConexion = "Driver={MySQL ODBC 9.2 Unicode Driver};Server=localhost;Database=enviobd;PORT=3306;user=user_python;password=Pass2025**"
        self.__Conexion = pyodbc.connect(self.__CadenaConexion)
        self.__ObjCursor = self.__Conexion.cursor()

    #Crear cursor para interacturar con la BD    
    def conectar(self):
        self.__ObjCursor=self.__Conexion.cursor()
    
    #Cerrar cursor 
    def desconectar(self):
        self.__ObjCursor.close()

    #Operacion que no devuelve tabla (Insertar,Actualizar,Eliminar)
    def ejecutarNoQuery(self,consultaSQL): #Ejecuto sonsulta
        self.__ObjCursor.execute(consultaSQL); #Ejecuto consulta
        self.__ObjCursor.commit(); #Guardo en BD

    #Operacion que devuelve tabla (Consulta)
    def ejecutarQuery(self,consultaSQL):
        self.__ObjCursor.execute(consultaSQL); #Ejecuto consulta
        tabla= self.__ObjCursor.fetchall()  # Esto asegura que se lean los resultados de la consulta   
        return tabla;

