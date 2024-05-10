# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Satisfacción de Restricciones-Propagación de Restricciones

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def propagacion_restricciones(ac3, restricciones, dominios):
    cola_trabajo = ac3(restricciones, dominios)
    while cola_trabajo:
        (i, j) = cola_trabajo.pop(0)
        if revisar_arco(i, j, dominios):
            for k in restricciones[j]:
                if k != i:
                    cola_trabajo.append((j, k))
    return dominios

def ac3(restricciones, dominios):
    cola_trabajo = []
    for i in restricciones:
        for j in restricciones[i]:
            cola_trabajo.append((i, j))
    return cola_trabajo

def revisar_arco(i, j, dominios):
    revisado = False
    valores_restantes = list(dominios[i])
    for x in dominios[i]:
        si_puede_asignar = False
        for y in dominios[j]:
            if restriccion_satisfecha(i, j, x, y):
                si_puede_asignar = True
                break
        if not si_puede_asignar:
            valores_restantes.remove(x)
            revisado = True
    dominios[i] = valores_restantes
    return revisado

def restriccion_satisfecha(i, j, x, y):
    # Supongamos que aquí se implementan las restricciones específicas del problema
    return True

# Ejemplo de restricciones y dominios
restricciones = {'A': ['B'], 'B': ['A']}
dominios = {'A': [1, 2, 3], 'B': [1, 2, 3]}

# Ejecutar la propagación de restricciones con AC-3
dominios_actualizados = propagacion_restricciones(ac3, restricciones, dominios)
print("Dominios actualizados después de la propagación de restricciones:", dominios_actualizados)
