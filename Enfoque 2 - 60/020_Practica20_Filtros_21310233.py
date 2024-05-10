# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Filtros de Kalman
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

from filterpy.kalman import KalmanFilter
import numpy as np

# Crear un filtro de Kalman
kf = KalmanFilter(dim_x=2, dim_z=1)

# Definir la matriz de transición de estado (A)
kf.F = np.array([[1, 1],
                 [0, 1]])

# Definir la matriz de observación (H)
kf.H = np.array([[1, 0]])

# Definir las matrices de covarianza del proceso (Q) y de medición (R)
kf.Q = np.array([[0.01, 0.02],
                 [0.02, 0.04]])
kf.R = np.array([[0.1]])

# Definir el estado inicial y la covarianza inicial
kf.x = np.array([[0],
                 [0]])
kf.P = np.eye(2)

# Observación
z = np.array([[1]])

# Actualizar el filtro de Kalman con la observación
kf.predict()
kf.update(z)

# Obtener la estimación del estado
state_estimate = kf.x
print("Estimación del estado del sistema:")
print(state_estimate)