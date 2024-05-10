# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Aprendizaje Por Refuerzo-Búsqueda de la Política
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import numpy as np

# Definir la función de recompensa
recompensa = np.array([[0, 0, 0, 0],
                       [0, 0, 0, 0]])

# Definir la matriz de transición de estado
transiciones = np.array([[[0.8, 0.1, 0.1, 0],
                          [0.1, 0.7, 0.1, 0.1],
                          [0, 0.1, 0.7, 0.2],
                          [0, 0, 0, 1]],
                         [[0.7, 0.2, 0.1, 0],
                          [0.1, 0.7, 0.2, 0],
                          [0, 0.1, 0.8, 0.1],
                          [0, 0, 0, 1]]])

# Inicializar la función de valor con la misma forma que la recompensa
valores = np.zeros_like(recompensa)

# Algoritmo de Iteración de Valor
def iteracion_de_valor(recompensa, transiciones, gamma=0.9, theta=0.0001):
    while True:
        delta = 0
        for s in range(2):
            v = valores[s].copy()
            nuevos_valores = np.sum(transiciones[s] * (recompensa[s] + gamma * valores), axis=1)
            valores[s] = np.max(nuevos_valores)
            delta = max(delta, np.abs(np.max(valores[s]) - np.max(v)))
        if delta < theta:
            break

# Ejecutar la Iteración de Valor
iteracion_de_valor(recompensa, transiciones)

# Calcular la política óptima
politica = np.argmax(np.sum(transiciones * (recompensa + 0.9 * valores[:, None, :]), axis=2), axis=1)
print("Política óptima:", politica)

