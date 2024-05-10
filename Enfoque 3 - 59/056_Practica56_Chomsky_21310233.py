# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

import nltk

# Definir la gramática
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V | V NP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog' | 'rug'
    V -> 'chased' | 'sat'
    P -> 'on' | 'in'
""")

# Crear un parser para la gramática
parser = nltk.ChartParser(grammar)

# Definir una oración para analizar
sentence = "the cat chased the dog".split()

# Realizar el análisis sintáctico de la oración
for tree in parser.parse(sentence):
    print(tree)
    tree.draw()  # Mostrar el árbol de análisis sintáctico6