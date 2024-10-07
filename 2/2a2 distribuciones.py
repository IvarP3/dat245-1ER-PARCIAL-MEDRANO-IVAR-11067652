def calcular_pdf_normal(x, media, desviacion):
    return (1 / (desviacion * (2 * 3.14159) ** 0.5)) * (2.71828 ** (-0.5 * ((x - media) / desviacion) ** 2))

def calcular_pdf_poisson(k, lambda_poisson):
    factorial = 1
    for i in range(1, k + 1):
        factorial *= i
    return (lambda_poisson ** k * (2.71828 ** -lambda_poisson)) / factorial

def calcular_pdf_uniforme(x, a, b):
    if a <= x <= b:
        return 1 / (b - a)
    else:
        return 0

for col in columnas_relevantes:
    plt.figure()
    col_data = dataset_filtrado[col].dropna().tolist()

    plt.hist(col_data, bins=30, density=True, alpha=0.6, color='blue', edgecolor='black')

    if col in ['u', 'g', 'r', 'i', 'z']:
        media = sum(col_data) / len(col_data)
        desviacion = (sum([(x - media) ** 2 for x in col_data]) / len(col_data)) ** 0.5
        x_vals = [min(col_data) + i * (max(col_data) - min(col_data)) / 100 for i in range(100)]
        y_vals = [calcular_pdf_normal(x, media, desviacion) for x in x_vals]
        plt.plot(x_vals, y_vals, color='red', linewidth=2)

    elif col == 'redshift':
        lambda_poisson = sum(col_data) / len(col_data)
        k_vals = list(range(int(min(col_data)), int(max(col_data)) + 1))
        y_vals = [calcular_pdf_poisson(k, lambda_poisson) for k in k_vals]
        plt.plot(k_vals, y_vals, color='green', linewidth=2)

    elif col in ['alpha', 'delta']:
        a = min(col_data)
        b = max(col_data)
        x_vals = [min(col_data) + i * (max(col_data) - min(col_data)) / 100 for i in range(100)]
        y_vals = [calcular_pdf_uniforme(x, a, b) for x in x_vals]
        plt.plot(x_vals, y_vals, color='orange', linewidth=2)

    plt.title(f'Distribución de {col} con línea de ajuste')
    plt.xlabel(col)
    plt.ylabel('Densidad')
    plt.grid(True)
    plt.show()
