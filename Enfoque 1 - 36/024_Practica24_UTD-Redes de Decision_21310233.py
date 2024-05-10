# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Utilidad y Toma de Decisiones-Redes de Decisión

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura de la red
modelo = BayesianModel([('A', 'C'), ('B', 'C')])

# Definir las distribuciones de probabilidad condicional (CPDs)
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.3], [0.7]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.4], [0.6]])
cpd_c = TabularCPD(variable='C', variable_card=2, 
                   values=[[0.9, 0.8, 0.7, 0.1], [0.1, 0.2, 0.3, 0.9]],
                   evidence=['A', 'B'], evidence_card=[2, 2])

# Añadir las CPDs al modelo
modelo.add_cpds(cpd_a, cpd_b, cpd_c)

# Verificar la validez del modelo
print("El modelo es válido?", modelo.check_model())

# Realizar inferencia en el modelo
inferencia = VariableElimination(modelo)
resultado = inferencia.query(variables=['C'], evidence={'A': 1, 'B': 0})
print(resultado)
4