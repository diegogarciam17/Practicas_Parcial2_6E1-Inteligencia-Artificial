# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Utilidad y Toma de Decisiones-Proceso de Decisión de Markov (MDP)
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import numpy as np

# Definir el MDP
num_estados = 3
num_acciones = 2

# Definir la matriz de transiciones (estado x acción x estado)
# En este ejemplo, las transiciones son determinísticas
transiciones = np.array([[[1, 0, 0], [0, 1, 0]],  # Acción 0: transiciones de S0 y S1 a S0 y S1, respectivamente
                         [[0, 1, 0], [0, 0, 1]]]) # Acción 1: transiciones de S1 y S2 a S1 y S2, respectivamente

# Definir la matriz de recompensas (estado x acción)
# El estado 2 es el estado final con recompensa 1, los demás estados tienen recompensa 0
recompensas = np.array([[0, 0],
                        [0, 0],
                        [0, 1]])

# Iteración de políticas
politica = np.zeros(num_estados, dtype=int)  # Política inicial (todas las acciones son 0)
while True:
    valores = np.zeros(num_estados)
    for estado in range(num_estados):
        # Calcular el valor del estado actual según la política actual
        valores[estado] = np.sum(transiciones[estado, politica[estado]] * recompensas[estado, politica[estado]])
    politica_estable = True
    for estado in range(num_estados):
        # Calcular la mejor acción para el estado actual
        mejor_accion = np.argmax(np.sum(transiciones[estado] * (recompensas[estado] + valores), axis=1))
        if politica[estado] != mejor_accion:
            # Actualizar la política si la acción cambia
            politica[estado] = mejor_accion
            politica_estable = False
    if politica_estable:
        # Detener la iteración si la política no cambia
        break

print("Política óptima:", politica)
