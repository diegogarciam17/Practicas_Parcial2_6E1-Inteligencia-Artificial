# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Localización: Monte-Carlo
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, x, y, theta, weight=1):
        self.x = x
        self.y = y
        self.theta = theta
        self.weight = weight

    def move(self, delta_x, delta_y, delta_theta):
        self.x += delta_x
        self.y += delta_y
        self.theta += delta_theta

class MonteCarloLocalization:
    def __init__(self, num_particles, map_size):
        self.num_particles = num_particles
        self.map_size = map_size
        self.particles = []

        # Inicializar las partículas de forma aleatoria en el mapa
        for _ in range(num_particles):
            x = np.random.uniform(0, map_size[0])
            y = np.random.uniform(0, map_size[1])
            theta = np.random.uniform(0, 2 * np.pi)
            self.particles.append(Particle(x, y, theta))

    def move_particles(self, delta_x, delta_y, delta_theta):
        for particle in self.particles:
            particle.move(delta_x, delta_y, delta_theta)

    def update_weights(self, measurements):
        for particle in self.particles:
            # Calcular la probabilidad de observar las mediciones dadas la posición de la partícula
            # (En una implementación real, esta sería la función de verosimilitud)
            particle.weight = 1.0  # Supongamos una probabilidad uniforme por ahora

def resample_particles(self):
        # Normalizar los pesos para asegurarse de que sumen 1
        weights = np.array([particle.weight for particle in self.particles])
        weights /= np.sum(weights)

        # Remuestrear las partículas usando las probabilidades normalizadas
        indices = np.random.choice(range(self.num_particles), size=self.num_particles, p=weights)

        self.particles = [self.particles[i] for i in indices]


    def estimate_pose(self):
        # Implementación de la función estimate_pose
        pass

# Parámetros
num_particles = 100
map_size = (10, 10)

# Inicializar el algoritmo de localización de Monte Carlo
mcl = MonteCarloLocalization(num_particles, map_size)

# Simular movimiento del robot (por ejemplo, avanzar 1 metro y girar 45 grados)
mcl.move_particles(1, 0, np.pi/4)

# Simular mediciones del entorno (por ejemplo, lecturas de un sensor de distancia)
measurements = [1.2, 0.8, 1.0]  # Ejemplo de mediciones

# Actualizar los pesos de las partículas en función de las mediciones
mcl.update_weights(measurements)

# Remuestrear las partículas
mcl.resample_particles()

# Estimar la pose del robot
estimated_pose = mcl.estimate_pose()
print("Pose estimada del robot:", estimated_pose)