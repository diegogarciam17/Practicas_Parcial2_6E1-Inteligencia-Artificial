# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Lógica Modal
class Mundo:
    def __init__(self, nombre):
        self.nombre = nombre

class Agente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conoce = set()

    def conoce_mundo(self, mundo):
        self.conoce.add(mundo.nombre)

# Crear mundos y agentes
mundo_a = Mundo("A")
mundo_b = Mundo("B")
agente_1 = Agente("Agente 1")

# El agente 1 conoce el mundo A
agente_1.conoce_mundo(mundo_a)

# Verificar si el agente conoce el mundo B
print("¿El agente 1 conoce el mundo B?", mundo_b.nombre in agente_1.conoce)