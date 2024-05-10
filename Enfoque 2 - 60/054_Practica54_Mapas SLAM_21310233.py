# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Generación de Mapas SLAM
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del entorno
num_landmarks = 5
landmarks = np.random.rand(num_landmarks, 2) * 10  # Posiciones aleatorias de los puntos de referencia
world_size = 10  # Tamaño del mundo (cuadrado)

# Parámetros del robot
initial_position = np.array([world_size / 2, world_size / 2])  # Posición inicial del robot
motion_noise = 0.1  # Ruido del movimiento
measurement_noise = 0.1  # Ruido de las mediciones

# Parámetros del filtro de partículas
num_particles = 100
particles = np.tile(initial_position, (num_particles, 1))  # Inicializar partículas en la posición inicial

# Función para mover el robot
def move_robot(position, delta):
    return np.clip(position + delta + np.random.randn(2) * motion_noise, 0, world_size)

# Función para medir la distancia a los puntos de referencia
def sense(position):
    return np.linalg.norm(landmarks - position, axis=1) + np.random.randn(num_landmarks) * measurement_noise

# Algoritmo SLAM
def slam(iterations):
    for _ in range(iterations):
        # Mover el robot y realizar una medición
        motion = np.random.randn(2)
        position = move_robot(initial_position, motion)
        measurements = sense(position)
        
        # Actualizar las partículas
        for i in range(num_particles):
            particles[i] = move_robot(particles[i], motion)
            weight = 1.0
            for j in range(num_landmarks):
                distance = np.linalg.norm(particles[i] - landmarks[j])
                weight *= np.exp(-(measurements[j] - distance) ** 2 / (2 * measurement_noise ** 2))
            particles[i] = np.clip(particles[i] + np.random.randn(2) * motion_noise, 0, world_size)
        
        # Calcular la posición del robot como el promedio ponderado de las partículas
        estimated_position = np.mean(particles, axis=0)
        
        # Visualizar el resultado
        plt.clf()
        plt.plot(landmarks[:, 0], landmarks[:, 1], 'bo', markersize=8, label='Landmarks')
        plt.plot(estimated_position[0], estimated_position[1], 'rx', markersize=10, label='Estimated Position')
        plt.plot(position[0], position[1], 'g.', markersize=10, label='True Position')
        plt.xlim(0, world_size)
        plt.ylim(0, world_size)
        plt.legend()
        plt.pause(0.1)
    
    plt.show()

# Ejecutar el algoritmo SLAM durante 100 iteraciones
slam(100)