import math
import random
import time

def mcd_euclides(a, b):
    a, b = abs(a), abs(b)
    iteraciones = 0
    while b != 0:
        a, b = b, a % b
        iteraciones += 1
    return a, iteraciones

def solicitar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada invalida. Introduce un entero.")

def ejecutar_prueba_diferencial(cantidad_pruebas=10000):
    errores = 0
    t_euclides, t_math = 0.0, 0.0
    random.seed(2026)

    for _ in range(cantidad_pruebas):
        n1 = random.randint(-100000, 100000)
        n2 = random.randint(-100000, 100000)
        
        inicio = time.perf_counter()
        res_propio, _ = mcd_euclides(n1, n2)
        t_euclides += time.perf_counter() - inicio
        
        inicio = time.perf_counter()
        res_math = math.gcd(n1, n2)
        t_math += time.perf_counter() - inicio
        
        if res_propio != res_math:
            errores += 1

    print(f"Pruebas: {cantidad_pruebas} | Errores: {errores}")
    print(f"T. Euclides: {t_euclides:.6f}s | T. Math: {t_math:.6f}s")

def demostrar_peor_caso_fibonacci(n):
    if n < 3:
        return
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    x, y, pasos = b, a, 0
    while y > 0:
        x, y, pasos = y, x % y, pasos + 1
    print(f"MCD Fibonacci (n={n}): {x} | Pasos: {pasos} (Lamé: {n - 2})")

if __name__ == "__main__":
    num1 = solicitar_entero("Primer numero: ")
    num2 = solicitar_entero("Segundo numero: ")
    resultado, it = mcd_euclides(num1, num2)
    print(f"MCD: {resultado} (Iteraciones: {it})")

    ejecutar_prueba_diferencial(10000)
    demostrar_peor_caso_fibonacci(11)
