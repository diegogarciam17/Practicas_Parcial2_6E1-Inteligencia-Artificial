# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
#Lógica Descriptiva:
from owlready2 import *

# Cargar ontología desde un archivo OWL
onto = get_ontology("mi_ontologia.owl").load()

# Consultar la ontología
for clase in onto.classes():
    print(clase)