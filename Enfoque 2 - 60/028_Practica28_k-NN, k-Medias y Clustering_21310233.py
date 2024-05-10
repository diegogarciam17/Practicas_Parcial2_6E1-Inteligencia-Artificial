# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-k-NN, k-Medias y Clustering
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.neighbors import KNeighborsClassifier

# Generar datos de ejemplo
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.6, random_state=0)

# Visualizar los datos de ejemplo
plt.figure(figsize=(12, 4))
plt.subplot(131)
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='viridis')
plt.title('Datos de ejemplo')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Algoritmo k-NN
knn = KNeighborsClassifier(n_neighbors=4)
knn.fit(X, y)

# Visualizar las fronteras de decisión de k-NN
plt.subplot(132)
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.8, cmap='viridis')
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, edgecolor='k', cmap='viridis')
plt.title('k-NN (k=4)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Algoritmo k-medias
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Visualizar las etiquetas de los clústeres de k-medias
plt.subplot(133)
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, s=50, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', s=200, marker='X')
plt.title('k-Medias')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Mostrar el gráfico
plt.tight_layout()
plt.show()

# Algoritmo de agrupamiento jerárquico
ac = AgglomerativeClustering(n_clusters=4, linkage='ward')
ac.fit(X)

# Visualizar las etiquetas de los clústeres de agrupamiento jerárquico
plt.figure(figsize=(6, 4))
plt.scatter(X[:, 0], X[:, 1], c=ac.labels_, s=50, cmap='viridis')
plt.title('Agrupamiento Jerárquico')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()