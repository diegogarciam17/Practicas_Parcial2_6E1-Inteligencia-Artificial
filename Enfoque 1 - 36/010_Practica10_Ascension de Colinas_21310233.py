# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Busqueda no informada-Búsqueda de Ascensión de Colinas

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import random

def hill_climbing(funcion_objetivo, paso=0.01, iteraciones_maximas=1000): #Búsqueda de Ascenso de Colinas (Hill Climbing)
    punto_actual = random.uniform(-10, 10)  # Punto inicial aleatorio
    valor_actual = funcion_objetivo(punto_actual)
    
    for _ in range(iteraciones_maximas):
        nuevo_punto = punto_actual + random.uniform(-paso, paso)  # Movimiento aleatorio
        nuevo_valor = funcion_objetivo(nuevo_punto)
        
        if nuevo_valor > valor_actual:  # Maximizar la función
            punto_actual = nuevo_punto
            valor_actual = nuevo_valor
    
    return punto_actual, valor_actual

# Función objetivo de ejemplo (función cuadrática)
def funcion_objetivo(x):
    return -x**2

# Ejecutar la búsqueda de ascenso de colinas
maximo_local, valor_maximo = hill_climbing(funcion_objetivo)
print("Máximo local encontrado:", maximo_local)
print("Valor máximo encontrado:", valor_maximo)
