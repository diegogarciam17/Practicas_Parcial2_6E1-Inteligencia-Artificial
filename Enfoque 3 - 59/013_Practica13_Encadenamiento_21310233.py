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

# Definir las reglas
reglas = [
    (("p", "q"), "r"),
    (("r", "s"), "t"),
    (("u",), "p"),
    (("v",), "q"),
    (("w",), "s")
]

# Definir los hechos iniciales
hechos = {"u", "v", "w"}

# Encadenamiento hacia adelante
def forward_chaining(reglas, hechos, objetivo):
    while True:
        new_facts = set()
        for antecedentes, consecuente in reglas:
            if all(hecho in hechos for hecho in antecedentes) and consecuente not in hechos:
                new_facts.add(consecuente)
        if not new_facts:
            break
        hechos.update(new_facts)
        if objetivo in hechos:
            return True
    return False

# Encadenamiento hacia atrás
def backward_chaining(reglas, hechos, objetivo):
    if objetivo in hechos:
        return True
    for antecedentes, consecuente in reglas:
        if objetivo == consecuente:
            if all(backward_chaining(reglas, hechos, antecedente) for antecedente in antecedentes):
                return True
    return False

# Ejemplo de uso
objetivo = "t"
print("Encadenamiento hacia adelante:", forward_chaining(reglas, hechos, objetivo))
print("Encadenamiento hacia atrás:", backward_chaining(reglas, hechos, objetivo))