# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Gramáticas Probab. Independ. del Contexto
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

from nltk import PCFG, ViterbiParser
from nltk.grammar import CFG
from nltk.parse import pchart

# Definir una gramática independiente del contexto
cfg_grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | NP PP
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'man' | 'dog' | 'cat'
    V -> 'chased' | 'saw'
    P -> 'in' | 'on'
""")

# Definir las probabilidades de las reglas de producción
pcfg_productions = """
    S -> NP VP [1.0]
    NP -> Det N [0.7] | NP PP [0.3]
    VP -> V NP [0.4] | VP PP [0.6]
    PP -> P NP [1.0]
    Det -> 'the' [0.6] | 'a' [0.4]
    N -> 'man' [0.3] | 'dog' [0.4] | 'cat' [0.3]
    V -> 'chased' [0.5] | 'saw' [0.5]
    P -> 'in' [0.6] | 'on' [0.4]
"""

# Crear una gramática probabilística independiente del contexto (PCFG)
pcfg_grammar = PCFG.fromstring(pcfg_productions)

# Crear un analizador Viterbi para la PCFG
parser = ViterbiParser(pcfg_grammar, trace=2)

# Frase de entrada para analizar
sentence = "the man saw a dog on the cat"

# Tokenizar la frase de entrada
tokens = sentence.split()

# Analizar la frase y mostrar el árbol de análisis más probable
for tree in parser.parse(tokens):
    print(tree)