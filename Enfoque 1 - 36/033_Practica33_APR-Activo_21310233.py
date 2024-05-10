# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Aprendizaje Por Refuerzo-Aprendizaje por Refuerzo Activo
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import numpy as np

# Definir el entorno (en este caso, un simple problema de la cuadrícula)
# 0: Estado vacío
# 1: Obstáculo
# 2: Recompensa
# 3: Agente
entorno = np.array([
    [0, 0, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 2],
    [0, 1, 0, 3]
])

# Definir parámetros
gamma = 0.8  # Factor de descuento
alpha = 0.1  # Tasa de aprendizaje
epsilon = 0.1  # Probabilidad de exploración

# Inicializar la tabla Q con ceros
num_estados = entorno.size
num_acciones = 4  # arriba, abajo, izquierda, derecha
Q = np.zeros((num_estados, num_acciones))

# Función de selección de acción (epsilon-greedy)
def seleccionar_accion(estado):
    if np.random.uniform(0, 1) < epsilon:
        return np.random.choice(num_acciones)  # Exploración aleatoria
    else:
        return np.argmax(Q[estado, :])  # Explotación de la mejor acción

# Algoritmo de Q-Learning
num_episodios = 1000
for _ in range(num_episodios):
    estado = 0  # Estado inicial
    while estado != 3:  # No terminal
        accion = seleccionar_accion(estado)
        # Actualizar estado usando la acción seleccionada
        if accion == 0:  # arriba
            nuevo_estado = max(0, estado - 1)
        elif accion == 1:  # abajo
            nuevo_estado = min(num_estados - 1, estado + 1)
        elif accion == 2:  # izquierda
            nuevo_estado = max(0, estado - 4)
        else:  # derecha
            nuevo_estado = min(num_estados - 1, estado + 4)
        recompensa = entorno[nuevo_estado // 4, nuevo_estado % 4]  # Recompensa del nuevo estado
        Q[estado, accion] = Q[estado, accion] + alpha * (recompensa + gamma * np.max(Q[nuevo_estado, :]) - Q[estado, accion])
        estado = nuevo_estado  # Actualizar estado

# Mostrar la tabla Q aprendida
print("Tabla Q:")
print(Q)
