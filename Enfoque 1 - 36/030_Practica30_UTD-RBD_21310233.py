# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Utilidad y Toma de Decisiones-Red Bayesiana Dinámica
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.factors.discrete import TabularCPD

# Crear la estructura de la DBN
dbn = DBN()

# Agregar los nodos de variables latentes y observadas con índices de tiempo
dbn.add_nodes_from([('L0', 0), ('L1', 1), ('X0', 0), ('X1', 1)])

# Agregar arcos temporales (dependencias entre variables en diferentes capas)
dbn.add_edges_from([('L0', 'L1'), ('L0', 'X0'), ('L1', 'X1')])

# Definir las distribuciones de probabilidad condicional (CPDs)
cpd_l0 = TabularCPD(variable='L0', variable_card=2, values=[[0.5], [0.5]])
cpd_l1 = TabularCPD(variable='L1', variable_card=2, values=[[0.7, 0.3], [0.3, 0.7]],
                    evidence=['L0'], evidence_card=[2])
cpd_x0 = TabularCPD(variable='X0', variable_card=2, values=[[0.2, 0.8], [0.8, 0.2]],
                    evidence=['L0'], evidence_card=[2])
cpd_x1 = TabularCPD(variable='X1', variable_card=2, values=[[0.3, 0.7], [0.7, 0.3]],
                    evidence=['L1'], evidence_card=[2])

# Asociar las CPDs a los nodos correspondientes
dbn.add_cpds(cpd_l0, cpd_l1, cpd_x0, cpd_x1)

# Verificar la consistencia del modelo
print(dbn.check_model())