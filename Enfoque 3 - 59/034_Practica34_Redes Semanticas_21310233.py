# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
#Redes Semánticas:
# Ejemplo de red semántica en Python (usando diccionarios)
red_semantica = {
    "animal": ["perro", "gato", "pájaro"],
    "mamífero": ["perro", "gato"],
    "ave": ["pájaro"]
}

# Consultar la red semántica
print(red_semantica["mamífero"])  # Salida: ['perro', 'gato']
print(red_semantica["ave"])       # Salida: ['pájaro']