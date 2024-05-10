# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Percepción
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

# Importar las bibliotecas necesarias
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist

# Cargar y preparar el conjunto de datos MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0

# Definir el modelo de percepción
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Capa para aplanar la imagen de 28x28 a un vector de 784 elementos
    layers.Dense(128, activation='relu'),   # Capa oculta con 128 neuronas y función de activación ReLU
    layers.Dense(10, activation='softmax') # Capa de salida con 10 neuronas para las 10 clases y función de activación Softmax
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_images, train_labels, epochs=5)

# Evaluar el modelo con el conjunto de datos de prueba
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Exactitud del modelo en el conjunto de prueba:", test_acc)
