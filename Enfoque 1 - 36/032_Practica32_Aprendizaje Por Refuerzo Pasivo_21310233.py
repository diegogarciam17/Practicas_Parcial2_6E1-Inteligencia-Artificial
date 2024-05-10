# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Aprendizaje Por Refuerzo-Aprendizaje por Refuerzo Pasivo
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.linear_model import LinearRegression

# Generar datos de entrenamiento
num_muestras = 100
X = np.random.rand(num_muestras, 1)  # Característica
y = 2 * X + np.random.randn(num_muestras, 1)  # Etiqueta con ruido

# Inicializar el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(X, y)

# Hacer predicciones
y_pred = modelo.predict(X)

# Calcular el error cuadrático medio
mse = np.mean((y - y_pred) ** 2)
print("Error cuadrático medio:", mse)