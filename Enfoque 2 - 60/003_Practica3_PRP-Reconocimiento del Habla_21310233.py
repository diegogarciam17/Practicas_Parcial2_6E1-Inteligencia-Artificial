# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Razonamiento Probabilístico en el Tiempo:Reconocimiento del Habla
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

from hmmlearn import hmm
import numpy as np

# Definir el modelo HMM
modelo = hmm.GaussianHMM(n_components=3, covariance_type="full")

# Entrenar el modelo con datos de entrenamiento
datos_entrenamiento = np.array([[0.5], [1.0], [-1.0], [0.42]]).reshape(-1, 1)
modelo.fit(datos_entrenamiento)

# Decodificar una secuencia de observaciones
secuencia_observaciones = np.array([[0.5], [1.0], [-1.0], [0.42]]).reshape(-1, 1)
secuencia_estados, probabilidades = modelo.decode(secuencia_observaciones)

print("Secuencia de estados más probable:", secuencia_estados)
print("Probabilidad de la secuencia de estados:", probabilidades)