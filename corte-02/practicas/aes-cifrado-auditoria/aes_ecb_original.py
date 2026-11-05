from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

key = b"1234567890123456"
mensaje = "Información confidencial del cliente"

cipher = AES.new(key, AES.MODE_ECB)
cifrado = cipher.encrypt(pad(mensaje.encode(), 16))

print("Mensaje original:", mensaje)
print("Mensaje cifrado:", base64.b64encode(cifrado).decode())

decipher = AES.new(key, AES.MODE_ECB)
original = unpad(decipher.decrypt(cifrado), 16)
print("Mensaje recuperado:", original.decode())
