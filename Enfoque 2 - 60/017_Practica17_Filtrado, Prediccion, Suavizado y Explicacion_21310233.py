# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Filtrado, Predicción, Suavizado y Explicación

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np
import matplotlib.pyplot as plt

# Definir el modelo dinámico del sistema (matrices A, B y H)
A = np.array([[1, 1],
              [0, 1]])
B = np.array([[0.5],
              [1]])

H = np.array([[1, 0]])

# Definir las matrices de covarianza del proceso (Q) y de observación (R)
Q = np.array([[0.1, 0],
              [0, 0.1]])
R = np.array([[1]])

# Definir el estado inicial del sistema y su covarianza inicial
x0 = np.array([[0],
               [0]])
P0 = np.array([[1, 0],
               [0, 1]])

# Generar datos de observación (simulación)
np.random.seed(42)
num_steps = 100
true_states = np.zeros((2, num_steps))
observations = np.zeros((1, num_steps))
true_states[:, t] = np.dot(A, true_states[:, t-1]) + np.dot(B, np.random.randn(1, 1))
for t in range(1, num_steps):
    true_states[:, t] = np.dot(A, true_states[:, t-1]) + np.dot(B, np.random.randn(1, 1))
    observations[:, t] = np.dot(H, true_states[:, t]) + np.random.randn(1, 1) * np.sqrt(R)

# Implementar el filtro de Kalman
x = x0
P = P0
filtered_states = np.zeros_like(true_states)
predicted_states = np.zeros_like(true_states)
smoothed_states = np.zeros_like(true_states)
for t in range(num_steps):
    # Predicción del estado
    x_pred = np.dot(A, x)
    P_pred = np.dot(np.dot(A, P), A.T) + Q

    # Actualización del estado basada en la observación
    y = observations[:, t] - np.dot(H, x_pred)
    S = np.dot(np.dot(H, P_pred), H.T) + R
    K = np.dot(np.dot(P_pred, H.T), np.linalg.inv(S))
    x = x_pred + np.dot(K, y)
    P = P_pred - np.dot(np.dot(K, H), P_pred)

    # Guardar los estados filtrados y predichos
    filtered_states[:, t] = x.flatten()
    predicted_states[:, t] = x_pred.flatten()

# Implementar el suavizado de Kalman
smoothed_states[:, -1] = filtered_states[:, -1]
for t in range(num_steps-2, -1, -1):
    J = np.dot(np.dot(P[:, :, t], A.T), np.linalg.inv(P_pred))
    smoothed_states[:, t] = filtered_states[:, t] + np.dot(J, smoothed_states[:, t+1] - predicted_states[:, t+1])

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(true_states[0], label='Estado Verdadero', color='blue')
plt.plot(observations.flatten(), 'ro', label='Observaciones', markersize=5)
plt.plot(filtered_states[0], label='Filtrado', color='green')
plt.plot(predicted_states[0], '--', label='Predicción', color='orange')
plt.plot(smoothed_states[0], label='Suavizado', color='red')
plt.xlabel('Tiempo')
plt.ylabel('Estado')
plt.title('Filtrado, Predicción y Suavizado con Filtro de Kalman')
plt.legend()
plt.grid(True)
plt.show()