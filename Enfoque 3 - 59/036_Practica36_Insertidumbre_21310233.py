# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

class UncertaintyReasoner:
    def __init__(self):
        self.facts = {}

    def add_fact(self, fact, certainty):
        self.facts[fact] = certainty

    def infer(self, new_fact, certainty):
        if new_fact not in self.facts or certainty > self.facts[new_fact]:
            self.facts[new_fact] = certainty
            print("Nuevo hecho inferido:", new_fact, "con certeza:", certainty)
        else:
            print("El hecho ya está presente en la base de conocimientos con una certeza mayor.")

    def retract(self, fact):
        if fact in self.facts:
            del self.facts[fact]
            print("Hecho retraído:", fact)
        else:
            print("El hecho no está presente en la base de conocimientos.")

# Crear un razonador de incertidumbre
reasoner = UncertaintyReasoner()

# Agregar algunos hechos iniciales con sus niveles de certeza
reasoner.add_fact("pájaros pueden volar", 0.8)
reasoner.add_fact("pájaros tienen alas", 0.9)

# Intentar inferir un nuevo hecho con cierta incertidumbre
reasoner.infer("pájaros pueden volar", 0.7)

# Retraer un hecho existente
reasoner.retract("pájaros tienen alas")

# Intentar inferir un hecho contradictorio con alta certeza
reasoner.infer("pájaros pueden volar", 0.95)