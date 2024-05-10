# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Busqueda no informada-Búsqueda en Profundidad

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def dfs(nodo, grafo, visitado): #Búsqueda en Profundidad (DFS por sus siglas en inglés, Depth-First Search) 
    if nodo not in visitado:
        print(nodo)  # Aquí podrías realizar cualquier operación con el nodo
        visitado.add(nodo)
        for vecino in grafo[nodo]:
            dfs(vecino, grafo, visitado)

# Ejemplo de grafo representado como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

inicio = 'A'
visitado = set()
print("Recorrido de Busqueda de profundidad:")
dfs(inicio, grafo, visitado)