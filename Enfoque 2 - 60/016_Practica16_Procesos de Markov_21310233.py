# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Hipótesis de Markov: Procesos de Markov

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np

# Definir la matriz de transición para una cadena de Markov de dos estados
# En este ejemplo, el primer estado es '0' y el segundo estado es '1'
# La matriz de transición indica las probabilidades de transición entre estados
# Por ejemplo, T[0, 0] es la probabilidad de permanecer en el estado '0'
# y T[0, 1] es la probabilidad de pasar del estado '0' al estado '1'
T = np.array([[0.8, 0.2],
              [0.4, 0.6]])

# Definir el estado inicial
estado_inicial = 0

# Definir el número de pasos de tiempo para simular
num_pasos_tiempo = 10

# Lista para almacenar la secuencia de estados generada por el proceso de Markov
secuencia_estados = [estado_inicial]

# Función para simular el proceso de Markov
def simular_proceso_markov(estado_actual, matriz_transicion, num_pasos):
    for _ in range(num_pasos):
        # Generar un estado futuro basado en la probabilidad de transición desde el estado actual
        estado_futuro = np.random.choice([0, 1], p=matriz_transicion[estado_actual])
        # Agregar el estado futuro a la secuencia de estados
        secuencia_estados.append(estado_futuro)
        # Actualizar el estado actual para el próximo paso de tiempo
        estado_actual = estado_futuro

# Simular el proceso de Markov
simular_proceso_markov(estado_inicial, T, num_pasos_tiempo)

# Imprimir la secuencia de estados generada por el proceso de Markov
print("Secuencia de estados generada por el proceso de Markov:")
print(secuencia_estados)