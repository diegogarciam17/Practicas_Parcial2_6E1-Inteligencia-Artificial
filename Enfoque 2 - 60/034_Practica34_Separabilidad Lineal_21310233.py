# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Separabilidad Lineal
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generar datos de ejemplo
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=42)

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de perceptrón
perceptron = Perceptron()
perceptron.fit(X_train, y_train)

# Predecir con el conjunto de prueba
y_pred = perceptron.predict(X_test)

# Calcular la precisión
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del Perceptrón:", accuracy)

# Verificar la separabilidad lineal
if accuracy == 1.0:
    print("Los datos son linealmente separables.")
else:
    print("Los datos no son linealmente separables.")

# Visualizar los datos y el hiperplano de separación
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')

# Coeficientes del hiperplano de separación
w = perceptron.coef_[0]
b = perceptron.intercept_[0]

# Plotear el hiperplano de separación
x_hyperplane = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
y_hyperplane = -(w[0] / w[1]) * x_hyperplane - (b / w[1])
plt.plot(x_hyperplane, y_hyperplane, linestyle='--', color='black')

plt.title('Separabilidad Lineal')
plt.show()
