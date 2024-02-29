import numpy as np  # Importa la librería numpy bajo el alias np

# Parámetros del modelo
r = 10  # Precio de venta por unidad
S = 100  # Umbral máximo de inventario
s = 20  # Umbral mínimo de inventario
h = 0.1  # Costo de almacenaje por unidad de tiempo
L = 2  # Tiempo de demora de reposición
T = 100  # Tiempo total de simulación

# Inicialización de variables
t = 0  # Tiempo general
tA = np.random.exponential(1)  # Tiempo de arribo de cliente, distribución exponencial con media 1
tM = float('inf')  # Tiempo de arribo de reposición, inicialmente infinito
C = H = R = P = y = 0  # Inicialización de contadores y acumuladores
x = 50  # Cantidad inicial en almacén

# Simulación basada en eventos discretos
while min(tA, tM) <= T:  # Mientras alguno de los tiempos de arribo sea menor o igual al tiempo total
    if tA <= tM:  # Si el tiempo de arribo de cliente es menor o igual al de reposición
        H += (tA - t) * x * h  # Actualiza el costo de almacbn/enaje considerando el tiempo transcurrido
        t = tA  # Actualiza el tiempo general
        X = np.random.randint(1, 30)  # Genera la demanda de clientes
        w = min(x, X)  # Calcula la cantidad vendida, tomando el mínimo entre lo disponible y la demanda
        R += w * r  # Actualiza los ingresos
        P += (X - w) * r  # Actualiza las pérdidas por falta de stock
        x -= w  # Actualiza la cantidad en inventario
        if x < s and y == 0:  # Si el inventario está por debajo del umbral mínimo y no hay reposición en curso
            y = S - x  # Calcula la cantidad a reponer
            tM = t + L  # Establece el tiempo de arribo de reposición
        tA += np.random.exponential(1)  # Genera el próximo tiempo de arribo de cliente
    else:  # Si el tiempo de arribo de reposición es menor al de cliente
        H += (tM - t) * x * h  # Actualiza el costo de almacenaje considerando el tiempo transcurrido
        t = tM  # Actualiza el tiempo general
        C += 10  # Actualiza el costo de ordenar y unidades
        x += y  # Incrementa la cantidad en inventario
        y = 0  # Reinicia la cantidad a reponer
        tM = float('inf')  # Indica que no hay reposición en curso

# Calcular ganancia total
ganancia_total = R - H - C  # Ingresos menos costos totales (ingresos - costos de almacenaje - costos de reposición)
perdida_por_falta_de_stock = P  # Pérdidas por falta de stock

# Resultados
print("Ganancia total:", ganancia_total)  # Imprime la ganancia total
print("Pérdida por falta de stock:", perdida_por_falta_de_stock)  # Imprime la pérdida por falta de stock
