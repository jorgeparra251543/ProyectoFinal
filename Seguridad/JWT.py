import jwt  # Importamos la librería JWT para generar y verificar tokens
import datetime  # Para manejar fechas y tiempos (para poner fecha de expiración al token)

# Clave secreta que se usa para firmar el token. Debería ser secreta y no compartirse.
CLAVE_SECRETA = "clave123"

class SeguridadJWT:
    
    # Método estático para generar un token
    @staticmethod
    def generar_token(usuario: str):
        # Creamos un diccionario con los datos que queremos almacenar en el token
        payload = {
            'usuario': usuario,  # Usamos el nombre de usuario
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Fecha de expiración (1 hora)
        }
        # Generamos el token usando la clave secreta y el algoritmo HS256
        token = jwt.encode(payload, CLAVE_SECRETA, algorithm='HS256')
        return token  # Retornamos el token generado

    # Método estático para verificar si un token es válido
    @staticmethod
    def verificar_token(token: str):
        try:
            # Decodificamos el token usando la clave secreta y verificamos su validez
            payload = jwt.decode(token, CLAVE_SECRETA, algorithms=['HS256'])
            return payload  # Si es válido, devolvemos los datos del token
        except jwt.ExpiredSignatureError:
            raise Exception("Token expirado")  # Si el token ha expirado
        except jwt.InvalidTokenError:
            raise Exception("Token incorrecto")  # Si el token no es válido
