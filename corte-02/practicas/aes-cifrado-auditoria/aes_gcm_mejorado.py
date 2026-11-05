
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# 1. Generar una clave aleatoria de 128 bits (16 bytes)
key = get_random_bytes(16)
mensaje = "hola tonotos prueba de cifrado AES-GCM en lab"

# 2. Crear cifrador AES-128 en modo GCM
cipher = AES.new(key, AES.MODE_GCM)
nonce = cipher.nonce  # Nonce generado automáticamente por PyCryptodome

# 3. Cifrar el mensaje y generar el tag de autenticación (no requiere padding)
cifrado, tag = cipher.encrypt_and_digest(mensaje.encode("utf-8"))

print("Mensaje original:","hola tonotos prueba de cifrado AES-GCM en lab")
print("Mensaje cifrado (Base64):", base64.b64encode(cifrado).decode())
print("Nonce (Base64):", base64.b64encode(nonce).decode())
print("Tag de autenticación (Base64):", base64.b64encode(tag).decode())

# 4. Descifrado y verificación de integridad
decipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
original_bytes = decipher.decrypt_and_verify(cifrado, tag)

print("Mensaje recuperado:", original_bytes.decode("utf-8"))
