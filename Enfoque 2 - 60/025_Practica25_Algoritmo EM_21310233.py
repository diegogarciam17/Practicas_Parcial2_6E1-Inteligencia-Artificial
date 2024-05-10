# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Algoritmo EM
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

# Generar datos de ejemplo con la función make_blobs
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=42)

# Crear una instancia del modelo de mezcla de Gaussianas
gmm = GaussianMixture(n_components=4, max_iter=100, random_state=42)

# Ajustar el modelo a los datos
gmm.fit(X)

# Obtener las etiquetas de cluster asignadas a cada punto de datos
labels = gmm.predict(X)

# Obtener los parámetros del modelo ajustado
means = gmm.means_
covariances = gmm.covariances_
weights = gmm.weights_

# Graficar los datos y los centroides de los clusters
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50, alpha=0.7)
plt.scatter(means[:, 0], means[:, 1], c='red', s=200, marker='X', edgecolors='k')
plt.title('Modelo de Mezcla de Gaussianas')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()