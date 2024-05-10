# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Traducción Automática Estadística
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import nltk
from nltk.translate import Alignment, AlignedSent

# Definir textos en dos idiomas
text_es = "Hola, ¿cómo estás?"
text_en = "Hello, how are you?"

# Tokenizar los textos en palabras
tokens_es = nltk.word_tokenize(text_es)
tokens_en = nltk.word_tokenize(text_en)

# Crear oraciones alineadas
aligned_sent = AlignedSent(tokens_es, tokens_en)

# Mostrar la alineación resultante
print("Alineación de palabras:")
print(aligned_sent.alignment)