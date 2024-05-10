# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Cinemática Inversa
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np

# Longitudes de los enlaces del brazo
l1 = 2
l2 = 1.5

# Función de cinemática inversa para un brazo de 2 grados de libertad
def inverse_kinematics(x, y):
    # Calcular la distancia desde el origen al punto deseado
    r = np.sqrt(x**2 + y**2)
    
    # Calcular el ángulo de la primera articulación
    theta1 = np.arctan2(y, x)
    
    # Calcular el ángulo de la segunda articulación usando el teorema del coseno
    alpha = np.arccos((l1**2 + l2**2 - r**2) / (2 * l1 * l2))
    beta = np.arctan2(y, x)
    gamma = np.arctan2(l2 * np.sin(alpha), l1 + l2 * np.cos(alpha))
    theta2 = beta - gamma
    
    return np.degrees(theta1), np.degrees(theta2)

# Coordenadas del punto deseado
x_target = 2
y_target = 2

# Calcular la cinemática inversa para el punto deseado
theta1, theta2 = inverse_kinematics(x_target, y_target)
print("Ángulos de articulación requeridos:")
print("Theta1:", theta1)
print("Theta2:", theta2)