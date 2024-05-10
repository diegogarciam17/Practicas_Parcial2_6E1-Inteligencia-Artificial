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

import itertools

# Definir la proposición lógica (p and q) or (not p)
proposicion = lambda p, q: (p and q) or (not p)

# Encabezado de la tabla
print("p\tq\tp and q\t¬p\t(p and q) or (¬p)")

# Enumerar todas las combinaciones de valores de verdad para p y q
valores_de_verdad = [True, False]
for p, q in itertools.product(valores_de_verdad, repeat=2):
    resultado_pq = p and q
    resultado_not_p = not p
    resultado_final = proposicion(resultado_pq, resultado_not_p)
    print(f"{p}\t{q}\t{resultado_pq}\t{resultado_not_p}\t{resultado_final}")