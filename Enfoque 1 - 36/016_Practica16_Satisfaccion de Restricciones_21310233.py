# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Satisfacción de Restricciones-Problemas de Satisfacción de Restricciones

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Problemas de Satisfacción de Restricciones (CSP, por sus siglas en inglés)
def resolver_csp():
    for a in range(2):
        for b in range(2):
            for c in range(2):
                if a + b + c == 2:
                    return (a, b, c)
    return None

# Ejecutar la función para resolver el CSP
solucion = resolver_csp()
print("Solución encontrada:", solucion)