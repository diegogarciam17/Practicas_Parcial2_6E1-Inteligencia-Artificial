# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-SW Robótico
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np
import matplotlib.pyplot as plt

class DifferentialDriveRobot:
    def __init__(self, wheel_radius, wheel_distance):
        self.wheel_radius = wheel_radius
        self.wheel_distance = wheel_distance
        self.x = 0  # Posición en el eje x
        self.y = 0  # Posición en el eje y
        self.theta = 0  # Orientación del robot en radianes

    def move(self, left_wheel_speed, right_wheel_speed, dt):
        # Calcular la velocidad lineal y angular del robot
        v = self.wheel_radius * (left_wheel_speed + right_wheel_speed) / 2
        w = self.wheel_radius * (right_wheel_speed - left_wheel_speed) / self.wheel_distance

        # Calcular el desplazamiento del robot
        dx = v * np.cos(self.theta) * dt
        dy = v * np.sin(self.theta) * dt
        dtheta = w * dt

        # Actualizar la posición y orientación del robot
        self.x += dx
        self.y += dy
        self.theta += dtheta

# Parámetros del robot
wheel_radius = 0.1  # Radio de las ruedas en metros
wheel_distance = 0.5  # Distancia entre las ruedas en metros

# Crear el robot
robot = DifferentialDriveRobot(wheel_radius, wheel_distance)

# Velocidades de las ruedas (m/s)
left_wheel_speed = 1
right_wheel_speed = 0.5

# Simulación del movimiento del robot durante 5 segundos
dt = 0.1  # Paso de tiempo en segundos
num_steps = int(5 / dt)
trajectory = []

for _ in range(num_steps):
    # Mover el robot
    robot.move(left_wheel_speed, right_wheel_speed, dt)
    # Registrar la posición actual del robot
    trajectory.append((robot.x, robot.y))

# Convertir la trayectoria en un arreglo numpy
trajectory = np.array(trajectory)

# Graficar la trayectoria del robot
plt.plot(trajectory[:, 0], trajectory[:, 1], label='Trayectoria del Robot')
plt.scatter(0, 0, color='red', label='Inicio')
plt.scatter(trajectory[-1, 0], trajectory[-1, 1], color='green', label='Fin')
plt.title('Trayectoria del Robot en 2D')
plt.xlabel('Posición en X (m)')
plt.ylabel('Posición en Y (m)')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()