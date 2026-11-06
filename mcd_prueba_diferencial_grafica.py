import math
import random
import time
import matplotlib.pyplot as plt # Importamos la librería para graficar

def mcd_euclides(a, b):
    """Implementación del Algoritmo de Euclides."""
    a, b = abs(a), abs(b)
    iteraciones = 0
    while b != 0:
        a, b = b, a % b
        iteraciones += 1
    return a, iteraciones

def ejecutar_prueba_diferencial(cantidad_pruebas=10000):
    """
    Prueba diferencial que además recolecta datos y grafica el 
    comportamiento del número de iteraciones frente al tamaño de la entrada.
    """
    print(f"🧪 Iniciando prueba diferencial con {cantidad_pruebas:,} casos...")
    
    errores_detectados = 0
    casos_probados = 0
    iteraciones_totales = 0  
    tiempo_euclides = 0.0
    tiempo_math_gcd = 0.0

    # LISTAS PARA ALMACENAR DATOS DE LA GRÁFICA
    lista_b = []           # Eje X: Guardaremos el menor de los números (el divisor b)
    lista_iteraciones = [] # Eje Y: Guardaremos cuántas iteraciones tomó ese caso

    random.seed(2026)

    for _ in range(cantidad_pruebas):
        num1 = random.randint(-100000, 100000)
        num2 = random.randint(-100000, 100000)
        
        # 1. Ejecutar y cronometrar la implementación
        inicio = time.perf_counter()
        resultado_propio, it_caso = mcd_euclides(num1, num2)
        tiempo_euclides += (time.perf_counter() - inicio)
        iteraciones_totales += it_caso  
        
        # GUARDAR DATOS PARA EL GRÁFICO (usamos valores absolutos)
        # Ponemos en b el menor de los dos para alinearlo con nuestra teoría n = log(b)
        v_b = min(abs(num1), abs(num2))
        if v_b > 0: # Evitamos el cero para que la gráfica limpie los extremos
            lista_b = lista_b + [v_b]
            lista_iteraciones = lista_iteraciones + [it_caso]

        # 2. Ejecutar y cronometrar la biblioteca estándar
        inicio = time.perf_counter()
        resultado_math = math.gcd(num1, num2)
        tiempo_math_gcd += (time.perf_counter() - inicio)
        
        # 3. Validación diferencial
        if resultado_propio != resultado_math:
            print(f"❌ ¡Discrepancia hallada! Entradas: ({num1}, {num2}) -> Propio: {resultado_propio} | Math: {resultado_math}")
            errores_detectados += 1
            
        casos_probados += 1

    iteraciones_promedio = iteraciones_totales / cantidad_pruebas

    # Resumen de resultados en consola (Tu código original)
    print("\n" + "="*40)
    print("📊 RESUMEN DE LA PRUEBA DIFERENCIAL")
    print("="*40)
    print(f"Casos totales evaluados: {casos_probados:,}")
    print(f"Casos exitosos (Coincidencia completa): {casos_probados - errores_detectados:,}")
    print(f"Errores / Discrepancias encontradas: {errores_detectados}")
    print("\n🔄 MÉTRICAS DEL BUCLE WHILE:")
    print(f"   • Número total de iteraciones:            {iteraciones_totales:,}")
    print(f"   • Promedio de iteraciones por cálculo:      {iteraciones_promedio:.2f}")
    print(f"\n⏱️ Estadísticas de rendimiento: Euclides ({tiempo_euclides:.6f}s) | Math ({tiempo_math_gcd:.6f}s)")

    # ==========================================
    # 📊 GRÁFICA PROFESIONAL CON HISTOGRAMA LATERAL
    # ==========================================
    print("\n🎨 Generando gráfica con histograma lateral...")
    
    # 1. Crear la figura y definir la cuadrícula (GridSpec)
    # 1 fila, 2 columnas. La primera columna es 4 veces más ancha que la segunda.
    fig = plt.figure(figsize=(13, 8))
    gs = fig.add_gridspec(1, 2, width_ratios=[4, 1], wspace=0.05)
    
    # Crear ambos paneles de dibujo
    ax_scatter = fig.add_subplot(gs[0, 0])
    ax_hist = fig.add_subplot(gs[0, 1], sharey=ax_scatter) # Comparten el eje Y
    
    # 2. PANEL PRINCIPAL: Gráfico de Dispersión y Cotas Teóricas
    # Datos empíricos aleatorios
    ax_scatter.scatter(lista_b, lista_iteraciones, color='#1f77b4', alpha=0.25, s=2.5, 
                       label='Casos aleatorios evaluados')
    
    # Curvas teóricas continuas
    import numpy as np
    b_teorico = np.linspace(2, max(lista_b), 1000)
    peor_caso = 2 * np.log2(b_teorico)
    caso_promedio = 0.843 * np.log(b_teorico)
    
    ax_scatter.plot(b_teorico, peor_caso, color='crimson', linewidth=2.5, 
                    label='Cota Superior Teórica: $O(\log_2 b)$')
    ax_scatter.plot(b_teorico, caso_promedio, color='forestgreen', linewidth=2, linestyle='--',
                    label='Comportamiento Promedio Teórico: $\Theta(\ln b)$')
    
    # Estilizado del panel principal
    ax_scatter.set_xlabel('Tamaño de la Entrada: Valor absoluto del divisor menor ($b$)', fontsize=11, labelpad=10)
    ax_scatter.set_ylabel('Costo Computacional: Número de iteraciones del bucle', fontsize=11, labelpad=10)
    ax_scatter.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax_scatter.grid(True, linestyle='--', alpha=0.4, color='gray')
    ax_scatter.legend(loc='upper left', fontsize=10, frameon=True, shadow=True).set_zorder(100)
    ax_scatter.set_ylim(0, max(lista_iteraciones) + 3)
    
     # ==========================================
    # 3. PANEL LATERAL: Histograma con Etiquetas Numéricas Exactas
    # ==========================================
    # Definimos contenedores fijos alineados con cada entero de iteración
    bins_fijos = np.arange(-0.5, max(lista_iteraciones) + 1.5, 1)
    
    # Dibujamos el histograma y guardamos los "patches" (las barras físicas)
    counts, bins, patches = ax_hist.hist(lista_iteraciones, bins=bins_fijos, orientation='horizontal', 
                                         color='#2ca02c', alpha=0.7, edgecolor='black', linewidth=0.5)
    
    # Añadir los valores numéricos exactos al final de cada barra
    for patch in patches:
        # Obtenemos el ancho de la barra (que representa el conteo de casos)
        ancho = patch.get_width()
        
        # Solo dibujamos la etiqueta si la barra tiene datos (mayor a cero)
        if ancho > 0:
            # Calculamos la coordenada central vertical (Y) de la barra actual
            y_pos = patch.get_y() + patch.get_height() / 2
            
            # Colocamos el texto formateado con separadores de miles
            # ancho * 1.03 le da un pequeño margen a la derecha para que no choque con el borde de la barra
            ax_hist.text(ancho * 1.03, y_pos, f"{int(ancho):,}", 
                         va='center', ha='left', fontsize=8.5, fontweight='bold', color='#2c3e50')
    
    # Ajustamos el límite del eje X del histograma un poco más allá para dar espacio a los textos
    ax_hist.set_xlim(0, max(counts) * 1.25)
    
    # Modificar las etiquetas del eje inferior (X) para que muestren "Miles" de forma limpia
    ax_hist.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{x/1000:.1f}k" if x > 0 else "0"))
    ax_hist.set_xlabel('Frecuencia (Miles de casos)', fontsize=11, labelpad=10)
    ax_hist.grid(True, linestyle=':', alpha=0.5, color='gray')
    
    # Ocultar las etiquetas del eje Y en el histograma ya que las comparte con el scatter
    plt.setp(ax_hist.get_yticklabels(), visible=False)

    
    # 4. TÍTULO GENERAL DE LA FIGURA MULTIPANEL
    fig.suptitle('Análisis Empírico de Complejidad y Distribución de Frecuencia: mcd_euclides(a, b)', 
                 fontsize=13, fontweight='bold', y=0.95)
    
    # Mostrar la interfaz unificada
    plt.show()

if __name__ == "__main__":
    # Reducimos a 20,000 para que la gráfica no sature tu memoria al renderizar tantos puntos flotantes,
    # pero manteniendo el volumen estadístico que deseas analizar.
    ejecutar_prueba_diferencial(cantidad_pruebas=20000)
