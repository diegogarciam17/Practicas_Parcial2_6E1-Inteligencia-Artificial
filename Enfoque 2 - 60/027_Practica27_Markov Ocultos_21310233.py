# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Modelos de Markov Ocultos
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

from hmmlearn import hmm
import numpy as np

# Definir los parámetros del modelo HMM
n_components = 2  # Número de estados ocultos
model = hmm.GaussianHMM(n_components=n_components)

# Generar datos de ejemplo
np.random.seed(42)
X = np.concatenate([np.random.normal(0, 1, (100, 2)), np.random.normal(5, 1, (100, 2))])

# Ajustar el modelo HMM a los datos
model.fit(X)

# Generar una secuencia de observaciones
observations, states = model.sample(10)

# Inferir la secuencia de estados ocultos más probable
estimated_states = model.predict(observations)

print("Secuencia de observaciones generada por el modelo HMM:")
print(observations)
print("\nSecuencia de estados ocultos inferidos:")
print(estimated_states)