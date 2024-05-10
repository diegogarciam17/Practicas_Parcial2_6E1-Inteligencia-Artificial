# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Busqueda no informada-Búsquedas A* y AO*_A*

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import heapq

def a_estrella(grafo, inicio, objetivo, heuristica):
    cola_prioridad = [(0, inicio)]
    visitado = set()
    costo_acumulado = {inicio: 0}
    
    while cola_prioridad:
        costo, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual == objetivo:
            return True  # Se encontró el objetivo
        
        if nodo_actual in visitado:
            continue
        
        visitado.add(nodo_actual)
        
        for vecino, costo_arista in grafo[nodo_actual]:
            nuevo_costo = costo_acumulado[nodo_actual] + costo_arista
            if vecino not in costo_acumulado or nuevo_costo < costo_acumulado[vecino]:
                costo_acumulado[vecino] = nuevo_costo
                heapq.heappush(cola_prioridad, (nuevo_costo + heuristica(vecino, objetivo), vecino))
    
    return False  # No se encontró el objetivo
