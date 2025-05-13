import hashlib;
import binascii, os;
from Crypto.Cipher import AES;

#Clase para encriptar o desencriptar 
class EncriptarAES:

    #Es una clave secreta de 32 bytes que se utiliza tanto para cifrar como para descifrar el mensaje. 
    secretKey = b'\x11\x9b$\xe8\x13\xe7\x18\xe7\x8e{\x86v\x1ab\x8c\xb7\x911Q@ \xca\xa4e\xc75H\x95\x89\xa6\x9d\xab';
    
    #Metodo para encriptar
    def Cifrar(self, valor: str) -> str:
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM);
        ciphertext, authTag = aesCipher.encrypt_and_digest(str.encode(valor));
        response = (ciphertext, aesCipher.nonce, authTag);
        return binascii.hexlify(response[0]).decode() + '|' + binascii.hexlify(response[1]).decode() + '|' + binascii.hexlify(response[2]).decode();
    
    #Metodo para desencriptar
    def Decifrar(self, valor: str) -> str:
        split = valor.split('|');
        ciphertext = binascii.unhexlify(split[0]);
        nonce = binascii.unhexlify(split[1]);
        authTag = binascii.unhexlify(split[2]);
        aesCipher = AES.new(self.secretKey, AES.MODE_GCM, nonce);
        plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag);
        return plaintext.decode();