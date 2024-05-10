# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
#Busqueda no informada-Búsqueda Bidireccional

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def BB(grafo, inicio, objetivo):#BB (Busqueda bidireccional)
    cola_inicio = [inicio]
    cola_objetivo = [objetivo]
    visitado_inicio = {inicio}
    visitado_objetivo = {objetivo}

    while cola_inicio and cola_objetivo:
        # Exploración desde el nodo inicial
        nodo_actual_inicio = cola_inicio.pop(0)
        for vecino in grafo[nodo_actual_inicio]:
            if vecino in visitado_objetivo:
                return nodo_actual_inicio, vecino  # Se encontró un nodo en común
            if vecino not in visitado_inicio:
                visitado_inicio.add(vecino)
                cola_inicio.append(vecino)

        # Exploración desde el nodo objetivo
        nodo_actual_objetivo = cola_objetivo.pop(0)
        for vecino in grafo[nodo_actual_objetivo]:
            if vecino in visitado_inicio:
                return vecino, nodo_actual_objetivo  # Se encontró un nodo en común
            if vecino not in visitado_objetivo:
                visitado_objetivo.add(vecino)
                cola_objetivo.append(vecino)

    return None  # No se encontró un camino entre los nodos

# Ejemplo de grafo no ponderado representado como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

inicio = 'A'
objetivo = 'F'
camino = BB(grafo, inicio, objetivo)
if camino:
    camino_completo = [camino[0]] + [nodo for nodo in reversed(grafo[camino[0]]) if nodo != camino[1]] + [camino[1]]
    print("Camino más corto:", camino_completo)
else:
    print("No se encontró un camino entre los nodos.")