import matplotlib.pyplot as plt

# Datos del experimento
n_vals = [1000, 2000, 4000, 8000, 16000, 32000]
medianas = [4, 5, 6, 8, 7, 8]

# 1. Gráfica en Escala Normal
plt.figure(figsize=(8, 5))
plt.plot(n_vals, medianas, marker='o', linestyle='-', color='b', linewidth=2, markersize=6)
plt.title('Algoritmo de Euclides - Crecimiento en Escala Normal', fontsize=12, fontweight='bold')
plt.xlabel('Tamaño de entrada (n)', fontsize=10)
plt.ylabel('Mediana de Iteraciones (Operaciones)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(n_vals)
plt.tight_layout()
plt.savefig('grafica_normal.png', dpi=300)
plt.show()

# 2. Gráfica en Escala Log-Log
plt.figure(figsize=(8, 5))
plt.loglog(n_vals, medianas, marker='s', linestyle='-', color='r', linewidth=2, markersize=6, base=2)
plt.title('Algoritmo de Euclides - Crecimiento en Escala Log-Log', fontsize=12, fontweight='bold')
plt.xlabel('Tamaño de entrada (log2 n)', fontsize=10)
plt.ylabel('Mediana de Iteraciones (log2 T(n))', fontsize=10)
plt.grid(True, which="both", linestyle='--', alpha=0.6)
plt.xticks(n_vals, labels=[str(x) for x in n_vals])
plt.yticks(medianas, labels=[str(x) for x in medianas])
plt.tight_layout()
plt.savefig('grafica_loglog.png', dpi=300)
plt.show()