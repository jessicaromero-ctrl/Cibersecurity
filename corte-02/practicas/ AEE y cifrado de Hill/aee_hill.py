#!/usr/bin/env python3
"""
Algoritmo Extendido de Euclides (AEE) y cifrado de Hill 2x2 sobre Z_26.

Uso:
    python3 src/aee_hill.py
"""

from math import gcd

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MODULO = 26


# --- Algoritmo Extendido de Euclides -------------------------------------

def aee(a, b):
    """Devuelve (mcd, x, y, pasos) tal que a*x + b*y = mcd.

    Cada paso es (r_anterior, r_actual, cociente, residuo).
    """
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    pasos = []
    while r1 != 0:
        q = r0 // r1
        residuo = r0 - q * r1
        pasos.append((r0, r1, q, residuo))
        r0, r1 = r1, residuo
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return r0, s0, t0, pasos


def inverso_modular(a, m):
    """Inverso de a módulo m mediante AEE. Lanza ValueError si no existe."""
    mcd, x, _, _ = aee(a % m, m)
    if mcd != 1:
        raise ValueError(f"{a} no tiene inverso módulo {m} (mcd = {mcd})")
    return x % m


# --- Cifrado de Hill 2x2 --------------------------------------------------

def a_numeros(texto):
    """Convierte texto a índices A=0 ... Z=25, ignorando lo que no sea letra."""
    limpio = "".join(c for c in texto.upper() if c in ALFABETO)
    return [ALFABETO.index(c) for c in limpio]


def a_letras(numeros):
    return "".join(ALFABETO[n % MODULO] for n in numeros)


def matriz_2x2(clave):
    """Convierte una clave de 4 letras en matriz 2x2, leída por filas."""
    v = a_numeros(clave)
    if len(v) != 4:
        raise ValueError("La clave de Hill 2x2 debe tener exactamente 4 letras")
    return [[v[0], v[1]], [v[2], v[3]]]


def determinante(k):
    return (k[0][0] * k[1][1] - k[0][1] * k[1][0]) % MODULO


def cifrar_hill(mensaje, clave):
    """C = K·M (mod 26) por bloques de 2 letras. Rellena con X si la longitud es impar."""
    k = matriz_2x2(clave)
    v = a_numeros(mensaje)
    if len(v) % 2:
        v.append(ALFABETO.index("X"))
    salida = []
    for i in range(0, len(v), 2):
        x, y = v[i], v[i + 1]
        salida.append((k[0][0] * x + k[0][1] * y) % MODULO)
        salida.append((k[1][0] * x + k[1][1] * y) % MODULO)
    return a_letras(salida)


def descifrar_hill(cifrado, clave):
    """M = K⁻¹·C (mod 26). Requiere que det(K) sea invertible módulo 26."""
    k = matriz_2x2(clave)
    det = determinante(k)
    try:
        det_inv = inverso_modular(det, MODULO)
    except ValueError:
        raise ValueError(
            f"La matriz no es invertible módulo 26: det = {det}, "
            f"mcd(det, 26) = {gcd(det, MODULO)}"
        )
    adj = [[k[1][1], -k[0][1]], [-k[1][0], k[0][0]]]
    inv = [[(det_inv * adj[i][j]) % MODULO for j in range(2)] for i in range(2)]
    v = a_numeros(cifrado)
    if len(v) % 2:
        raise ValueError("El texto cifrado debe tener longitud par")
    salida = []
    for i in range(0, len(v), 2):
        x, y = v[i], v[i + 1]
        salida.append((inv[0][0] * x + inv[0][1] * y) % MODULO)
        salida.append((inv[1][0] * x + inv[1][1] * y) % MODULO)
    return a_letras(salida)


def preimagenes_hill(bloque_c, clave):
    """Todos los bloques M de 2 letras con K·M ≡ C (mod 26). Fuerza bruta: 676 casos."""
    k = matriz_2x2(clave)
    c = a_numeros(bloque_c)
    if len(c) != 2:
        raise ValueError("El bloque debe tener 2 letras")
    hallados = []
    for x in range(MODULO):
        for y in range(MODULO):
            if ((k[0][0] * x + k[0][1] * y) % MODULO == c[0]
                    and (k[1][0] * x + k[1][1] * y) % MODULO == c[1]):
                hallados.append(a_letras([x, y]))
    return hallados


# --- Ejecución de los ejercicios -----------------------------------------

def ejecutar_aee(pares):
    print("Ejercicio 1: AEE(a, m) = inverso de a módulo m")
    for a, m in pares:
        mcd, x, _, pasos = aee(a, m)
        inv = inverso_modular(a, m)
        print(f"  AEE({a},{m}): mcd = {mcd}, inverso = {inv}, "
              f"verificación: {a}·{inv} mod {m} = {(a * inv) % m}")
        for r0, r1, q, res in pasos:
            print(f"      {r0} = {q}·{r1} + {res}")


def ejecutar_hill():
    print("\nEjercicio 2: cifrado de Hill")
    m, k = "PEAR", "EAFB"
    print(f"  Encontrar C: M = {m}, K = {k}")
    print(f"      C = {cifrar_hill(m, k)}")

    c, k = "ZLXD", "KCDB"
    print(f"  Encontrar M: C = {c}, K = {k}")
    kk = matriz_2x2(k)
    det = determinante(kk)
    print(f"      det(K) = {det}, mcd(det, 26) = {gcd(det, MODULO)}")
    try:
        print(f"      M = {descifrar_hill(c, k)}")
    except ValueError as e:
        print(f"      Sin inversa: {e}")
    for i in range(0, len(c), 2):
        bloque = c[i:i + 2]
        sol = preimagenes_hill(bloque, k)
        print(f"      bloque {bloque}: {len(sol)} preimágenes {sol}")


if __name__ == "__main__":
    ejecutar_aee([(3, 7), (7, 32), (23, 120), (13, 64), (5, 44)])
    ejecutar_hill()
