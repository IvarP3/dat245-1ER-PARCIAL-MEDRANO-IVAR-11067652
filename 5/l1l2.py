coeficientes = data[X].mean().values 
# Funciones de penalización L1 y L2
def penalizacion_L1(coeficientes, lambda_val):
    l1_penalizacion = 0
    for w in coeficientes:
        l1_penalizacion += abs(w)
    return lambda_val * l1_penalizacion

def penalizacion_L2(coeficientes, lambda_val):
    l2_penalizacion = 0
    for w in coeficientes:
        l2_penalizacion += w ** 2
    return lambda_val * l2_penalizacion

# Definir un valor de lambda (puedes ajustarlo según tus necesidades)
lambda_val = 0.1

# Aplicar las penalizaciones
penalizacion_l1 = penalizacion_L1(coeficientes, lambda_val)
penalizacion_l2 = penalizacion_L2(coeficientes, lambda_val)

# Mostrar resultados
print("Coeficientes:", coeficientes)
print("Penalización L1:", penalizacion_l1)
print("Penalización L2:", penalizacion_l2)

