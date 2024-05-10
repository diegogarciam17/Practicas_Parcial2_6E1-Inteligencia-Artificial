# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Aprendizaje Bayesiano
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np

# Definir una función para simular el lanzamiento de una moneda
def lanzamiento_moneda(probabilidad_cara, num_lanzamientos):
    # Generar una secuencia de lanzamientos de la moneda
    lanzamientos = np.random.rand(num_lanzamientos)
    # Contar el número de caras
    num_caras = np.sum(lanzamientos < probabilidad_cara)
    return num_caras / num_lanzamientos

# Definir la probabilidad a priori de que salga cara (sin conocimiento previo)
probabilidad_cara_a_priori = 0.5

# Simular lanzamientos de la moneda y actualizar la probabilidad a posteriori
num_lanzamientos_totales = 1000
num_lanzamientos = 10
for _ in range(num_lanzamientos_totales // num_lanzamientos):
    # Simular lanzamientos de la moneda
    resultado_lanzamiento = lanzamiento_moneda(probabilidad_cara_a_priori, num_lanzamientos)
    # Actualizar la probabilidad a posteriori utilizando el teorema de Bayes
    probabilidad_cara_a_posteriori = (resultado_lanzamiento * probabilidad_cara_a_priori) / \
                                      (resultado_lanzamiento * probabilidad_cara_a_priori + (1 - resultado_lanzamiento) * (1 - probabilidad_cara_a_priori))
    # Actualizar la probabilidad a priori para el siguiente conjunto de lanzamientos
    probabilidad_cara_a_priori = probabilidad_cara_a_posteriori

# Imprimir la probabilidad a posteriori estimada
print("La probabilidad a posteriori de que salga cara es:", probabilidad_cara_a_posteriori)