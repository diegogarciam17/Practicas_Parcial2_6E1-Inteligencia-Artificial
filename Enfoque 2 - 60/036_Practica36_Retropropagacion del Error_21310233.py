# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Retropropagación del Error
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np

# Función de activación ReLU
def relu(x):
    return np.maximum(0, x)

# Función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función de activación ReLU
def relu_derivative(x):
    return np.where(x > 0, 1, 0)

# Derivada de la función de activación sigmoide
def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Función de pérdida de entropía cruzada binaria
def binary_crossentropy(y_true, y_pred):
    return - (y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

# Datos de entrada
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# Salidas deseadas
y_true = np.array([[0], [1], [1], [0]])

# Inicialización de pesos
np.random.seed(42)
W1 = np.random.randn(2, 2)
b1 = np.zeros((1, 2))
W2 = np.random.randn(2, 1)
b2 = np.zeros((1, 1))

# Hiperparámetros
learning_rate = 0.01
epochs = 1000

# Entrenamiento
for epoch in range(epochs):
    # Propagación hacia adelante
    z1 = np.dot(X, W1) + b1
    a1 = relu(z1)
    z2 = np.dot(a1, W2) + b2
    y_pred = sigmoid(z2)
    
    # Cálculo de la pérdida
    loss = np.mean(binary_crossentropy(y_true, y_pred))
    
    # Propagación hacia atrás
    delta2 = y_pred - y_true
    delta1 = np.dot(delta2, W2.T) * relu_derivative(z1)
    
    # Actualización de pesos
    W2 -= learning_rate * np.dot(a1.T, delta2)
    b2 -= learning_rate * np.sum(delta2, axis=0, keepdims=True)
    W1 -= learning_rate * np.dot(X.T, delta1)
    b1 -= learning_rate * np.sum(delta1, axis=0, keepdims=True)
    
    # Imprimir pérdida cada 100 épocas
    if epoch % 100 == 0:
        print(f'Epoch {epoch}, Loss: {loss}')

# Predicción final
print("Predicción final:")
print(y_pred)