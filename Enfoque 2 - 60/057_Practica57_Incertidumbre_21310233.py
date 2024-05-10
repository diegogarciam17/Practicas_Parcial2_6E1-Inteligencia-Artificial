# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Incertidumbre
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np

def funcion_a_evaluar(x):
    """Función de ejemplo para evaluar."""
    return x**2 + 2*x + 1

def simulacion_monte_carlo(funcion, n_simulaciones, rango_min, rango_max):
    """Realiza una simulación de Monte Carlo para estimar el valor esperado y la varianza de una función dada."""
    resultados = []
    
    for _ in range(n_simulaciones):
        # Genera una muestra aleatoria uniforme dentro del rango especificado
        x = np.random.uniform(rango_min, rango_max)
        # Evalúa la función en el valor de x generado aleatoriamente
        y = funcion(x)
        # Almacena el resultado de la evaluación de la función
        resultados.append(y)
    
    # Calcula el valor esperado y la varianza de los resultados
    valor_esperado = np.mean(resultados)
    varianza = np.var(resultados)
    
    return valor_esperado, varianza

# Parámetros de la simulación
n_simulaciones = 10000
rango_min = -10
rango_max = 10

# Realiza la simulación de Monte Carlo para la función especificada
valor_esperado, varianza = simulacion_monte_carlo(funcion_a_evaluar, n_simulaciones, rango_min, rango_max)

# Imprime los resultados
print("Valor esperado de la función:", valor_esperado)
print("Varianza de la función:", varianza)
