# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

from pyDatalog import pyDatalog

# Definir las reglas lógicas
pyDatalog.create_terms('padre, abuelo, X, Y, Z')

# Reglas lógicas: definición de relaciones entre los términos
+padre('juan', 'pepe')
+padre('pepe', 'juanito')
+padre('pepe', 'maría')
+padre('paco', 'pepe')

abuelo(X, Y) <= padre(X, Z) & padre(Z, Y)

# Consultas lógicas
print(abuelo(X, 'juanito'))
print(abuelo('paco', Y))