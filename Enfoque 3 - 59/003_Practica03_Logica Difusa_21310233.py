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

#Lógica Difusa
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear variables lingüísticas
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definir las funciones de pertenencia
calidad.automf(3)
servicio.automf(3)
propina['bajo'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['medio'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alto'] = fuzz.trimf(propina.universe, [13, 25, 25])

# Crear reglas difusas
regla1 = ctrl.Rule(antecedent=((calidad['poor'] | servicio['poor'])),
                   consequent=propina['bajo'], label='regla1')
regla2 = ctrl.Rule(antecedent=((servicio['average'])),
                   consequent=propina['medio'], label='regla2')
regla3 = ctrl.Rule(antecedent=((calidad['good'] | servicio['good'])),
                   consequent=propina['alto'], label='regla3')

# Crear el sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
propina_calculada = ctrl.ControlSystemSimulation(sistema_control)

# Entradas al sistema
propina_calculada.input['calidad'] = 6.5
propina_calculada.input['servicio'] = 9.8

# Evaluar el sistema
propina_calculada.compute()

# Resultado
print("El resultado difuso de la propina es:", propina_calculada.output['propina'])
