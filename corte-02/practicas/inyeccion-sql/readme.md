# Inyección SQL en aplicaciones web

| | |
|---|---|
| **Asignatura** | Ciberseguridad |
| **Programa** | Maestría en Inteligencia Artificial |
| **Institución** | Universidad Politécnica Metropolitana del Estado de Hidalgo (UPMH) |
| **Línea de investigación** | Automatización de Procesos Aplicados a la Ingeniería |
| **Alumna** | Jessica Melani Romero Lora |
| **Profesor** | Dr. Antonio Cedillo Hernández |
| **Periodo** | 2026 |
| **Actividad** | 1. Inyección SQL |
| **Documento** | `Inyección SQL.pdf` |
| **Entorno** | Ver sección 4: el entorno original **no es un laboratorio controlado** |

---

> **Aviso importante.** La práctica original describe pruebas sobre un portal público de un gobierno municipal, en producción. Eso no está autorizado y no corresponde al entorno controlado que declara el repositorio. Este documento no repite la dirección del sitio. Antes de publicar el repositorio, la sección 4 debe reescribirse para usar únicamente laboratorios diseñados para practicar, como se indica en la sección 4.2.

---

> ⚠️ **AVISO DE SEGURIDAD Y USO ACADÉMICO**
>
> - Este documento forma parte de una **práctica de la Maestría en Inteligencia Artificial de la UPMH**. Su contenido tiene **fines exclusivamente académicos y educativos**.
> - **No debe replicarse** contra sistemas reales. La inyección SQL solo debe practicarse en laboratorios aislados y autorizados. Probarla contra sitios de terceros puede constituir un delito.
> - Este documento y su contenido están **protegidos como documentos académicos**. Se prohíbe su reproducción, distribución o uso total o parcial sin autorización de la autora.

## 1. Descripción técnica

La inyección SQL ocurre cuando una aplicación concatena datos enviados por el usuario dentro de una consulta a la base de datos, sin separarlos de la lógica de la consulta. Un atacante puede entonces alterar el significado de la consulta, por ejemplo para eludir un formulario de autenticación o leer datos que no debería ver.

La actividad busca localizar páginas de administración expuestas, como las rutas `/admin/admin_login.asp` y sus variantes, y evaluar si son vulnerables. El objetivo declarado es identificar vulnerabilidades y justificar la necesidad de reforzar la seguridad.

## 2. Objetivo

Identificar un patrón de vulnerabilidad de inyección SQL en formularios de autenticación y proponer medidas para corregirlo.

## 3. Marco teórico

- **Clasificación.** Inyección es la categoría **A03:2021** del OWASP Top 10.
- **Tríada CIA.** Una inyección exitosa compromete la **confidencialidad** (lectura de datos) y la **integridad** (modificación o borrado de datos).
- **Modelo de riesgo.** $R = P(\text{amenaza explota vulnerabilidad}) \times I(\text{impacto})$. La presencia de una ruta de administración expuesta aumenta $P$.

## 4. Entorno

### 4.1 Entorno del documento original

| Elemento | Descripción |
|---|---|
| **Navegador** | Google Chrome en macOS |
| **Objetivo** | Portal público de un gobierno municipal, en producción |
| **Resultado** | El sitio fue el único al que se pudo acceder. En otros intentos la acción fue detectada por el firewall, se mostraron restricciones y advertencias, y la IP fue marcada como amenaza |

Este entorno no es válido para la práctica. Las pruebas de inyección solo deben hacerse en sistemas propios, en laboratorios o en plataformas diseñadas para practicar.

### 4.2 Entorno recomendado para repetir la práctica

| Laboratorio | Uso |
|---|---|
| **DVWA**, módulo *SQL Injection* | Consulta vulnerable con distintos niveles de seguridad |
| **OWASP Juice Shop** | Aplicación con múltiples vulnerabilidades, incluida la inyección |
| **bWAPP** | Colección de vulnerabilidades web para práctica |

Se pueden desplegar con Docker, igual que en la práctica de ataque de diccionario, para mantenerlas aisladas de la red.

## 5. Procedimiento general (defensivo)

1. Identificar las rutas de autenticación y de administración de la aplicación de laboratorio.
2. Enviar entradas de prueba en los campos del formulario y observar cambios en la respuesta: mensajes de error de base de datos, diferencias de longitud o comportamiento inesperado.
3. Documentar qué parámetro es vulnerable y qué tipo de consulta lo procesa.
4. Proponer la corrección y verificar que la entrada maliciosa ya no altera la consulta.

*[Pendiente de completar con datos del PDF: rutas probadas, tipo de respuesta observada en cada intento y cualquier resultado distinto a los descritos en la sección 6.]*

## 6. Resultados observados

- Solo uno de los sitios probados permitió el acceso. En los demás, los mecanismos de defensa bloquearon la actividad.
- Las medidas de detección (firewall, bloqueo de IP, advertencias) respondieron antes de confirmar una vulnerabilidad. Esto muestra que la defensa perimetral puede detectar actividad de prueba, aunque no siempre impide que una aplicación mal programada sea vulnerable.

## 7. Conclusiones

*[Pendiente: transcribir las conclusiones del documento original.]*

## 8. Medidas de mitigación

- **Consultas parametrizadas o preparadas.** Separan los datos de la lógica SQL. Es la medida principal.
- **Validación de entrada** con listas blancas, según el formato esperado de cada campo.
- **Mínimo privilegio.** La cuenta de la aplicación debe tener solo los permisos que necesita.
- **Mensajes de error genéricos.** No deben mostrar detalles de la base de datos al usuario.
- **Firewall de aplicaciones web (WAF)** como capa adicional, nunca como sustituto de corregir el código.
- **Pruebas periódicas** de seguridad sobre la aplicación propia.

## 9. Consideraciones éticas y legales

- Probar la seguridad de un sistema ajeno sin autorización escrita puede constituir un delito, aunque la intención sea académica.
- El hallazgo de una vulnerabilidad en un sistema real debe reportarse al responsable del sistema por un canal de divulgación responsable, no publicarse.
- Las capturas de pantalla de sistemas ajenos no deben incluirse en un repositorio público.

## 10. Archivos de esta carpeta

- `readme.md`: este documento.
- `Inyección SQL.pdf`: informe original. *(Debe colocarse en esta misma carpeta.)*
