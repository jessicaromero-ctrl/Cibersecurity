# Esteganografía en imagen y texto con plataformas de mensajería

| | |
|---|---|
| **Asignatura** | Ciberseguridad |
| **Programa** | Maestría en Inteligencia Artificial |
| **Institución** | Universidad Politécnica Metropolitana del Estado de Hidalgo (UPMH) |
| **Línea de investigación** | Automatización de Procesos Aplicados a la Ingeniería |
| **Alumna** | Jessica Melani Romero Lora |
| **Profesor** | Dr. Antonio Cedillo Hernández |
| **Periodo** | 2026 |
| **Actividad** | 3. Esteganografía |
| **Documento** | `Estenografía.pdf` |
| **Entorno** | Archivos propios; envío por correo, WhatsApp e Instagram |

---

> ⚠️ **AVISO DE SEGURIDAD Y USO ACADÉMICO**
>
> - Este documento forma parte de una **práctica de la Maestría en Inteligencia Artificial de la UPMH**. Su contenido tiene **fines exclusivamente académicos y educativos**.
> - **No debe replicarse.** Las técnicas de ocultamiento descritas no deben usarse para enviar contenido malicioso, instrucciones de ataque ni información sin consentimiento, ni a través de plataformas de terceros.
> - Este documento y su contenido están **protegidos como documentos académicos**. Se prohíbe su reproducción, distribución o uso total o parcial sin autorización de la autora.

## 1. Descripción técnica

La esteganografía oculta información dentro de un medio aparentemente normal: una imagen o un texto. A diferencia del cifrado, el objetivo no es que el contenido sea ilegible, sino que **no se perciba que existe**.

La práctica evalúa tres experimentos. En cada uno se oculta un mensaje, se transmite por un canal y se verifica si el mensaje sobrevive y si el archivo muestra alteraciones visibles:

1. **Mensaje en imagen, comprimido en .rar.** El mensaje se oculta en una imagen y el resultado se comprime en formato .rar.
2. **Mensaje en texto con Unicode Steganography (330k).** Se insertan caracteres invisibles en un texto que se envía después.
3. **Mensaje en imagen publicada como historia de Instagram.** La imagen con el mensaje oculto se sube a la aplicación sin modificarla.

## 2. Objetivo

Evaluar si es posible ocultar información de ataque en medios cotidianos, y si ese contenido sobrevive al paso por plataformas de comunicación sin alteraciones perceptibles.

## 3. Marco teórico

- **Esteganografía frente a cifrado.** El cifrado protege el contenido; la esteganografía protege la existencia del canal. En seguridad, esto la convierte en un medio para **canales encubiertos** (*covert channels*).
- **Triada CIA.** La práctica muestra cómo un canal encubierto puede comprometer la **confidencialidad** (información sacada del sistema sin ser vista) e **integridad** (instrucciones ocultas en archivos aparentemente legítimos).
- **Modelo de riesgo.** $R = P(\text{amenaza explota vulnerabilidad}) \times I(\text{impacto})$. La práctica sugiere que $P$ es alto: las plataformas aceptan los archivos sin cuestionarlos.
- **Costo de ocultar información en una imagen.** Una medida útil es el aumento de tamaño del archivo tras insertar el mensaje. Con los datos del experimento 1:

$$
\Delta\% = \frac{59\,000 - 50\,000}{50\,000} \times 100 = 18\%
$$

Ese aumento es una señal que puede usarse para detectar el archivo, aunque el contenido visual no cambie.

## 4. Entorno y herramientas

| Componente | Función |
|---|---|
| **Herramienta de ocultamiento en imagen** | Inserta el mensaje en la imagen *(pendiente: nombre y versión)* |
| **Compresión .rar** | Empaqueta la imagen con el mensaje *(pendiente: herramienta)* |
| **Unicode Steganography (330k)** | Oculta el mensaje en caracteres Unicode de un texto |
| **WhatsApp, correo electrónico, Instagram** | Canales de transmisión para las pruebas de robustez |

## 5. Procedimiento

**Experimento 1: imagen y .rar**

1. Ocultar el mensaje dentro de una imagen.
2. Comprimir el resultado en formato .rar.
3. Enviar el archivo por correo electrónico, WhatsApp y plataformas sociales.
4. Verificar que la imagen no presente alteraciones visibles y que el mensaje se decodifique en el destino.

**Experimento 2: texto con Unicode Steganography**

1. Insertar el mensaje en un texto con Unicode Steganography (330k).
2. Descargar el texto modificado y enviarlo por WhatsApp e Instagram.
3. Decodificar el texto recibido para recuperar el mensaje original.

**Experimento 3: historia de Instagram**

1. Insertar el mensaje en una imagen.
2. Subir la imagen como historia de Instagram sin modificarla.
3. Verificar que la plataforma la acepte sin cambios visibles y que el mensaje se pueda recuperar.

## 6. Resultados observados

| Experimento | Canal | Resultado |
|---|---|---|
| 1. Imagen en .rar | Correo electrónico | Mensaje decodificado correctamente |
| 1. Imagen en .rar | WhatsApp | Mensaje decodificado correctamente |
| 1. Imagen en .rar | Plataformas sociales | La imagen no mostró alteraciones |
| 1. Imagen en .rar | Tamaño del archivo | Aumentó de 50 000 KB a 59 000 KB (+18 %) |
| 2. Texto (Unicode, 330k) | WhatsApp e Instagram | Sin alteración perceptible; mensaje recuperado solo al decodificar |
| 3. Historia de Instagram | Instagram | Aceptada sin cambios aparentes; el mensaje se mantuvo oculto |

Ningún destinatario del experimento 2 detectó la alteración del texto.

## 7. Conclusiones

- Fue posible ocultar información de ataque en formatos distintos (imagen y texto) con técnicas diferentes.
- Las imágenes sobrevivieron al paso por correo, WhatsApp y redes sociales sin alteraciones visibles, pero su tamaño sí cambió, lo que puede delatar la presencia del mensaje.
- Las plataformas aceptaron los archivos sin análisis de contenido. Esto permite introducir instrucciones o información cifrada en archivos comunes y mantenerlos disponibles en plataformas sociales.

## 8. Implicaciones defensivas

- **Análisis forense de archivos.** Revisar la entropía, los metadatos y el tamaño de los archivos recibidos.
- **Recompresión o re-codificación** de imágenes en servidores de la organización, lo que suele destruir el contenido oculto en el bit menos significativo.
- **Normalización de texto**, eliminando caracteres Unicode invisibles antes de procesarlo.
- **Política de monitoreo** de canales de salida, sin depender solo del contenido visible del archivo.

## 9. Consideraciones éticas y de alcance

- Las pruebas del experimento 2 y 3 se enviaron a **destinatarios reales** a través de plataformas en producción. Para futuras prácticas, deben usarse cuentas propias o de prueba, y no personas que no hayan dado su consentimiento.
- El contenido de los mensajes debe ser inocuo. Una instrucción real de ataque, aunque sea de prueba, no debe enviarse por canales de terceros.

## 10. Pendientes para completar

*[Completar con datos del PDF: nombre y versión de la herramienta de esteganografía en imagen, algoritmo usado, si hubo contraseña, texto del mensaje de prueba y la transcripción completa de las conclusiones.]*

## 11. Archivos de esta carpeta

- `readme.md`: este documento.
- `Estenografía.pdf`: informe original. *(Debe colocarse en esta misma carpeta.)*
