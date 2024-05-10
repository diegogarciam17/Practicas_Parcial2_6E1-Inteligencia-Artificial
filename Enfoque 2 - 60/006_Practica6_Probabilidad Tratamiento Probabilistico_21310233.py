# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Tratamiento Probabilístico del Lenguaje
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

from collections import Counter
import nltk
from nltk.corpus import brown

# Descargar el corpus 'brown' si no está disponible
nltk.download('brown')

# Obtener las palabras del corpus Brown
words = brown.words()

# Construir un modelo de bigramas
bigrams = list(nltk.bigrams(words))

# Contar la frecuencia de cada bigrama
bigram_counts = Counter(bigrams)

# Función para calcular la probabilidad de una palabra dado el bigrama anterior
def probability(word, prev_word):
    bigram = (prev_word, word)
    return bigram_counts[bigram] / sum(bigram_counts.values())

# Ejemplo de uso
prev_word = 'the'
word = 'cat'
prob = probability(word, prev_word)
print(f'La probabilidad de la palabra "{word}" dado el bigrama "{prev_word} {word}" es: {prob:.4f}')