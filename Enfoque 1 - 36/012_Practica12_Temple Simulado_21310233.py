# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Busqueda no informada-Búsqueda de Temple Simulado

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import math
import random

def temple_simulado(funcion_objetivo, temperatura_inicial=100, factor_enfriamiento=0.95, iteraciones_maximas=1000):
    estado_actual = random.uniform(-10, 10)  # Estado inicial aleatorio
    valor_actual = funcion_objetivo(estado_actual)
    mejor_estado = estado_actual
    mejor_valor = valor_actual
    temperatura_actual = temperatura_inicial
    
    for _ in range(iteraciones_maximas):
        estado_vecino = estado_actual + random.uniform(-0.1, 0.1)  # Genera un estado vecino aleatorio
        valor_vecino = funcion_objetivo(estado_vecino)
        
        diferencia = valor_vecino - valor_actual
        if diferencia < 0 or random.random() < math.exp(-diferencia / temperatura_actual):
            estado_actual = estado_vecino
            valor_actual = valor_vecino
            
            if valor_actual < mejor_valor:  # Minimizar la función
                mejor_estado = estado_actual
                mejor_valor = valor_actual
        
        temperatura_actual *= factor_enfriamiento  # Enfriamiento
    
    return mejor_estado, mejor_valor

# Función objetivo de ejemplo (función cuadrática)
def funcion_objetivo(x):
    return x**2

# Ejecutar Temple Simulado
mejor_estado, mejor_valor = temple_simulado(funcion_objetivo)
print("Mejor estado encontrado:", mejor_estado)
print("Valor mínimo encontrado:", mejor_valor)