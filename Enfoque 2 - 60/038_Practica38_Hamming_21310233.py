# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Hamming, Hopfield, Hebb, Boltzmann, ...
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

#Algoritmo de Hebb
import numpy as np

class HebbianNetwork:
    def __init__(self, num_neurons):
        self.num_neurons = num_neurons
        self.weights = np.zeros((num_neurons, num_neurons))

    def train(self, patterns):
        for pattern in patterns:
            pattern_row = np.reshape(pattern, (1, self.num_neurons))
            self.weights += np.dot(pattern_row.T, pattern_row)

    def predict(self, input_pattern):
        return np.sign(np.dot(input_pattern, self.weights))

# Ejemplo de uso
patterns = np.array([
    [-1, 1, -1, 1],
    [1, -1, 1, -1],
    [-1, -1, -1, -1]
])
num_neurons = len(patterns[0])
hebb_net = HebbianNetwork(num_neurons)
hebb_net.train(patterns)

input_pattern = np.array([1, 1, 1, -1])
predicted_pattern = hebb_net.predict(input_pattern)
print("Patrón de entrada:", input_pattern)
print("Patrón predicho:", predicted_pattern)