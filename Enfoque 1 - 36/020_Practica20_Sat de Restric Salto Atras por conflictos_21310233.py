# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Satisfacción de Restricciones-Salto Atrás Dirigido por Conflictos

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

#Salto Atrás Dirigido por Conflictos (Conflict-Directed Backjumping, CB)
def conflict_directed_backjumping(csp):
    asignacion = {}
    return cb_recursivo(csp, asignacion)

def cb_recursivo(csp, asignacion):
    if len(asignacion) == len(csp):  # Si se ha asignado un valor a todas las variables, se ha encontrado una solución
        return asignacion
    
    variable = seleccionar_variable_sin_asignar(csp, asignacion)
    for valor in ordenar_valores(csp, variable):
        if es_valor_consistente(valor, variable, asignacion, csp):
            asignacion[variable] = valor
            resultado = cb_recursivo(csp, asignacion)
            if resultado:
                return resultado
            asignacion.pop(variable)  # Retroceder (backtrack)
    
    return None

def seleccionar_variable_sin_asignar(csp, asignacion):
    for variable in csp:
        if variable not in asignacion:
            return variable

def ordenar_valores(csp, variable):
    # Podrías implementar algún criterio de ordenación aquí
    return csp[variable]

def es_valor_consistente(valor, variable, asignacion, csp):
    # Verificar si el valor es consistente con las restricciones
    # Puedes implementar esta función según las restricciones específicas del problema
    return True

# Ejemplo de un problema CSP representado como un diccionario de variables y sus dominios
csp = {
    'A': [1, 2, 3],
    'B': [1, 2, 3],
    'C': [1, 2, 3]
}

# Ejecutar la búsqueda con Salto Atrás Dirigido por Conflictos
solucion = conflict_directed_backjumping(csp)
print("Solución encontrada:", solucion)
