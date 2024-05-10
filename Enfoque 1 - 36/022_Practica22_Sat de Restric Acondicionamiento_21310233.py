# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Satisfacción de Restricciones-Acondicionamiento del Corte

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def acondicionamiento_del_corte(csp):
    restricciones_adicionales = generar_restricciones_adicionales(csp)
    csp_actualizado = combinar_csp(csp, restricciones_adicionales)
    return csp_actualizado

def generar_restricciones_adicionales(csp):
    restricciones_adicionales = []
    for variable, vecinos in csp.items():
        for vecino in vecinos:
            restricciones_adicionales.append((variable, vecino))
    return restricciones_adicionales

def combinar_csp(csp, restricciones_adicionales):
    csp_actualizado = csp.copy()
    for restriccion in restricciones_adicionales:
        variable1, variable2 = restriccion
        if variable1 not in csp_actualizado:
            csp_actualizado[variable1] = [variable2]
        else:
            csp_actualizado[variable1].append(variable2)
        if variable2 not in csp_actualizado:
            csp_actualizado[variable2] = [variable1]
        else:
            csp_actualizado[variable2].append(variable1)
    return csp_actualizado

# Ejemplo de un problema CSP representado como un diccionario de variables y sus vecinos
csp = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

# Aplicar el acondicionamiento del corte al problema CSP
csp_actualizado = acondicionamiento_del_corte(csp)
print("CSP actualizado con restricciones adicionales:")
print(csp_actualizado)

