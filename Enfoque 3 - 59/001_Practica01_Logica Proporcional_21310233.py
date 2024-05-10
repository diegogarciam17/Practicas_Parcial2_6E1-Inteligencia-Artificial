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

# Definición de variables booleanas
p = True
q = False

# Operador AND: True si ambos son True, de lo contrario False
resultado_and = p and q
print("p AND q =", resultado_and)

# Operador OR: True si al menos uno es True, de lo contrario False
resultado_or = p or q
print("p OR q =", resultado_or)

# Operador NOT: Niega el valor de la variable
resultado_not_p = not p
print("NOT p =", resultado_not_p)

# Expresión lógica más compleja usando paréntesis para agrupar operaciones
expresion_compleja = (p or q) and (not p)
print("(p OR q) AND (NOT p) =", expresion_compleja)

# Otra expresión lógica más compleja
expresion_compleja2 = (p and q) or (not p and q)
print("(p AND q) OR (NOT p AND q) =", expresion_compleja2)