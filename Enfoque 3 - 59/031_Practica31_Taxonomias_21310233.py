# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
# Definir la taxonomía como un diccionario
taxonomia = {
    "animales": ["perro", "gato", "pájaro"],
    "frutas": ["manzana", "banana", "naranja"],
    "colores": ["rojo", "verde", "azul"]
}

# Función para imprimir la taxonomía
def imprimir_taxonomia(taxonomia):
    for categoria, objetos in taxonomia.items():
        print(categoria + ":")
        for objeto in objetos:
            print("  -", objeto)

# Imprimir la taxonomía
print("Taxonomía:")
imprimir_taxonomia(taxonomia)