# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Satisfacción de Restricciones-Comprobación Hacia Delante

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def forward_checking(grafo, dominios):
    asignacion = {}
    return forward_checking_recursivo(grafo, asignacion, dominios)

def forward_checking_recursivo(grafo, asignacion, dominios):
    if len(asignacion) == len(grafo):  # Si se ha asignado un color a todos los nodos, se ha encontrado una solución
        return asignacion
    
    nodo = seleccionar_nodo_sin_color(asignacion, grafo)
    for color in dominios[nodo]:
        if es_color_valido(nodo, color, asignacion, grafo):
            asignacion[nodo] = color
            dominios_reducidos = reducir_dominios(nodo, color, asignacion, grafo, dominios)
            resultado = forward_checking_recursivo(grafo, asignacion, dominios_reducidos)
            if resultado:
                return resultado
            asignacion.pop(nodo)  # Retroceder (backtrack)
    return None

def seleccionar_nodo_sin_color(asignacion, grafo):
    for nodo in grafo:
        if nodo not in asignacion:
            return nodo

def es_color_valido(nodo, color, asignacion, grafo):
    for vecino in grafo[nodo]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

def reducir_dominios(nodo, color, asignacion, grafo, dominios):
    dominios_reducidos = dominios.copy()
    for vecino in grafo[nodo]:
        if vecino not in asignacion:
            if color in dominios_reducidos[vecino]:
                dominios_reducidos[vecino].remove(color)
    return dominios_reducidos

# Ejemplo de grafo representado como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Colores disponibles para asignar a los nodos
dominios = {
    'A': ['rojo', 'verde', 'azul'],
    'B': ['rojo', 'verde', 'azul'],
    'C': ['rojo', 'verde', 'azul'],
    'D': ['rojo', 'verde', 'azul']
}

# Ejecutar la comprobación hacia adelante para encontrar una asignación de colores válida
solucion = forward_checking(grafo, dominios)

if solucion:
    print("Asignación de colores encontrada:")
    for nodo, color in solucion.items():
        print(f"Nodo {nodo}: {color}")
else:
    print("No se encontró una asignación de colores válida.")