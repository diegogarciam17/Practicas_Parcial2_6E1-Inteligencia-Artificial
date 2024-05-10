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

from sympy import symbols, And, Or, Not, Implies, Equivalent, satisfiable, ask

# Definir las variables proposicionales
p, q = symbols('p q')

# Ejemplo de proposiciones
proposicion1 = And(Implies(p, q), Implies(q, p))
proposicion2 = Or(Not(p), q)

# Crear la proposición de equivalencia
proposicion_equivalente = Equivalent(proposicion1, proposicion2)

# Verificar equivalencia
if ask(proposicion_equivalente):
    print("Las proposiciones son equivalentes.")
else:
    print("Las proposiciones no son equivalentes.")

# Verificar validez de proposición 1
if ask(proposicion1):
    print("La proposición 1 es válida.")
else:
    print("La proposición 1 no es válida.")

# Verificar satisfacibilidad de proposición 2
if satisfiable(proposicion2):
    print("La proposición 2 es satisfacible.")
else:
    print("La proposición 2 no es satisfacible.")

