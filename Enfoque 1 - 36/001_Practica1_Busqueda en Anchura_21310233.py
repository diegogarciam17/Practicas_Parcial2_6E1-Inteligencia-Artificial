# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Busqueda en grafos

#Busqueda no informada-Busqueda en anchura

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

from collections import deque

def bfs(inicio, grafo):
    cola = deque()
    visitado = set()
    
    cola.append(inicio)
    visitado.add(inicio)
    
    while cola:
        nodo_actual = cola.popleft()
        print(nodo_actual)  # Aquí podrías realizar cualquier operación con el nodo
        
        for vecino in grafo[nodo_actual]:
            if vecino not in visitado:
                visitado.add(vecino)
                cola.append(vecino)

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
print("Recorrido BFS:")
bfs(inicio, grafo)