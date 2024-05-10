# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Aprendizaje Por Refuerzo-Exploración vs. Explotación
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import numpy as np

# Definir parámetros
epsilon = 0.1  # Probabilidad de exploración

# Función de selección de acción (epsilon-greedy)
def seleccionar_accion(Q, estado):
    if np.random.uniform(0, 1) < epsilon:
        # Exploración: seleccionar una acción aleatoria
        return np.random.choice(len(Q[estado]))
    else:
        # Explotación: seleccionar la mejor acción según la tabla Q
        return np.argmax(Q[estado])

# Algoritmo de Q-Learning
def q_learning(entorno, gamma=0.8, alpha=0.1, num_episodios=1000):
    # Inicializar la tabla Q con ceros
    num_estados = entorno.shape[0]
    num_acciones = entorno.shape[1]
    Q = np.zeros((num_estados, num_acciones))
    
    # Ejecutar episodios de aprendizaje
    for _ in range(num_episodios):
        estado = 0  # Estado inicial
        while estado != num_estados - 1:  # No terminal
            accion = seleccionar_accion(Q, estado)
            # Selección del nuevo estado según las probabilidades definidas en el entorno
            nuevo_estado = np.random.choice(num_estados, p=entorno[estado])
            recompensa = entorno[estado, accion]  # Recompensa del nuevo estado
            mejor_proxima_accion = np.max(Q[nuevo_estado])
            Q[estado, accion] = Q[estado, accion] + alpha * (recompensa + gamma * mejor_proxima_accion - Q[estado, accion])
            estado = nuevo_estado  # Actualizar estado
    
    return Q

# Ejemplo de uso
# Definir una matriz de recompensas (entorno)
# Cada fila representa un estado y cada columna representa una acción
entorno = np.array([[0, 1], [1, 2], [2, 3], [3, 0]])  # Ejemplo de entorno (matriz de recompensas)
Q_aprendida = q_learning(entorno)
print("Tabla Q aprendida:")
print(Q_aprendida)