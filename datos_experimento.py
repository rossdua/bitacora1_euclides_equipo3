import random
import statistics

def mcd_conteo(a, b):
    """Calcula el MCD y cuenta las iteraciones (operaciones)."""
    iteraciones = 0
    while b != 0:
        a, b = b, a % b
        iteraciones += 1
    return iteraciones

# Configuración del experimento
random.seed(42)
dimension = [1000, 2000, 4000, 8000, 16000, 32000]
medianas_registradas = []

print("--- RESULTADOS DEL EXPERIMENTO (MCD) ---")
print(f"{'Tamaño (n)':<12} | {'Mediciones':<35} | {'Mediana (T(n))':<15} | {'Razón T(2n)/T(n)'}")
print("-" * 85)

for i, n in enumerate(dimension):
    mediciones = []
    for _ in range(5):
        a = random.randint(1, n)
        b = random.randint(1, n)
        if a < b:
            a, b = b, a
        ops = mcd_conteo(a, b)
        mediciones.append(ops)
    
    mediana = statistics.median(mediciones)
    medianas_registradas.append(mediana)
    
    # Calcular la razón T(2n) / T(n) si no es el primer elemento
    if i > 0:
        mediana_anterior = medianas_registradas[i - 1]
        # Evitar división por cero por seguridad
        if mediana_anterior != 0:
            razon = round(mediana / mediana_anterior, 2)
            razon_str = str(razon)
        else:
            razon_str = "N/A"
    else:
        razon_str = "—"
        
    print(f"{n:<12} | {str(mediciones):<35} | {mediana:<15} | {razon_str}")
