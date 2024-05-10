# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Red Bayes. Dinámica: Filtrado de Partículas
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

from filterpy.monte_carlo import multinomial_resample
import numpy as np
import matplotlib.pyplot as plt

# Definir la función de transición de estado del sistema
def modelo_de_proceso(x):
    return x + np.random.randn(len(x)) * 0.1  # Modelo de proceso simple con ruido

# Generar una muestra inicial de partículas
num_particulas = 1000
posicion_inicial = 0
particulas = np.random.normal(posicion_inicial, 1, num_particulas)

# Simular movimiento y observaciones
num_pasos = 50
posiciones_verdaderas = [posicion_inicial]
observaciones = [posicion_inicial + np.random.randn() * 0.5]  # Observación inicial
for _ in range(num_pasos):
    # Simular movimiento del objeto
    nueva_posicion = posiciones_verdaderas[-1] + np.random.randn() * 0.1
    posiciones_verdaderas.append(nueva_posicion)
    # Simular observación ruidosa
    observaciones.append(nueva_posicion + np.random.randn() * 0.5)

# Filtrado de partículas
for z in observaciones:
    # Predicción: propagar las partículas a través del modelo de proceso
    particulas = modelo_de_proceso(particulas)
    # Calcular las ponderaciones de las partículas
    likelihoods = np.exp(-0.5 * (z - particulas)**2)
    weights = likelihoods / np.sum(likelihoods)
    # Re-muestrear las partículas de acuerdo con sus ponderaciones
    resampled_indices = multinomial_resample(weights)
    particulas = particulas[resampled_indices]

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(posiciones_verdaderas, label='Posición Verdadera', color='blue')
plt.plot(observaciones, 'ro', label='Observaciones', markersize=5)
plt.hist(particulas, bins=30, density=True, label='Estimación de Partículas', alpha=0.5, color='green')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Filtrado de Partículas para Estimación de Posición')
plt.legend()
plt.grid(True)
plt.show()