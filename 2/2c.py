import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Obtener la media, mediana y moda de cada columna seleccionada
columnas = ['redshift', 'u', 'alpha']

# Cálculo de media, mediana y moda usando pandas y scipy
for col in columnas:
    media = dataset_filtrado[col].mean()
    mediana = dataset_filtrado[col].median()
    moda = stats.mode(dataset_filtrado[col])[0]
    print(f"--- {col} ---")
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print()

# Graficar diagramas de cajas y bigotes (boxplots) para las tres columnas
plt.figure(figsize=(10, 6))
dataset_filtrado.boxplot(column=columnas)
plt.title('Diagrama de cajas y bigotes para Redshift, Magnitud u, Alpha')
plt.ylabel('Valores')
plt.grid(True)
plt.show()