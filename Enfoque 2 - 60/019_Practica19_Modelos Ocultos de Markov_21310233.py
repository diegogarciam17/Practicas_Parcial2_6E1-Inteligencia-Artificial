# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Modelos Ocultos de Markov
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

from hmmlearn import hmm
import numpy as np

# Definir el modelo oculto de Markov
model = hmm.GaussianHMM(n_components=2, covariance_type="diag")

# Secuencia de observaciones
X = np.array([[1.0], [0.9], [1.1], [2.0]])

# Ajustar el modelo al conjunto de datos de observaciones
model.fit(X)

# Calcular la secuencia de estados más probable
logprob, state_sequence = model.decode(X)

print("Secuencia de estados más probable:")
print(state_sequence)