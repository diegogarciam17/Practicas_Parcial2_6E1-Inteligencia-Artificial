# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

import heapq

# Definir el entorno (representado como una matriz)
entorno = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Definir los movimientos posibles del robot (arriba, abajo, izquierda, derecha)
movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Función para encontrar una ruta utilizando el algoritmo A*
def encontrar_ruta(inicio, objetivo):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio))
    padres = {inicio: None}
    costos = {inicio: 0}
    
    while cola_prioridad:
        costo_actual, nodo_actual = heapq.heappop(cola_prioridad)
        if nodo_actual == objetivo:
            break
        for movimiento in movimientos:
            fila_nueva = nodo_actual[0] + movimiento[0]
            columna_nueva = nodo_actual[1] + movimiento[1]
            nuevo_nodo = (fila_nueva, columna_nueva)
            if 0 <= fila_nueva < len(entorno) and 0 <= columna_nueva < len(entorno[0]) and entorno[fila_nueva][columna_nueva] == 0:
                nuevo_costo = costo_actual + 1
                if nuevo_nodo not in costos or nuevo_costo < costos[nuevo_nodo]:
                    costos[nuevo_nodo] = nuevo_costo
                    heapq.heappush(cola_prioridad, (nuevo_costo + distancia_manhattan(nuevo_nodo, objetivo), nuevo_nodo))
                    padres[nuevo_nodo] = nodo_actual
                    
    if objetivo not in padres:
        return None
    else:
        ruta = []
        nodo_actual = objetivo
        while nodo_actual is not None:
            ruta.append(nodo_actual)
            nodo_actual = padres[nodo_actual]
        return ruta[::-1]

# Función para calcular la distancia Manhattan entre dos puntos
def distancia_manhattan(punto1, punto2):
    return abs(punto1[0] - punto2[0]) + abs(punto1[1] - punto2[1])

# Función para simular la navegación del robot
def navegar(inicio, objetivo):
    ruta = encontrar_ruta(inicio, objetivo)
    if ruta is None:
        print("No se pudo encontrar una ruta válida.")
        return
    print("Ruta planificada:", ruta)
    for paso, posicion in enumerate(ruta):
        print("Paso {}: Robot se mueve a la posición {}".format(paso + 1, posicion))
        # Simular detección de obstáculos o desviación de la ruta planificada
        if paso == 2:
            print("¡Obstáculo detectado!")
            print("Activando replanificación...")
            nueva_ruta = encontrar_ruta(posicion, objetivo)
            if nueva_ruta is None:
                print("No se pudo encontrar una nueva ruta válida.")
                return
            ruta = nueva_ruta
            print("Nueva ruta planificada:", ruta)

# Definir el punto de inicio y el punto objetivo
inicio = (0, 0)
objetivo = (4, 4)

# Iniciar la navegación del robot
navegar(inicio, objetivo)