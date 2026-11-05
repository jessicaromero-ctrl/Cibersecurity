# Registro de auditoría con inteligencia artificial (Parte 2)

**Maestría en Inteligencia Artificial · UPMH · Ciberseguridad · Periodo 2026**
**Alumna:** Jessica Melani Romero Lora · **Profesor:** Dr. Antonio Cedillo Hernández

> **Aviso de uso académico.** Este registro tiene fines exclusivamente académicos y educativos. Las técnicas descritas deben aplicarse únicamente en entornos aislados y autorizados.

---

## 1. Herramienta utilizada

- **Herramienta:** Google Gemini.
- **Código enviado:** `aes_ecb_original.py` (AES-128 en modo ECB, clave fija `b"1234567890123456"`).

## 2. Prompt utilizado (Parte 2)

```
Actúa como un especialista en ciberseguridad y criptografía. Analiza este código Python que utiliza AES para proteger información confidencial. Identifica tres riesgos o debilidades de seguridad y explica cada uno de forma sencilla. Propón alternativas más seguras y justifica tus recomendaciones. No modifiques el código todavía.
```

## 3. Respuesta de la IA (transcrita sin modificaciones)

**1. Uso del modo de operación ECB (Electronic Codebook)**

- **Explicación sencilla:** El modo ECB divide el mensaje en bloques de 16 bytes y cifra cada uno exactamente con la misma regla y clave. Si dos bloques de texto plano son idénticos, sus bloques cifrados resultantes serán idénticos. Esto permite a un atacante identificar patrones visuales o de estructura en los datos sin necesidad de descifrar la clave.
- **Alternativa recomendada:** Cambiar el modo de operación a AES-GCM (Galois/Counter Mode) o AES-CBC (Cipher Block Chaining) utilizando un Vector de Inicialización (IV) o nonce único y aleatorio para cada mensaje.
- **Justificación:** Al incorporar un IV aleatorio por cada operación, dos mensajes idénticos (o bloques idénticos dentro de un mismo mensaje) generarán textos cifrados completamente diferentes, eliminando cualquier patrón detectable.

**2. Clave incrustada en el código (Hardcoded Key) y de baja entropía**

- **Explicación sencilla:** La clave de cifrado (`"1234567890123456"`) está escrita directamente en el texto del código fuente y consiste en una secuencia numérica predecible. Cualquier usuario con acceso al repositorio de código, copias de seguridad o archivos compilados obtendrá acceso directo a los datos protegidos.
- **Alternativa recomendada:** Separar el código fuente de las credenciales utilizando variables de entorno o un servicio de gestión de secretos (como AWS Secrets Manager, HashiCorp Vault o Azure Key Vault). Adicionalmente, la clave debe generarse mediante una función criptográficamente segura como `secrets.token_bytes(16)` o `os.urandom(16)`.
- **Justificación:** Previene la filtración de credenciales en repositorios de control de versiones (como Git) y asegura que la clave tenga la aleatoriedad (entropía) necesaria para hacer inviable un ataque de fuerza bruta o de diccionario.

**3. Ausencia de autenticación e integridad de los datos**

- **Explicación sencilla:** El proceso utilizado solo intenta ocultar la información (confidencialidad), pero no comprueba si el texto cifrado ha sido alterado. Si un atacante intercepta el mensaje y modifica algunos bytes en el camino, el receptor intentará descifrar el mensaje modificado sin saber que fue manipulado, lo que puede corromper datos o causar fallos en la aplicación.
- **Alternativa recomendada:** Implementar un esquema de Cifrado Autenticado con Datos Asociados (AEAD), siendo AES-GCM la norma estándar en la industria.
- **Justificación:** AEAD genera una etiqueta de autenticación (Authentication Tag) junto con el texto cifrado. Al momento de descifrar, la biblioteca verifica esta etiqueta; si el mensaje fue modificado aunque sea en un solo bit, la operación se rechaza inmediatamente antes de procesar el texto plano, evitando ataques de manipulación de datos y de oráculo de relleno (Padding Oracle).

## 4. Análisis crítico de la respuesta

| Observación de la IA | Evaluación | Corrección o precisión |
|---|---|---|
| ECB permite identificar patrones. | Correcta. | Precisar que se revelan bloques repetidos, no el contenido del mensaje. |
| Sustituir ECB por CBC con IV aleatorio. | Insuficiente. | CBC evita los patrones, pero no ofrece autenticación. Para el riesgo de integridad, la recomendación correcta es AES-GCM. |
| La clave hardcodeada es un riesgo. | Correcta. | La clave no es una credencial de acceso a la plataforma: es la clave que protege los datos. Su exposición compromete la confidencialidad. |
| Usar `secrets.token_bytes(16)` o `os.urandom(16)`. | Correcta. | Ambas funciones generan aleatoriedad criptográficamente segura. |
| Mencionar el oráculo de relleno (padding oracle) como beneficio de AES-GCM. | Imprecisa. | GCM no usa relleno, por lo que ese ataque no aplica a GCM. Aplica a CBC con relleno PKCS#7 mal implementado. |
| AES-GCM verifica la etiqueta antes de procesar el texto plano. | Correcta. | Se confirma con `decrypt_and_verify`, que rechaza el mensaje ante cualquier modificación. |

## 5. Decisiones tomadas a partir del análisis

1. Se acepta el diagnóstico de los tres riesgos (clave hardcodeada, modo ECB y ausencia de integridad), pero se describe cada uno con precisión técnica en el documento final.
2. Se descarta CBC como solución al riesgo de integridad y se adopta AES-GCM.
3. Se mantiene la recomendación de gestionar la clave fuera del código y generarla con una fuente aleatoria segura.
4. La mención al oráculo de relleno se conserva solo como referencia, y se aclara que no aplica a GCM.

## 6. Referencia a la implementación

- Código original: `aes_ecb_original.py`.
- Código mejorado: `aes_gcm_mejorado.py` (generado a partir del prompt de la Parte 3, con correcciones de sintaxis y de nombres de variables).
- Prueba de manipulación: `prueba_manipulacion.py`.
