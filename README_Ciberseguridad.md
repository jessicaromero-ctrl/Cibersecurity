<p align="center">
  <img src="https://img.shields.io/badge/Maestr%C3%ADa-Inteligencia%20Artificial-333333?style=for-the-badge" alt="Maestría en IA"/>
  <img src="https://img.shields.io/badge/UPMH-Ciberseguridad-555555?style=for-the-badge" alt="Ciberseguridad"/>
  <img src="https://img.shields.io/badge/Formato-PDF-777777?style=for-the-badge" alt="Formato PDF"/>
</p>

<h1 align="center">Ciberseguridad</h1>

<p align="center">
  <strong>Universidad Politécnica Metropolitana del Estado de Hidalgo</strong><br/>
  Maestría en Inteligencia Artificial<br/>
  Línea de investigación: <em>Automatización de Procesos Aplicados a la Ingeniería</em>
</p>

<p align="center">
  <strong>Alumna:</strong> Jessica Melani Romero Lora<br/>
  <strong>Profesor:</strong> Dr. Antonio Cedillo Hernández<br/>
  <strong>Periodo:</strong> 2026
</p>

---

## Acerca del Repositorio

Este repositorio reúne las actividades y reportes desarrollados para la materia **Ciberseguridad** de la Maestría en Inteligencia Artificial de la UPMH. El trabajo se enmarca en la línea de investigación **Automatización de Procesos Aplicados a la Ingeniería**, donde la seguridad de la información es un requisito transversal: todo proceso automatizado (sistemas de control, plataformas de datos, aplicaciones web, modelos de IA en producción) depende de que sus datos y sus credenciales mantengan **confidencialidad, integridad y disponibilidad**.

Las actividades se abordan desde un enfoque de **seguridad ofensiva con fines educativos y defensivos**: se estudia cómo funciona cada ataque para modelarlo matemáticamente, medir su efectividad y diseñar contramedidas. Toda práctica se realiza en entornos controlados, de laboratorio o sobre datos propios.

---

## Fundamentos Teóricos

### Modelo base de seguridad y riesgo

La **tríada CIA** define los objetivos de protección: Confidencialidad, Integridad y Disponibilidad. El riesgo asociado a una amenaza se cuantifica como:

$$R = P(\text{amenaza explota vulnerabilidad}) \times I(\text{impacto})$$

Un control de seguridad es efectivo cuando reduce $P$, $I$ o ambos. Las tres actividades del repositorio ilustran tres superficies de ataque distintas: la **capa de aplicación** (inyección SQL), la **capa de autenticación** (ataque de diccionario) y el **canal encubierto de datos** (esteganografía).

### Autenticación: entropía, espacio de claves y ataque de diccionario

**Espacio de búsqueda.** Para una contraseña de longitud $L$ construida sobre un alfabeto de $N$ símbolos, el espacio de claves es:

$$|K| = N^{L}$$

**Entropía de la contraseña** (Shannon, 1948), en bits, suponiendo selección uniforme:

$$H = L \cdot \log_2 N$$

**Tiempo esperado de fuerza bruta**, con tasa de intentos $v$ (hashes por segundo): en promedio se recorre la mitad del espacio,

$$\mathbb{E}[T_{\text{fb}}] = \frac{N^{L}}{2v}$$

**Ataque de diccionario.** En la práctica las contraseñas humanas no son uniformes: se concentran en un conjunto reducido de palabras y variantes. Sea $D$ un diccionario ordenado por probabilidad decreciente $p_1 \ge p_2 \ge \dots \ge p_{|D|}$ y $r$ el número promedio de reglas de mutación aplicadas a cada palabra (sufijos numéricos, sustituciones tipo *leet*, mayúsculas). El tamaño efectivo y el tiempo del ataque son:

$$|D_{\text{ef}}| = |D| \cdot r, \qquad T_{\text{dic}} = \frac{|D| \cdot r}{v}$$

**Probabilidad de éxito tras $k$ intentos:**

$$P_{\text{éxito}}(k) = \sum_{i=1}^{k} p_i$$

**Esfuerzo esperado de adivinación** (*guesswork*, Massey, 1994), que mide el número medio de intentos con la estrategia óptima:

$$G = \sum_{i=1}^{|D|} i \cdot p_i$$

**Efecto de la sal criptográfica.** Si el sistema almacena $h = H(\text{sal} \,\|\, \text{contraseña})$ con sal única por usuario, el atacante no puede reutilizar cálculos entre cuentas y el costo de comprometer $U$ usuarios pasa de $T_{\text{dic}}$ a:

$$T_{\text{sal}} = U \cdot \frac{|D| \cdot r}{v}$$

**Costo de derivación de clave.** Con funciones de estiramiento (bcrypt, scrypt, Argon2, PBKDF2) que ejecutan $c$ iteraciones, la tasa efectiva se reduce a $v' = v / c$, lo que multiplica por $c$ el tiempo del atacante.

### Esteganografía digital

La esteganografía oculta la **existencia** del mensaje (a diferencia de la criptografía, que oculta su **contenido**). En el método de **bit menos significativo (LSB)**, cada bit $m_i$ del mensaje reemplaza el LSB del $i$-ésimo valor de píxel $s_i$ de la imagen portadora:

$$s_i' = 2\left\lfloor \frac{s_i}{2} \right\rfloor + m_i, \qquad m_i \in \{0,1\}$$

**Capacidad de inserción** para una imagen de $W \times H$ píxeles con $c$ canales y $k$ bits por canal:

$$C = W \cdot H \cdot c \cdot k \quad \text{bits}$$

**Métricas de imperceptibilidad.** Error cuadrático medio entre la portadora $I$ y la imagen estego $K$ (de tamaño $M \times N$):

$$\text{MSE} = \frac{1}{MN}\sum_{x=1}^{M}\sum_{y=1}^{N}\left[I(x,y) - K(x,y)\right]^2$$

Relación señal-ruido pico, con $\text{MAX}_I = 255$ para imágenes de 8 bits:

$$\text{PSNR} = 10 \cdot \log_{10}\!\left(\frac{\text{MAX}_I^{2}}{\text{MSE}}\right) \ \text{dB}$$

Valores de PSNR por encima de ~40 dB suelen considerarse visualmente imperceptibles. Como complemento perceptual se usa el índice SSIM (Wang et al., 2004).

**Estegoanálisis por chi-cuadrada** (Westfeld y Pfitzmann, 2000). La inserción LSB tiende a igualar las frecuencias de los pares de valores $(2i,\,2i+1)$. Con $n_j$ la frecuencia del valor $j$ y $\bar{n}_i = \tfrac{n_{2i} + n_{2i+1}}{2}$:

$$\chi^2 = \sum_{i=1}^{127} \frac{\left(n_{2i} - \bar{n}_i\right)^2}{\bar{n}_i}$$

Un valor de $\chi^2$ bajo (p-valor alto) es indicio de contenido oculto.

### Inyección SQL

Una consulta construida por **concatenación** de entrada del usuario $x$ puede formalizarse como:

$$q(x) = \text{prefijo} \;\|\; x \;\|\; \text{sufijo}$$

La aplicación supone que $x$ es **dato**, pero si $x$ contiene metacaracteres del lenguaje, el analizador sintáctico de la base de datos puede interpretarlo como **código**. Existe inyección cuando la estructura sintáctica de la consulta depende de la entrada:

$$\exists\, x:\ \text{AST}\big(q(x)\big) \neq \text{AST}\big(q(x_{\text{legítima}})\big)$$

La defensa principal elimina esa dependencia. Con **consultas parametrizadas** la estructura se compila de forma independiente del valor, y se cumple por construcción:

$$\forall\, x:\ \text{AST}\big(q_{\text{param}}(x)\big) = \text{AST}\big(q_{\text{param}}(x_{\text{legítima}})\big)$$

**Cuantificación del riesgo** por punto de entrada $e$ de la aplicación:

$$R_{\text{SQLi}} = \sum_{e \in E} P(\text{vuln}_e) \cdot I(\text{datos expuestos}_e)$$

**Contramedidas** (defensa en profundidad): consultas parametrizadas o *prepared statements*, validación y normalización de entradas, principio de mínimo privilegio en la cuenta de base de datos, manejo de errores sin información interna y monitoreo (WAF y registros de auditoría).

---

## Relevancia en Automatización de Procesos de Ingeniería

| Área de aplicación | Riesgo asociado | Actividad relacionada |
|---|---|---|
| **Aplicaciones web y sistemas de información** | Exfiltración o alteración de bases de datos por entradas no saneadas | Inyección SQL |
| **Autenticación en plataformas industriales y de datos** | Compromiso de cuentas por contraseñas débiles o hashes expuestos | Ataque de diccionario |
| **Protección de propiedad intelectual y trazabilidad** | Canales encubiertos de fuga de datos; marcado de autoría en medios digitales | Esteganografía |
| **Pipelines de IA y MLOps** | Credenciales de servicios, datos de entrenamiento y modelos como activos a proteger | Transversal |
| **Sistemas de control y automatización** | Un proceso automatizado vulnerable es una vía de ataque a la operación física | Transversal |

La automatización incrementa el alcance de un sistema, pero también el de cualquier fallo de seguridad. Por ello, la formación en ciberseguridad con enfoque cuantitativo (entropía, probabilidades de éxito, métricas de detección) permite **diseñar controles medibles** y no solo reactivos.

---

## Estructura del Repositorio

```
ciberseguridad/
├── README.md
├── Inyección SQL.pdf
├── Ataque de Diccionario.pdf
├── Act. 3 Esteganografía.pdf
└── ...            # Actividades futuras
```

---

## Desglose de Actividades

### Inyección SQL

**Archivo:** `Inyección SQL.pdf`

Estudio de la vulnerabilidad de inyección SQL como fallo de separación entre código y datos en la capa de aplicación.

- Mecanismo de la vulnerabilidad y formalización de la consulta $q(x)$.
- Clasificación general de los ataques de inyección y su impacto sobre la tríada CIA.
- Contramedidas: consultas parametrizadas, validación de entradas, mínimo privilegio y manejo de errores.
- Marco matemático: dependencia estructural del AST y riesgo $R_{\text{SQLi}}$.

---

### Ataque de Diccionario

**Archivo:** `Ataque de Diccionario.pdf`

Análisis de ataques contra mecanismos de autenticación basados en contraseñas.

- Diferencia entre fuerza bruta y ataque de diccionario.
- Modelado con entropía $H = L\log_2 N$, espacio de claves y tiempo esperado $T_{\text{dic}}$.
- Reglas de mutación y probabilidad de éxito acumulada $P_{\text{éxito}}(k)$.
- Contramedidas: políticas de contraseñas, sal criptográfica, funciones de derivación lentas (Argon2, bcrypt), límite de intentos y autenticación multifactor.

---

### Actividad 3 — Esteganografía

**Archivo:** `Act. 3 Esteganografía.pdf`

Estudio de la ocultación de información en medios digitales.

- Distinción entre esteganografía y criptografía.
- Técnica LSB, capacidad de inserción $C$ y compromiso entre capacidad e imperceptibilidad.
- Evaluación de calidad con MSE y PSNR.
- Estegoanálisis estadístico (chi-cuadrada) y su papel en la detección.

---

## Cómo Agregar Nuevas Actividades

1. Subir el archivo del reporte a la raíz del repositorio (o a una carpeta por actividad).
2. Añadir una sección en **Desglose de Actividades** con archivo, contenido y marco matemático.
3. Si la actividad introduce un modelo nuevo, agregarlo en **Fundamentos Teóricos**.
4. Actualizar el árbol de **Estructura del Repositorio**.

---

## Aviso de Uso Responsable

El material de este repositorio tiene fines **estrictamente académicos y defensivos**. Las técnicas descritas deben aplicarse únicamente en entornos de laboratorio, sistemas propios o con autorización expresa por escrito. El uso no autorizado contra sistemas de terceros puede constituir un delito.

---

## Referencias

1. Shannon, C.E. (1948). A Mathematical Theory of Communication. *Bell System Technical Journal*, 27(3), 379–423.
2. Massey, J.L. (1994). Guessing and Entropy. *Proc. IEEE International Symposium on Information Theory*, 204.
3. Bonneau, J. (2012). The Science of Guessing: Analyzing an Anonymized Corpus of 70 Million Passwords. *IEEE Symposium on Security and Privacy*, 538–552.
4. Grassi, P. et al. (2017). *NIST Special Publication 800-63B: Digital Identity Guidelines — Authentication and Lifecycle Management*. NIST.
5. Halfond, W., Viegas, J. & Orso, A. (2006). A Classification of SQL-Injection Attacks and Countermeasures. *Proc. IEEE International Symposium on Secure Software Engineering*.
6. OWASP Foundation. *OWASP Top 10 – Web Application Security Risks*. https://owasp.org/www-project-top-ten/
7. Westfeld, A. & Pfitzmann, A. (2000). Attacks on Steganographic Systems. *Information Hiding, LNCS 1768*, 61–76.
8. Provos, N. & Honeyman, P. (2003). Hide and Seek: An Introduction to Steganography. *IEEE Security & Privacy*, 1(3), 32–44.
9. Wang, Z., Bovik, A.C., Sheikh, H.R. & Simoncelli, E.P. (2004). Image Quality Assessment: From Error Visibility to Structural Similarity. *IEEE Trans. Image Processing*, 13(4), 600–612.
10. Stallings, W. (2017). *Cryptography and Network Security: Principles and Practice*. 7th ed. Pearson.

---

<p align="center">
  <em>Universidad Politécnica Metropolitana del Estado de Hidalgo — Maestría en Inteligencia Artificial — 2026</em>
</p>
