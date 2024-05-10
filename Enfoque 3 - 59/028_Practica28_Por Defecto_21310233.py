# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
class DefaultLogicSystem:
    def __init__(self):
        self.default_knowledge = {}
        self.non_default_knowledge = set()

    def add_default_knowledge(self, condition, conclusion):
        condition = tuple(condition)  # Convertir la lista de condiciones en una tupla
        if condition not in self.default_knowledge:
            self.default_knowledge[condition] = conclusion

    def add_non_default_knowledge(self, fact):
        self.non_default_knowledge.add(fact)

    def query(self, fact):
        # Primero, revisamos si el hecho está en el conocimiento no por defecto
        if fact in self.non_default_knowledge:
            return True
        # Si el hecho no está en el conocimiento no por defecto, comprobamos las reglas por defecto
        for condition, conclusion in self.default_knowledge.items():
            if fact in conclusion:
                if all(self.query(c) for c in condition):
                    return True
        # Si no se encuentra en las reglas por defecto, se asume falso
        return False


# Ejemplo de uso
logic_system = DefaultLogicSystem()

# Agregar reglas por defecto
logic_system.add_default_knowledge(["pájaros tienen alas"], ["pueden volar"])

# Agregar hechos no por defecto
logic_system.add_non_default_knowledge("los pingüinos no pueden volar")

# Consulta inicial
print("¿Pueden volar los pingüinos?", logic_system.query("los pingüinos pueden volar"))

# Agregar nueva información no por defecto
logic_system.add_non_default_knowledge("los avestruces pueden correr rápido")

# Consulta después de agregar nueva información no por defecto
print("¿Pueden volar los avestruces?", logic_system.query("los avestruces pueden volar"))

# Agregar nueva regla por defecto
logic_system.add_default_knowledge(["animales tienen alas"], ["pueden volar"])

# Consulta después de agregar nueva regla por defecto
print("¿Pueden volar los animales?", logic_system.query("los animales pueden volar"))
