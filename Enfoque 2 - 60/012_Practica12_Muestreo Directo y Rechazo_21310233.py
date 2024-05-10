# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Muestreo Directo y Por Rechazo

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np
import matplotlib.pyplot as plt

# Función para generar muestras de la distribución exponencial
def exponencial(size):
    return -np.log(np.random.uniform(size=size))

# Función para realizar el muestreo por rechazo
def rejection_sampling(num_samples):
    samples = []
    max_value = 1 / np.sqrt(2 * np.pi)  # Valor máximo de la distribución normal estándar
    while len(samples) < num_samples:
        x = exponencial(1)[0]  # Genera una muestra de la distribución exponencial
        u = np.random.uniform()  # Genera un valor uniforme entre 0 y 1
        if u < np.exp(-0.5 * x ** 2) / max_value:  # Comprueba si la muestra es aceptada
            samples.append(x)
    return np.array(samples)

# Generar muestras utilizando muestreo por rechazo
num_samples = 1000
samples = rejection_sampling(num_samples)

# Visualizar las muestras generadas
plt.hist(samples, bins=30, density=True, alpha=0.6, color='g')
plt.title('Muestreo por Rechazo: Distribución Normal Estándar')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.show()