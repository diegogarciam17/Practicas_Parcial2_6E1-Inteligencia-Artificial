# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Ponderación de Verosimilitud

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# Generar datos de ejemplo
X, y = make_regression(n_samples=1000, n_features=2, noise=0.1, random_state=42)

# Crear un modelo de regresión lineal
model = LinearRegression()

# Ajustar el modelo a los datos de muestra sin ponderación
model.fit(X, y)

# Imprimir los coeficientes del modelo sin ponderación
print("Coeficientes del modelo sin ponderación:")
print(model.coef_)

# Crear pesos para la ponderación (en este caso, simplemente se usará el inverso de la distancia euclidiana al cuadrado)
weights = 1 / np.linalg.norm(X, axis=1)**2

# Ajustar el modelo a los datos de muestra con ponderación
model.fit(X, y, sample_weight=weights)

# Imprimir los coeficientes del modelo con ponderación
print("\nCoeficientes del modelo con ponderación:")
print(model.coef_)