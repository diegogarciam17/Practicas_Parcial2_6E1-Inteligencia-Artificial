# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Busqueda no informada-Búsqueda en Anchura de Costo Uniforme

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import heapq

def ucs(inicio, objetivo, grafo): # Búsqueda en Anchura de Costo Uniforme (UCS por sus siglas en inglés, Uniform Cost Search)
    cola_prioridad = [(0, inicio)]  # (costo acumulado, nodo)
    visitado = set()
    
    while cola_prioridad:
        costo_acumulado, nodo_actual = heapq.heappop(cola_prioridad)
        if nodo_actual == objetivo:
            return costo_acumulado
        
        if nodo_actual not in visitado:
            visitado.add(nodo_actual)
            for vecino, costo in grafo[nodo_actual].items():
                heapq.heappush(cola_prioridad, (costo_acumulado + costo, vecino))
    
    return float('inf')  # Si no se encuentra el objetivo, retornar infinito

# Ejemplo de grafo ponderado representado como un diccionario de diccionarios
grafo = {
    'A': {'B': 1, 'C': 5},
    'B': {'A': 1, 'D': 3, 'E': 7},
    'C': {'A': 5, 'F': 2},
    'D': {'B': 3},
    'E': {'B': 7, 'F': 1},
    'F': {'C': 2, 'E': 1}
}

inicio = 'A'
objetivo = 'F'
costo_minimo = ucs(inicio, objetivo, grafo)
if costo_minimo != float('inf'):
    print(f"El costo mínimo desde {inicio} hasta {objetivo} es: {costo_minimo}")
else:
    print(f"No se encontró un camino desde {inicio} hasta {objetivo}")