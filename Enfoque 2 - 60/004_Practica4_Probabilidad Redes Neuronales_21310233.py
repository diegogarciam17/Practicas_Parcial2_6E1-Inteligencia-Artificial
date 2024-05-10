# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Redes Neuronales
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np

# Paso 1: Preparar los datos de entrenamiento
# Definimos los datos de entrada y salida
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
salidas = np.array([[0], [1], [1], [0]])

# Paso 2: Construir el modelo de la red neuronal
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(2, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Paso 3: Compilar el modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Paso 4: Entrenar el modelo
modelo.fit(entradas, salidas, epochs=1000, verbose=0)

# Paso 5: Evaluar el modelo
puntuacion = modelo.evaluate(entradas, salidas)
print("Precisión:", puntuacion[1])

# Paso 6: Hacer predicciones
predicciones = modelo.predict(entradas)
print("Predicciones:")
for i in range(len(entradas)):
    print(entradas[i], "-->", predicciones[i])