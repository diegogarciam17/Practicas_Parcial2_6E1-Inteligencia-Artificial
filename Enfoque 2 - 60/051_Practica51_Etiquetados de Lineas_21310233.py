# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Etiquetados de Líneas
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('imagen.png', cv2.IMREAD_GRAYSCALE)

# Aplicar umbralización para obtener una imagen binaria
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)

# Encontrar contornos en la imagen binaria
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar contornos en la imagen original
output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
for contour in contours:
    cv2.drawContours(output_image, [contour], -1, (0, 255, 0), 2)

# Mostrar la imagen con los contornos dibujados
cv2.imshow('Lineas Etiquetadas', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()