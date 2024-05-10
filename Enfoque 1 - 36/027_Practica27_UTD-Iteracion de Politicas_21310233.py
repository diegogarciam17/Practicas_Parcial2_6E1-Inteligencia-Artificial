# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Utilidad y Toma de Decisiones-Iteración de Políticas
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import numpy as np

def iteracion_politicas(transiciones, recompensas, gamma=0.9, epsilon=0.01):
    num_estados, num_acciones, _ = transiciones.shape
    politica = np.zeros(num_estados, dtype=int)
    while True:
        # Paso 1: Evaluación de la política
        valores = np.zeros(num_estados)
        for estado in range(num_estados):
            valores[estado] = np.sum(transiciones[estado, politica[estado], :] * (recompensas[estado, politica[estado]] + gamma * valores))
        
        # Paso 2: Mejora de la política
        politica_estable = True
        for estado in range(num_estados):
            mejor_accion = np.argmax(np.sum(transiciones[estado] * (recompensas[estado] + gamma * valores), axis=1))
            if politica[estado] != mejor_accion:
                politica[estado] = mejor_accion
                politica_estable = False
        
        # Comprobar convergencia
        if politica_estable:
            break
    
    return politica

# Definir la función de transición y las recompensas
transiciones = np.array([[[0.9, 0.1], [0.2, 0.8]], [[5, 1], [2, 3]]])
recompensas = np.array([[5, 1], [2, 3]])

# Resolver el MDP utilizando iteración de políticas
politica_optima = iteracion_politicas(transiciones, recompensas)

print("Política óptima:", politica_optima)