# Práctica: AEE y cifrado de Hill

Implementación en Python (sólo biblioteca estándar) del Algoritmo Extendido de Euclides, el cálculo de inversos modulares y el cifrado de Hill 2×2 sobre Z₂₆, con los ejercicios resueltos y un documento de desarrollo.

## Contenido

```
practica_aee_hill/
├── README.md
├── .gitignore
├── docs/
│   └── practica_aee_hill.docx     # descripción, lógica, ecuaciones y ejecución
├── src/
│   └── aee_hill.py                # AEE, inversos, Hill y ejecución de ejercicios
└── tests/
    └── test_aee_hill.py           # pruebas unitarias
```

## Requisitos

Python 3.8 o superior. No requiere dependencias externas.

## Uso

Ejecutar los ejercicios:

```bash
python3 src/aee_hill.py
```

Ejecutar las pruebas:

```bash
python3 -m unittest discover -s tests -v
```

## Ejercicios

### 1. AEE(a, m)

El Algoritmo Extendido de Euclides calcula el mcd de a y m y los coeficientes x, y de la identidad de Bézout `a·x + m·y = mcd(a, m)`. Si el mcd es 1, x mod m es el inverso de a módulo m.

| Ejercicio     | Inverso |
|---------------|---------|
| AEE(3, 7)     | 5       |
| AEE(7, 32)    | 23      |
| AEE(23, 120)  | 47      |
| AEE(13, 64)   | 5       |
| AEE(5, 44)    | 9       |

### 2. Cifrado de Hill 2×2

Las letras se convierten a A = 0 … Z = 25. La clave de 4 letras se lee por filas como matriz 2×2 y el mensaje se procesa en bloques de dos letras.

- **Cifrar** M = PEAR con K = EAFB: `C = K·M mod 26` → **IBAR**.
- **Descifrar** C = ZLXD con K = KCDB: la matriz tiene det = 4, y mcd(4, 26) = 2, por lo que no es invertible módulo 26. Además, ningún bloque de M produce ZL ni XD con esa clave (la primera fila de K sólo genera valores pares). El script lo verifica por fuerza bruta. **No existe solución única.**

## Supuestos

- La clave de Hill se lee por filas. Si se leyera por columnas, el cifrado de PEAR con EAFB daría CEHR.
- El relleno para mensajes de longitud impar es la letra X.

## Autoría

Jessica Melani Romero Lora
