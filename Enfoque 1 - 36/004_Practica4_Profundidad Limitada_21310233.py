# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Búsqueda en Profundidad Limitada (DLFS por sus siglas en inglés, Depth-Limited Search)


def dlfs(nodo, grafo, visitado, limite):
    if limite >= 0:
        if nodo not in visitado:
            print(nodo)  # Aquí podrías realizar cualquier operación con el nodo
            visitado.add(nodo)
            for vecino in grafo[nodo]:
                dlfs(vecino, grafo, visitado, limite - 1)

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
limite_profundidad = 2
print(f"Recorrido Busqueda en profundidad Limitado a Profundidad {limite_profundidad}:")
dlfs(inicio, grafo, visitado, limite_profundidad)