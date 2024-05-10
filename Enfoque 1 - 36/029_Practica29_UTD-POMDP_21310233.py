# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Utilidad y Toma de Decisiones-MDP Parcialmente Observable (POMDP)
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import numpy as np

class POMDP:
    def __init__(self, num_estados, num_acciones, num_obs):
        self.num_estados = num_estados
        self.num_acciones = num_acciones
        self.num_obs = num_obs
        self.T = np.random.rand(num_estados, num_acciones, num_estados)  # Función de transición
        self.O = np.random.rand(num_estados, num_acciones, num_obs)       # Función de observación
        self.R = np.random.rand(num_estados, num_acciones)                # Función de recompensa
    
    # Normalizar las probabilidades en la matriz de observación
        for s in range(num_estados):
            for a in range(num_acciones):
                self.O[s, a] /= np.sum(self.O[s, a])

# Crear un POMDP de ejemplo
num_estados = 5
num_acciones = 3
num_obs = 2
pomdp = POMDP(num_estados, num_acciones, num_obs)

# Función de creencia inicial
def creencia_inicial(num_estados):
    return np.ones(num_estados) / num_estados

# Actualizar la creencia dada una observación
def actualizar_creencia(pomdp, creencia, accion, observacion):
    nueva_creencia = np.zeros_like(creencia)
    for s in range(pomdp.num_estados):
        suma = 0
        for s_prime in range(pomdp.num_estados):
            suma += pomdp.T[s, accion, s_prime] * pomdp.O[s_prime, accion, observacion] * creencia[s_prime]
        nueva_creencia[s] = suma
    return nueva_creencia / np.sum(nueva_creencia)

# Ejemplo de navegación en un laberinto
creencia = creencia_inicial(num_estados)
for t in range(10):
    accion = np.random.randint(num_acciones)
    observacion = pomdp.observacion(np.argmax(creencia), accion)
    creencia = actualizar_creencia(pomdp, creencia, accion, observacion)
    print("Tiempo {}: Acción: {}, Observación: {}, Creencia: {}".format(t+1, accion, observacion, creencia))