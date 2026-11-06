# Bitácora 1: Análisis y Pruebas del Algoritmo de Euclides (MCD)

Este repositorio contiene la implementación en Python, las pruebas unitarias, la validación diferencial y los scripts del experimento reproducible para el **Algoritmo de Euclides (MCD)**, correspondiente a la Bitácora 1 del curso *Análisis y Diseño de Algoritmos* (Cohorte X2026-III).

---

## Estructura del Repositorio

* `mcd_algoritmo.py` - Implementación base del algoritmo de Euclides, prueba interactiva, demostración del peor caso (Sucesión de Fibonacci / Teorema de Lamé) y prueba diferencial contra `math.gcd`.
* `test_mcd.py` - Pruebas unitarias (`unittest`).
* `datos_experimento.py` - Experimento empírico de conteo de iteraciones y cálculo de la razón T(2n)/T(n).
* `grafica_euclides.py` - Script en Python para generar los gráficos en escala normal y log-log.
* `mcd_prueba_diferencial_grafica.py` - Script en Python para generar la gráfica de la prueba diferencial.
* `requirements.txt` - Lista de dependencias del entorno.

---

## Requisitos del Entorno

* **Lenguaje:** Python 3.10+
* **Librerías principales:** `matplotlib` (para la generación de gráficas).

### Instalación de dependencias

```bash
pip install -r requirements.txt
 Comandos de Ejecución Exáctos
1. Ejecutar Algoritmo Principal, Demostración de FibonacciBashpython y Prueba DiferencialBashpython  mcd_algoritmo.py
2. Ejecutar Pruebas Unitarias  test_mcd.py
3. Generar Gráfica de Prueba Diferencial mcd_prueba_diferencial_grafica.py
4. Ejecutar Experimento Reproducible (Tablas y Mediciones)Bashpython datos_experimento.py
5. Generar Gráficas (Escala Normal y Log-Log)Bashpython grafica_euclides.py.py
⚙️ Configuración de Reproducibilidad 
Para garantizar que los resultados de las mediciones y pruebas sean idénticos a los reportados en el informe, se utilizó una semilla fija en la generación de números aleatorios:Semilla asignada: 2026 (Prueba diferencial) / 42 (Experimento empírico)Medición de costo: Conteo directo de operaciones iterativas (operación % del bucle while) para eliminar la varianza del sistema operativo.Tamaños de entrada ($n$): [1000, 2000, 4000, 8000, 16000, 32000]Repeticiones: 5 por tamaño de entrada, tomando la mediana como estadístico representativo.