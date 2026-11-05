import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# 1. Cifrado original con AES-GCM
key = get_random_bytes(16)
mensaje = "hola tonotos prueba de cifrado AES-GCM en lab"

cipher = AES.new(key, AES.MODE_GCM)
nonce = cipher.nonce
cifrado, tag = cipher.encrypt_and_digest(mensaje.encode("utf-8"))

print("Texto cifrado original (Base64):", base64.b64encode(cifrado).decode())

# 2. Control: descifrado sin alterar los datos
decipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
recuperado = decipher.decrypt_and_verify(cifrado, tag)
print("Control, mensaje recuperado:", recuperado.decode("utf-8"))

# 3. Prueba: modificar un byte del texto cifrado (conservando el tag original)
cifrado_alterado = bytearray(cifrado)
cifrado_alterado[0] ^= 0x01
print("Texto cifrado alterado (Base64):", base64.b64encode(bytes(cifrado_alterado)).decode())

# 4. Verificación de autenticidad sobre el texto alterado
decipher_alterado = AES.new(key, AES.MODE_GCM, nonce=nonce)
try:
    resultado = decipher_alterado.decrypt_and_verify(bytes(cifrado_alterado), tag)
    print("Mensaje recuperado:", resultado.decode("utf-8"))
except ValueError:
    print("ERROR: falló la verificación de autenticidad. El mensaje fue modificado.")
