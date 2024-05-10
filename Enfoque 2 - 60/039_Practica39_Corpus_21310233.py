# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Modelo Probabilístico del Lenguaje: Corpus
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

from collections import defaultdict

class Corpus:
    def __init__(self):
        self.data = defaultdict(int)

    def add_text(self, text):
        words = text.split()
        for word in words:
            self.data[word] += 1

    def word_count(self, word):
        return self.data[word]

    def total_words(self):
        return sum(self.data.values())

    def word_probability(self, word):
        return self.word_count(word) / self.total_words()

# Ejemplo de uso
corpus = Corpus()
corpus.add_text("El gato está en la casa")
corpus.add_text("La casa está cerca del parque")
corpus.add_text("El perro está en el parque")
corpus.add_text("La casa es grande")

word = "casa"
print("Número de ocurrencias de la palabra '{}' en el corpus: {}".format(word, corpus.word_count(word)))
print("Probabilidad de la palabra '{}' en el corpus: {:.4f}".format(word, corpus.word_probability(word)))