# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

import random
import math

# Función objetivo para ilustrar los algoritmos
def objective_function(x):
    return -(x ** 2)

# Algoritmo de Ascenso de Colinas
def hill_climbing(max_iterations, step_size, initial_solution):
    current_solution = initial_solution
    for _ in range(max_iterations):
        next_solution = current_solution + random.uniform(-step_size, step_size)
        if objective_function(next_solution) > objective_function(current_solution):
            current_solution = next_solution
    return current_solution

# Algoritmo de Recocido Simulado
def simulated_annealing(max_iterations, initial_temperature, cooling_rate, initial_solution):
    current_solution = initial_solution
    current_temperature = initial_temperature
    for _ in range(max_iterations):
        next_solution = current_solution + random.uniform(-1, 1)
        delta = objective_function(next_solution) - objective_function(current_solution)
        if delta > 0 or random.random() < math.exp(delta / current_temperature):
            current_solution = next_solution
        current_temperature *= cooling_rate
    return current_solution

# Ejemplo de uso
initial_solution = 0
max_iterations = 1000
step_size = 0.1
initial_temperature = 100.0
cooling_rate = 0.95

print("Hill Climbing:", hill_climbing(max_iterations, step_size, initial_solution))
print("Simulated Annealing:", simulated_annealing(max_iterations, initial_temperature, cooling_rate, initial_solution))