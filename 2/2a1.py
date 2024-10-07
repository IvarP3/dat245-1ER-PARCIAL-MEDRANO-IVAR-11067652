from google.colab import drive
drive.mount('/content/Drive')

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('/content/Drive/MyDrive/datos/star_classification.csv')

def calcular_percentil(datos, percentil):
    datos_ordenados = sorted(datos) 
    indice = int((percentil / 100) * len(datos_ordenados)) - 1
    return datos_ordenados[indice]

def calcular_cuartiles(datos):
    Q1 = calcular_percentil(datos, 25)  # Primer cuartil
    Q2 = calcular_percentil(datos, 50)  # Mediana o segundo cuartil
    Q3 = calcular_percentil(datos, 75)  # Tercer cuartil
    return Q1, Q2, Q3

# columnas relevantes (u, g, r, i, z, redshift, alpha, delta)
columnas_relevantes = ['u', 'g', 'r', 'i', 'z', 'redshift', 'alpha', 'delta']
dataset_filtrado = data[columnas_relevantes]

def imprimir_percentiles_cuartiles(percentiles_cuartiles):
    for col, valores in percentiles_cuartiles.items():
        print(f"--- {col} ---")
        for key, value in valores.items():
            print(f"{key}: {value}")
        print()  # Espacio entre columnas

percentiles_cuartiles = {}

for col in columnas_relevantes:
    col_data = dataset_filtrado[col].dropna()  # Eliminar valores NaN
    percentiles_cuartiles[col] = {
        'Q1': calcular_cuartiles(col_data)[0],
        'Mediana (Q2)': calcular_cuartiles(col_data)[1],
        'Q3': calcular_cuartiles(col_data)[2],
        'Percentil_90': calcular_percentil(col_data, 90)
    }

imprimir_percentiles_cuartiles(percentiles_cuartiles)

for col in columnas_relevantes:
    plt.figure()
    plt.hist(dataset_filtrado[col].dropna(), bins=30, alpha=0.7, color='blue', edgecolor='black')
    plt.title(f'{col}')
    plt.xlabel(col)
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.show()