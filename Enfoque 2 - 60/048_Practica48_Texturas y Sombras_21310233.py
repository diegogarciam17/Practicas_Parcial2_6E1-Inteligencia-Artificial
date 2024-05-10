# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Texturas y Sombras
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
image = cv2.imread('imagen.png', cv2.IMREAD_GRAYSCALE)

# Aplicar un filtro de suavizado para eliminar el ruido
smoothed = cv2.GaussianBlur(image, (5, 5), 0)

# Detectar bordes utilizando el algoritmo Canny
edges = cv2.Canny(smoothed, 100, 200)

# Mostrar la imagen original y sus bordes detectados
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagen Original')
plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Bordes Detectados')
plt.show()