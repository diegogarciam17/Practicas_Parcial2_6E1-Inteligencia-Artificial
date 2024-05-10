# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Satisfacción de Restricciones-Búsqueda Local: Mínimos-Conflictos

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import random

def minimos_conflictos(csp, max_iter):
    asignacion = inicializar_asignacion(csp)
    for _ in range(max_iter):
        conflicto_variable = encontrar_conflicto_variable(asignacion, csp)
        if conflicto_variable is None:
            return asignacion  # Se encontró una solución
        asignar_minimo_conflicto(conflicto_variable, asignacion, csp)
    return None  # No se encontró una solución dentro del número máximo de iteraciones

def inicializar_asignacion(csp):
    asignacion = {}
    for variable in csp:
        asignacion[variable] = random.choice(csp[variable])
    return asignacion

def encontrar_conflicto_variable(asignacion, csp):
    for variable in asignacion:
        if not es_asignacion_valida(variable, asignacion, csp):
            return variable
    return None

def es_asignacion_valida(variable, asignacion, csp):
    valor = asignacion[variable]
    for vecino in csp[variable]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True

def asignar_minimo_conflicto(variable, asignacion, csp):
    mejor_valor = asignacion[variable]
    mejor_conflicto = contar_conflictos(variable, mejor_valor, asignacion, csp)
    for valor in csp[variable]:
        if valor != mejor_valor:
            conflicto_actual = contar_conflictos(variable, valor, asignacion, csp)
            if conflicto_actual < mejor_conflicto:
                mejor_valor = valor
                mejor_conflicto = conflicto_actual
    asignacion[variable] = mejor_valor

def contar_conflictos(variable, valor, asignacion, csp):
    contador = 0
    for vecino in csp[variable]:
        if vecino in asignacion and asignacion[vecino] == valor:
            contador += 1
    return contador

# Ejemplo de un problema CSP representado como un diccionario de variables y sus dominios
csp = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3]
}

# Ejecutar la búsqueda local con mínimos conflictos
max_iter = 1000
solucion = minimos_conflictos(csp, max_iter)
if solucion:
    print("Solución encontrada:", solucion)
else:
    print("No se encontró una solución dentro del número máximo de iteraciones.")
