# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Utilidad y Toma de Decisiones-Valor de la Información
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def calcular_voi(valor_informacion, rendimiento_sin_info):
    rendimiento_con_info = rendimiento_sin_info + valor_informacion
    voi = rendimiento_con_info - rendimiento_sin_info
    return voi

# Rendimiento esperado de las acciones sin información adicional
rendimiento_sin_info_A = 1000
rendimiento_sin_info_B = 800

# Rendimiento esperado de las acciones con información adicional
rendimiento_con_info_A = 1200
rendimiento_con_info_B = 900

# Calcular el valor de la información para cada acción
voi_A = calcular_voi(rendimiento_con_info_A - rendimiento_sin_info_A, rendimiento_sin_info_A)
voi_B = calcular_voi(rendimiento_con_info_B - rendimiento_sin_info_B, rendimiento_sin_info_B)

# Imprimir los resultados
print("Valor de la información para la acción A:", voi_A)
print("Valor de la información para la acción B:", voi_B)