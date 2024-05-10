# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
# Definir un diccionario para representar un marco de acción
accion_marco = {
    "nombre": "ir_al_supermercado",
    "actor": "yo",
    "objetivo": "comprar alimentos",
    "recursos": ["dinero", "lista de compras"],
    "efectos": ["adquirir alimentos", "gastar dinero"],
    "duración": "1 hora"
}

# Función para imprimir un marco de acción
def imprimir_marco(marco):
    print("Nombre:", marco["nombre"])
    print("Actor:", marco["actor"])
    print("Objetivo:", marco["objetivo"])
    print("Recursos:", marco["recursos"])
    print("Efectos:", marco["efectos"])
    print("Duración estimada:", marco["duración"])

# Imprimir el marco de acción
print("Marco de acción:")
imprimir_marco(accion_marco)