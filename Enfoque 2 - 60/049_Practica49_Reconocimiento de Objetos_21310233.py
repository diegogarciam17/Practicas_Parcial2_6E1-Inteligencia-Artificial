# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Reconocimiento de Objetos
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import cv2
import numpy as np
import tensorflow as tf

# Cargar el modelo preentrenado de detección de objetos
model = tf.saved_model.load('ruta/a/modelo_objetos')

# Función para realizar la detección de objetos en una imagen
def detect_objects(image):
    # Convertir la imagen a un tensor
    input_tensor = tf.convert_to_tensor(image)
    input_tensor = input_tensor[tf.newaxis, ...]

    # Realizar la detección de objetos
    detections = model(input_tensor)

    return detections

# Cargar la imagen
image = cv2.imread('imagen.png')

# Realizar la detección de objetos en la imagen
detections = detect_objects(image)

# Mostrar los resultados de la detección de objetos en la imagen
for i in range(detections['num_detections']):
    class_id = int(detections['detection_classes'][0, i])
    score = float(detections['detection_scores'][0, i])
    bbox = [int(coord) for coord in detections['detection_boxes'][0, i]]

    if score > 0.5:
        cv2.rectangle(image, (bbox[1], bbox[0]), (bbox[3], bbox[2]), (0, 255, 0), 2)
        cv2.putText(image, f'Objeto {class_id} - {score}', (bbox[1], bbox[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Mostrar la imagen con los objetos detectados
cv2.imshow('Objetos Detectados', image)
cv2.waitKey(0)
cv2.destroyAllWindows()