# Cifrados César y Vigenère

| | |
|---|---|
| **Asignatura** | Ciberseguridad |
| **Programa** | Maestría en Inteligencia Artificial |
| **Institución** | Universidad Politécnica Metropolitana del Estado de Hidalgo (UPMH) |
| **Línea de investigación** | Automatización de Procesos Aplicados a la Ingeniería |
| **Alumna** | Jessica Melani Romero Lora |
| **Profesor** | Dr. Antonio Cedillo Hernández |
| **Periodo** | 2026 |
| **Actividad** | Cifrados César y Vigenère |
| **Documento** | `practica_cifrados_cesar_vigenere.docx` |
| **Fecha** | 22 de octubre de 2026 |
| **Entorno** | Cálculo manual y verificación con el alfabeto de 26 letras |

---

> ⚠️ **AVISO DE SEGURIDAD Y USO ACADÉMICO**
>
> - Este documento forma parte de una **práctica de la Maestría en Inteligencia Artificial de la UPMH**. Su contenido tiene **fines exclusivamente académicos y educativos**.
> - Los cifrados César y Vigenère son **técnicas históricas e inseguras**. No deben usarse para proteger información real. Su estudio sirve para entender el análisis de cifrados, no para aplicarlos en sistemas.
> - Este documento y su contenido están **protegidos como documentos académicos**. Se prohíbe su reproducción, distribución o uso total o parcial sin autorización de la autora.

---

## 1. Descripción técnica

La práctica cifra y descifra cuatro textos con dos algoritmos clásicos de sustitución:

- **Cifrado César**, monoalfabético: cada letra se desplaza el mismo número de posiciones.
- **Cifrado de Vigenère**, polialfabético: cada letra se desplaza según una letra de una clave que se repite.

En los ejercicios 1 y 3 se conoce el mensaje en claro $M$ y se calcula el texto cifrado $C$. En los ejercicios 2 y 4 se conoce $C$ y se calcula $M$.

| No. | Cifrado | Datos | Incógnita |
|---|---|---|---|
| 1 | César | M = MEXICANFLAG, K = 6 | C |
| 2 | César | C = SLALHV, K = 30 | M |
| 3 | Vigenère | M = WINDOWS, K = UNIX | C |
| 4 | Vigenère | C = LJEHDV, K = GOL | M |

## 2. Objetivo

Aplicar las ecuaciones de cifrado y descifrado de César y Vigenère, verificar los resultados y analizar qué tan legibles son, como criterio práctico para validar una clave.

## 3. Marco teórico

### 3.1 Cifrado César

- **Origen.** Se atribuye a Julio César, quien según Suetonio usaba un desplazamiento de 3 posiciones en su correspondencia militar.
- **Lógica.** Cada letra se convierte en su índice dentro del alfabeto ($A = 0 \dots Z = 25$), se desplaza $K$ posiciones y el resultado se reduce módulo 26.
- **Debilidad.** Solo existen 25 claves distintas, por lo que puede probarse cada una.

### 3.2 Cifrado de Vigenère

- **Origen.** Giovan Battista Bellaso describió la técnica en 1553, aunque se atribuye a Blaise de Vigenère. Se consideró indescifrable durante siglos, hasta que Friedrich Kasiski publicó en 1863 un método para estimar la longitud de la clave a partir de repeticiones en el texto cifrado.
- **Lógica.** La clave alfabética se repite cíclicamente hasta igualar la longitud del mensaje. Cada posición usa un desplazamiento distinto, lo que aplana la distribución de frecuencias frente al César simple.

## 4. Ecuaciones

Sea $x$ el índice de una letra, con $x \in \{0, 1, \dots, 25\}$.

**César:**

$$
C_i = (M_i + K) \bmod 26, \qquad M_i = (C_i - K) \bmod 26, \qquad K \equiv K \pmod{26}
$$

**Vigenère:**

$$
K_i = k[(i - 1) \bmod m], \qquad C_i = (M_i + K_i) \bmod 26, \qquad M_i = (C_i - K_i) \bmod 26
$$

donde $m$ es la longitud de la clave. Cuando la resta es negativa, se suma 26 antes de aplicar el módulo. Por ejemplo, $(2 - 4) \bmod 26 = 24$.

## 5. Ejecución

### 5.1 Ejercicio 1: César, M = MEXICANFLAG, K = 6

Se aplica $C_i = (M_i + 6) \bmod 26$ a cada letra.

| Pos. | Letra M | Índice M | Suma (+6) | mod 26 | Letra C |
|---|---|---|---|---|---|
| 1 | M | 12 | 18 | 18 | S |
| 2 | E | 4 | 10 | 10 | K |
| 3 | X | 23 | 29 | 3 | D |
| 4 | I | 8 | 14 | 14 | O |
| 5 | C | 2 | 8 | 8 | I |
| 6 | A | 0 | 6 | 6 | G |
| 7 | N | 13 | 19 | 19 | T |
| 8 | F | 5 | 11 | 11 | L |
| 9 | L | 11 | 17 | 17 | R |
| 10 | A | 0 | 6 | 6 | G |
| 11 | G | 6 | 12 | 12 | M |

**Resultado: C = SKDOIGTLRGM**

### 5.2 Ejercicio 2: César, C = SLALHV, K = 30

Como $30 \equiv 4 \pmod{26}$, se aplica $M_i = (C_i - 4) \bmod 26$.

| Pos. | Letra C | Índice C | Resta (−4) | mod 26 | Letra M |
|---|---|---|---|---|---|
| 1 | S | 18 | 14 | 14 | O |
| 2 | L | 11 | 7 | 7 | H |
| 3 | A | 0 | −4 | 22 | W |
| 4 | L | 11 | 7 | 7 | H |
| 5 | H | 7 | 3 | 3 | D |
| 6 | V | 21 | 17 | 17 | R |

**Resultado: M = OHWHDR**

**Observación.** Con $K = 3$ el mismo texto produce **PIXIES**, una palabra legible. Esto sugiere que la clave pretendida pudo ser 3 y no 30. Este punto debe confirmarse con quien planteó el ejercicio.

### 5.3 Ejercicio 3: Vigenère, M = WINDOWS, K = UNIX

La clave extendida para 7 letras es `UNIXUNI`. Se aplica $C_i = (M_i + K_i) \bmod 26$.

| Pos. | M | Índice M | Clave | Índice K | Suma | mod 26 | C |
|---|---|---|---|---|---|---|---|
| 1 | W | 22 | U | 20 | 42 | 16 | Q |
| 2 | I | 8 | N | 13 | 21 | 21 | V |
| 3 | N | 13 | I | 8 | 21 | 21 | V |
| 4 | D | 3 | X | 23 | 26 | 0 | A |
| 5 | O | 14 | U | 20 | 34 | 8 | I |
| 6 | W | 22 | N | 13 | 35 | 9 | J |
| 7 | S | 18 | I | 8 | 26 | 0 | A |

**Resultado: C = QVVAIJA**

### 5.4 Ejercicio 4: Vigenère, C = LJEHDV, K = GOL

La clave extendida para 6 letras es `GOLGOL`. Se aplica $M_i = (C_i - K_i) \bmod 26$, sumando 26 cuando la resta es negativa.

| Pos. | C | Índice C | Clave | Índice K | Resta | mod 26 | M |
|---|---|---|---|---|---|---|---|
| 1 | L | 11 | G | 6 | 5 | 5 | F |
| 2 | J | 9 | O | 14 | −5 | 21 | V |
| 3 | E | 4 | L | 11 | −7 | 19 | T |
| 4 | H | 7 | G | 6 | 1 | 1 | B |
| 5 | D | 3 | O | 14 | −11 | 15 | P |
| 6 | V | 21 | L | 11 | 10 | 10 | K |

**Resultado: M = FVTBPK**

**Observación.** Los cálculos son correctos respecto a la clave dada, pero el resultado no es legible. Es probable que la clave o el texto cifrado original sean distintos de los indicados en el enunciado.

## 6. Análisis de resultados

| Ejercicio | Operación | Resultado | Estado |
|---|---|---|---|
| 1. César | $C = (M + 6) \bmod 26$ | SKDOIGTLRGM | Verificado |
| 2. César | $M = (C - 4) \bmod 26$ | OHWHDR | Verificado; con K = 3 se obtiene PIXIES |
| 3. Vigenère | $C = (M + K_i) \bmod 26$ | QVVAIJA | Verificado |
| 4. Vigenère | $M = (C - K_i) \bmod 26$ | FVTBPK | No legible; revisar clave o texto |

Los ejercicios 1 y 3 son consistentes con las ecuaciones. Los ejercicios 2 y 4 se calcularon correctamente, pero el resultado del ejercicio 2 solo es legible con $K = 3$, y el del ejercicio 4 no es legible con la clave dada.

## 7. Conclusiones

- El cifrado César es sencillo de aplicar y de romper, porque solo existen 25 claves distintas que probar.
- El cifrado de Vigenère amplía el espacio de búsqueda y dificulta el análisis de frecuencias, porque cada posición usa un desplazamiento distinto.
- La legibilidad del resultado es el criterio práctico para validar una clave. Los ejercicios 2 y 4 deben revisarse con quien planteó el reto antes de darlos por cerrados.

## 8. Archivos de esta carpeta

- `practica_cifrados_cesar_vigenere.docx`: versión editable en Word de la práctica. *(Debe colocarse en esta misma carpeta.)*
- `readme.md`: este documento.
