# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

from z3 import *

# Crear un solucionador
solver = Solver()

# Definir variables
P = Function('P', IntSort(), BoolSort())
Q = Function('Q', IntSort(), BoolSort())
x = Int('x')

# Agregar restricciones
solver.add(ForAll(x, Implies(P(x), Q(x))))

# Verificar la satisfactibilidad
print(solver.check())

# Obtener el modelo si es satisfacible
if solver.check() == sat:
    print(solver.model())