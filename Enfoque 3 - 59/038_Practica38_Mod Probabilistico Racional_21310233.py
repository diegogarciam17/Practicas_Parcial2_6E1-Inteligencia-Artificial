# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
import numpy as np

class ModeloProbabilistaRacional:
    def __init__(self, creencias):
        self.creencias = creencias

    def actualizar_creencias(self, nueva_informacion):
        self.creencias = nueva_informacion

    def tomar_decision(self, opciones):
        probabilidades = self.calcular_probabilidades(opciones)
        mejor_opcion = np.argmax(probabilidades)
        return opciones[mejor_opcion]

    def calcular_probabilidades(self, opciones):
        probabilidades = []
        for opcion in opciones:
            probabilidad_opcion = self.calcular_probabilidad_opcion(opcion)
            probabilidades.append(probabilidad_opcion)
        return probabilidades

    def calcular_probabilidad_opcion(self, opcion):
        # Por simplicidad, asumimos que la probabilidad de una opción es proporcional a su utilidad percibida
        utilidad_percibida = self.calcular_utilidad_percibida(opcion)
        return utilidad_percibida / sum(self.creencias)

    def calcular_utilidad_percibida(self, opcion):
        # En este ejemplo, la utilidad percibida de una opción es simplemente la suma de los valores de sus características
        return sum(opcion)

# Ejemplo de uso
creencias = [0.3, 0.5, 0.2]  # Creencias iniciales sobre la probabilidad de ocurrencia de ciertos eventos
modelo = ModeloProbabilistaRacional(creencias)

# Nueva información que actualiza las creencias del modelo
nueva_informacion = [0.2, 0.6, 0.2]
modelo.actualizar_creencias(nueva_informacion)

# Opciones disponibles para tomar una decisión
opciones = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]

# El modelo selecciona la mejor opción basada en las creencias actualizadas
mejor_opcion = modelo.tomar_decision(opciones)
print("La mejor opción es:", mejor_opcion)