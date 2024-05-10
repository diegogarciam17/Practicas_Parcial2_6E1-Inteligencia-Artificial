# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
from pyswip import Prolog

def foil(examples):
    prolog = Prolog()
    prolog.assertz(":- use_module(library(foil)).")
    
    for example in examples:
        prolog.assertz(example)
    
    prolog.assertz(":- foil.")
    for result in prolog.query("induce_rules"):
        print(result)

# Ejemplo de datos de entrenamiento
examples = [
    "pos(ex1).",
    "neg(ex2).",
    "pos(ex3).",
    "neg(ex4)."
]

# Ejecutar FOIL en los ejemplos
foil(examples)