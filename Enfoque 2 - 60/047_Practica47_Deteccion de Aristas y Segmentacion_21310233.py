# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Detección de Aristas y Segmentación
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar una imagen en escala de grises
image = cv2.imread('imagen.png', cv2.IMREAD_GRAYSCALE)

# Aplicar el operador Canny para detectar bordes
edges = cv2.Canny(image, 100, 200)

# Aplicar la segmentación por umbralización (binarización)
ret, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Mostrar las imágenes originales y procesadas
plt.figure(figsize=(10, 6))

plt.subplot(131)
plt.imshow(image, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(132)
plt.imshow(edges, cmap='gray')
plt.title('Detección de Bordes (Canny)')
plt.axis('off')

plt.subplot(133)
plt.imshow(thresholded, cmap='gray')
plt.title('Segmentación por Umbralización')
plt.axis('off')

plt.show()