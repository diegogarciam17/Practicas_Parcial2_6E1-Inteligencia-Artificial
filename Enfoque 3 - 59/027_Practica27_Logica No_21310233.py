# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
class NonMonotonicLogicSystem:
    def __init__(self):
        self.knowledge_base = set()

    def add_fact(self, fact):
        self.knowledge_base.add(fact)

    def retract_fact(self, fact):
        if fact in self.knowledge_base:
            self.knowledge_base.remove(fact)

    def query(self, fact):
        return fact in self.knowledge_base


# Ejemplo de uso
logic_system = NonMonotonicLogicSystem()

# Agregar algunos hechos iniciales
logic_system.add_fact("Puede volar un pájaro")
logic_system.add_fact("Un avestruz no puede volar")

# Consulta inicial
print("¿Puede volar un pájaro?", logic_system.query("Puede volar un pájaro"))

# Agregar nueva información
logic_system.add_fact("Un pingüino no puede volar")

# Consulta después de agregar nueva información
print("¿Puede volar un pingüino?", logic_system.query("Un pingüino no puede volar"))

# Retractar información
logic_system.retract_fact("Un avestruz no puede volar")

# Consulta después de retractar información
print("¿Puede volar un avestruz?", logic_system.query("Un avestruz no puede volar"))