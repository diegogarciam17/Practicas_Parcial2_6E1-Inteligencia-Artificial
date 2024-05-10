# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Utilidad y Toma de Decisiones-Iteración de Valores
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import numpy as np

# Definir la función de transición y las recompensas
# Supongamos un MDP con dos estados (S1 y S2) y dos acciones (A1 y A2)
# Transiciones: S1->S2 con A1 (0.9) y S1->S1 con A2 (0.1), S2->S1 con A1 (0.2) y S2->S2 con A2 (0.8)
# Recompensas: S1->S2 con A1 (5), S1->S1 con A2 (1), S2->S1 con A1 (2) y S2->S2 con A2 (3)
transiciones = np.array([[[0.9, 0.1], [0.2, 0.8]], [[5, 1], [2, 3]]])
recompensas = np.array([[5, 1], [2, 3]])

# Inicializar la función de valor de cada estado a cero
valores = np.zeros(2)

# Iteración de valores
epsilon = 0.01  # Criterio de convergencia
max_valor = np.max(recompensas)
min_valor = np.min(recompensas)
while True:
    nuevos_valores = np.max(np.sum(transiciones * (recompensas + valores - min_valor) / (max_valor - min_valor), axis=2), axis=1)
    if np.max(np.abs(nuevos_valores - valores)) < epsilon:
        break
    valores = nuevos_valores


# Imprimir los valores óptimos de cada estado
print("Valores óptimos de los estados:", valores)

# Calcular la política óptima
politica = np.argmax(np.sum(transiciones * (recompensas + valores), axis=2), axis=1)
print("Política óptima:", politica)