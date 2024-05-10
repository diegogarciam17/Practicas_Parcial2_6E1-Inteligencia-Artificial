# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir variables de entrada
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')

# Definir variable de salida
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definir funciones de membresía
calidad['baja'] = fuzz.trimf(calidad.universe, [0, 0, 5])
calidad['media'] = fuzz.trimf(calidad.universe, [0, 5, 10])
calidad['alta'] = fuzz.trimf(calidad.universe, [5, 10, 10])

servicio['bajo'] = fuzz.trimf(servicio.universe, [0, 0, 5])
servicio['medio'] = fuzz.trimf(servicio.universe, [0, 5, 10])
servicio['alto'] = fuzz.trimf(servicio.universe, [5, 10, 10])

propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# Visualizar las funciones de membresía
calidad.view()
servicio.view()
propina.view()

# Definir reglas
regla1 = ctrl.Rule(calidad['baja'] | servicio['bajo'], propina['baja'])
regla2 = ctrl.Rule(calidad['media'] & servicio['medio'], propina['media'])
regla3 = ctrl.Rule(calidad['alta'] | servicio['alto'], propina['alta'])

# Crear sistema de control difuso
sistema_ctrl = ctrl.ControlSystem([regla1, regla2, regla3])

# Simular el sistema de control
propina_prediccion = ctrl.ControlSystemSimulation(sistema_ctrl)

# Pasar entradas al sistema
propina_prediccion.input['calidad'] = 6.5
propina_prediccion.input['servicio'] = 9.8

# Computar la salida
propina_prediccion.compute()

# Imprimir el resultado
print("Propina prevista:", propina_prediccion.output['propina'])

# Visualizar el resultado
propina.view(sim=propina_prediccion)