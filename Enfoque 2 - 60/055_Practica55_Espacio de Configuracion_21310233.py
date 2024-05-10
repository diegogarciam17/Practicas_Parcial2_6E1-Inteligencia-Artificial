# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Movimiento: Espacio de Configuración
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np
import matplotlib.pyplot as plt

# Definir los límites del entorno
world_size = 10
min_x, max_x = 0, world_size
min_y, max_y = 0, world_size

# Crear una cuadrícula de puntos en el espacio de configuración
num_points = 50
x_values = np.linspace(min_x, max_x, num_points)
y_values = np.linspace(min_y, max_y, num_points)
config_space = np.transpose([np.tile(x_values, len(y_values)), np.repeat(y_values, len(x_values))])

# Visualizar el espacio de configuración
plt.figure(figsize=(8, 6))
plt.plot(config_space[:, 0], config_space[:, 1], 'o', markersize=3, color='blue')
plt.title('Espacio de Configuración')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.xlim(min_x, max_x)
plt.ylim(min_y, max_y)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()