# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Incertidumbre
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np

def propagacion_incertidumbre(mu1, sigma1, mu2, sigma2):
    """
    Calcula la incertidumbre asociada con la suma de dos variables aleatorias con distribuciones normales
    utilizando la propagación de incertidumbre.

    Args:
    - mu1: Media de la primera variable aleatoria
    - sigma1: Desviación estándar de la primera variable aleatoria
    - mu2: Media de la segunda variable aleatoria
    - sigma2: Desviación estándar de la segunda variable aleatoria

    Returns:
    - mu_suma: Media de la suma de las dos variables aleatorias
    - sigma_suma: Desviación estándar de la suma de las dos variables aleatorias
    """
    mu_suma = mu1 + mu2
    sigma_suma = np.sqrt(sigma1**2 + sigma2**2)
    return mu_suma, sigma_suma

# Valores de ejemplo para las medias y desviaciones estándar de las variables aleatorias
mu1 = 10
sigma1 = 2
mu2 = 5
sigma2 = 3

# Calcula la incertidumbre de la suma de las variables aleatorias
mu_suma, sigma_suma = propagacion_incertidumbre(mu1, sigma1, mu2, sigma2)

# Imprime los resultados
print("La media de la suma de las variables aleatorias es:", mu_suma)
print("La desviación estándar de la suma de las variables aleatorias es:", sigma_suma)