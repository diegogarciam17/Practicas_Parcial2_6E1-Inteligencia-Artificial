# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Funciones de Activación
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Generar datos de ejemplo
X_train = np.random.randn(1000, 784)  # 1000 muestras de entrenamiento, 784 características
y_train = np.random.randint(0, 10, size=(1000,))  # Etiquetas aleatorias del 0 al 9 para las muestras de entrenamiento
X_test = np.random.randn(200, 784)  # 200 muestras de prueba, 784 características
y_test = np.random.randint(0, 10, size=(200,))  # Etiquetas aleatorias del 0 al 9 para las muestras de prueba

# Definir el modelo de red neuronal con funciones de activación específicas
model = Sequential([
    Dense(64, activation='relu', input_shape=(784,)),  # ReLU en la primera capa oculta
    Dense(64, activation='tanh'),  # Tangente hiperbólica en la segunda capa oculta
    Dense(10, activation='softmax')  # Softmax en la capa de salida
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Evaluar el modelo
test_loss, test_acc = model.evaluate(X_test, y_test)
print('Precisión en datos de prueba:', test_acc)