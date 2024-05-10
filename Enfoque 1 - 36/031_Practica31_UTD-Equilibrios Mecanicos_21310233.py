# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Utilidad y Toma de Decisiones-Teoría de Juegos: Equilibrios y Mecanismos
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import numpy as np

# Definir la cantidad de jugadores y sus ofertas
num_jugadores = 3
ofertas = np.random.randint(1, 101, size=num_jugadores)  # Ofertas aleatorias entre 1 y 100

# Encontrar la oferta más alta y su índice
oferta_maxima = np.max(ofertas)
indice_maximo = np.argmax(ofertas)

# Eliminar la oferta más alta y encontrar la segunda oferta más alta
ofertas_sin_maxima = np.delete(ofertas, indice_maximo)
segunda_oferta_maxima = np.max(ofertas_sin_maxima)

# Encontrar el índice de la segunda oferta más alta
indice_segunda_maxima = np.argmax(ofertas_sin_maxima)

# Mostrar resultados
print("Ofertas de los jugadores:", ofertas)
print("Oferta más alta:", oferta_maxima)
print("Segunda oferta más alta:", segunda_oferta_maxima)
print("Ganador de la subasta:", indice_maximo)
print("Precio pagado por el ganador:", segunda_oferta_maxima)
