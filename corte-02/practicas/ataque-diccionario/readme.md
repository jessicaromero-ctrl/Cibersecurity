# Ataque de Diccionario contra autenticación web (DVWA)

| | |
|---|---|
| **Asignatura** | Ciberseguridad |
| **Programa** | Maestría en Inteligencia Artificial |
| **Institución** | Universidad Politécnica Metropolitana del Estado de Hidalgo (UPMH) |
| **Línea de investigación** | Automatización de Procesos Aplicados a la Ingeniería |
| **Alumna** | Jessica Melani Romero Lora |
| **Profesor** | Dr. Antonio Cedillo Hernández |
| **Periodo** | 2026 |
| **Actividad** | 2. Ataque de diccionario |
| **Documento** | `Ataque de Diccionario.pdf` |
| **Entorno** | Laboratorio aislado con Docker |

---

> ⚠️ **AVISO DE SEGURIDAD Y USO ACADÉMICO**
>
> - Este documento forma parte de una **práctica de la Maestría en Inteligencia Artificial de la UPMH**. Su contenido tiene **fines exclusivamente académicos y educativos**.
> - **No debe replicarse** fuera de un laboratorio aislado y autorizado. Las técnicas descritas no deben aplicarse contra sistemas, cuentas, redes ni personas sin autorización expresa y por escrito.
> - Este documento y su contenido están **protegidos como documentos académicos**. Se prohíbe su reproducción, distribución o uso total o parcial sin autorización de la autora.

## 1. Descripción técnica

La práctica describe la instalación, la experimentación y la ejecución de un ataque de diccionario contra el formulario de autenticación de **DVWA (Damn Vulnerable Web Application)**, una aplicación web deliberadamente vulnerable. El flujo tiene dos fases:

1. **Intercepción.** Un proxy de interceptación (OWASP ZAP) captura la petición HTTP que envía el formulario de inicio de sesión (usuario y contraseña).
2. **Fuzzing.** Sobre esa petición capturada, ZAP reemplaza el campo de contraseña con los valores de una lista (diccionario) y analiza la respuesta de cada intento.

Todo el entorno se levanta con Docker: un contenedor para DVWA (objetivo), otro para la base de datos MariaDB que usa DVWA, y ZAP como herramienta de análisis.

## 2. Objetivo

Evaluar qué tan vulnerable es un formulario de autenticación con contraseñas débiles ante un ataque de diccionario, y documentar las medidas que lo impedirían.

## 3. Marco teórico

- **Modelo de riesgo.** El riesgo de una amenaza se cuantifica como $R = P(\text{amenaza explota vulnerabilidad}) \times I(\text{impacto})$. Un ataque de diccionario aumenta $P$ cuando las contraseñas son predecibles.
- **Ataque de diccionario.** Prueba sistemáticamente contraseñas tomadas de una lista de candidatas. Su probabilidad de éxito depende de qué tan frecuentes son las contraseñas de la víctima en esa lista:

$$
P(\text{éxito}) = \frac{|D \cap C|}{|C|}
$$

donde $D$ es el diccionario de candidatas y $C$ el conjunto de contraseñas reales de los usuarios.

- **Relación con la tríada CIA.** Un acceso indebido compromete la **confidencialidad** (datos del usuario) y la **integridad** (modificación de datos tras el acceso).
- **Riesgo de categoría A07:2021 (OWASP Top 10).** Corresponde a fallas de identificación y autenticación, entre ellas la ausencia de límites de intentos y las contraseñas débiles.

## 4. Entorno y herramientas

| Componente | Función |
|---|---|
| **Docker** | Despliegue aislado de DVWA y de su base de datos |
| **DVWA** | Aplicación web objetivo con formulario de login |
| **MariaDB** | Base de datos que usa DVWA para almacenar usuarios |
| **OWASP ZAP** | Proxy de interceptación y motor de fuzzing sobre la contraseña |

*[Completar con versiones de Docker, imágenes utilizadas, versión de ZAP y nivel de seguridad configurado en DVWA.]*

## 5. Procedimiento

1. Levantar los contenedores de DVWA y MariaDB con Docker, y verificar que la página de login responde.
2. Configurar OWASP ZAP como proxy del navegador.
3. Enviar una petición de login con credenciales de prueba y capturarla con ZAP (intercepción).
4. Marcar el campo de contraseña como punto de inyección en la petición capturada.
5. Lanzar el fuzzer de ZAP con la lista de contraseñas candidatas.
6. Analizar las respuestas: un intento fallido muestra el mensaje *Login failed*; un intento exitoso debe distinguirse por una diferencia en la respuesta (código HTTP, longitud o contenido).
7. Registrar las credenciales válidas encontradas, si las hay.

## 6. Resultados observados

- La página de login de DVWA respondió con el mensaje **"Login failed"** tras los intentos de prueba (captura incluida en el documento original).
- La práctica se realizó **únicamente en el laboratorio aislado**, nunca contra un sistema de terceros.

*[Pendiente de completar con datos del PDF: tamaño y origen del diccionario, número total de intentos, tiempo de ejecución, criterio que distingue un login exitoso, y contraseñas recuperadas.]*

## 7. Conclusiones

*[Pendiente: transcribir las conclusiones del documento original. Como mínimo, debe relacionar el resultado con la falta de límite de intentos y con la calidad de las contraseñas.]*

## 8. Medidas de mitigación

- **Limitar intentos** por cuenta y por dirección IP, con bloqueo temporal o aumento progresivo de la espera.
- **Política de contraseñas** que rechace contraseñas de diccionario y contraseñas comunes.
- **Autenticación multifactor** para que una contraseña adivinada no baste para entrar.
- **Mensajes de error uniformes**, que no revelen si el usuario existe.
- **Monitoreo** de patrones de intentos fallidos repetidos.

## 9. Consideraciones éticas y de alcance

- Esta práctica se realiza en un laboratorio aislado y con un objetivo diseñado para ser vulnerable. No debe ejecutarse contra sistemas de terceros sin autorización escrita.
- Las credenciales obtenidas en el laboratorio no deben reutilizarse fuera de él.

## 10. Archivos de esta carpeta

- `readme.md`: este documento.
- `Ataque de Diccionario.pdf`: informe original. *(Debe colocarse en esta misma carpeta.)*
