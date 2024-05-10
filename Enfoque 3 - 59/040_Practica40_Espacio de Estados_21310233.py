# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
class EstadoLaberinto:
    def __init__(self, posicion):
        self.posicion = posicion

    def __eq__(self, other):
        return self.posicion == other.posicion

    def __hash__(self):
        return hash(self.posicion)

class Laberinto:
    def __init__(self, matriz):
        self.matriz = matriz

    def es_valido(self, posicion):
        x, y = posicion
        return 0 <= x < len(self.matriz) and 0 <= y < len(self.matriz[0]) and self.matriz[x][y] == 0

    def obtener_vecinos(self, estado):
        movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Movimientos arriba, abajo, derecha e izquierda
        vecinos = []
        for dx, dy in movimientos:
            nueva_posicion = (estado.posicion[0] + dx, estado.posicion[1] + dy)
            if self.es_valido(nueva_posicion):
                vecinos.append(EstadoLaberinto(nueva_posicion))
        return vecinos

# Definir el laberinto
laberinto = Laberinto([
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0]
])

# Definir estado inicial y estado objetivo
estado_inicial = EstadoLaberinto((0, 0))
estado_objetivo = EstadoLaberinto((4, 4))

# Obtener vecinos del estado inicial
vecinos_estado_inicial = laberinto.obtener_vecinos(estado_inicial)
print("Vecinos del estado inicial:", vecinos_estado_inicial)