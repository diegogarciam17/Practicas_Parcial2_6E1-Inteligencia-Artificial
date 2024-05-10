# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Busqueda no informada-Algoritmos Genéticos

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import random

def algoritmo_genetico(funcion_objetivo, tamano_poblacion=100, tasa_mutacion=0.1, generaciones_maximas=1000):
    # Inicialización de la población
    poblacion = [random.uniform(-10, 10) for _ in range(tamano_poblacion)]
    
    for generacion in range(generaciones_maximas):
        # Evaluación de la aptitud de la población
        aptitudes = [funcion_objetivo(individuo) for individuo in poblacion]
        
        # Selección de padres mediante selección de torneo
        padres = []
        for _ in range(tamano_poblacion):
            torneo = random.sample(list(range(tamano_poblacion)), 2)
            padres.append(poblacion[torneo[0]] if aptitudes[torneo[0]] > aptitudes[torneo[1]] else poblacion[torneo[1]])
        
        # Cruce de padres para producir descendencia
        descendencia = []
        for i in range(0, tamano_poblacion, 2):
            punto_cruce = random.randint(0, 1)
            hijo1 = padres[i] * punto_cruce + padres[i+1] * (1 - punto_cruce)
            hijo2 = padres[i+1] * punto_cruce + padres[i] * (1 - punto_cruce)
            descendencia.extend([hijo1, hijo2])
        
        # Mutación de la descendencia
        for i in range(len(descendencia)):
            if random.random() < tasa_mutacion:
                punto_mutacion = random.randint(0, len(descendencia[i]) - 1)
                descendencia[i] = descendencia[i][:punto_mutacion] + [random.uniform(-10, 10)] + descendencia[i][punto_mutacion+1:]
        
        # Reemplazo de la población por la descendencia
        poblacion = descendencia
    
    # Devolver el mejor individuo encontrado
    mejor_individuo = min(poblacion, key=funcion_objetivo)
    mejor_valor = funcion_objetivo(mejor_individuo)
    
    return mejor_individuo, mejor_valor

# Función objetivo de ejemplo (función cuadrática)
def funcion_objetivo(x):
    return x**2

# Ejecutar el Algoritmo Genético
mejor_individuo, mejor_valor = algoritmo_genetico(funcion_objetivo)
print("Mejor individuo encontrado:", mejor_individuo)
print("Valor mínimo encontrado:", mejor_valor)
