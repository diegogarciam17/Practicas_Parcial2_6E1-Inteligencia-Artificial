# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
from pysat.solvers import Glucose3
from pysat.formula import CNF

class SATPlan:
    def __init__(self, initial_state, goal_state, actions):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions

    def convert_to_sat(self):
        formula = CNF()

        # Agregar las cláusulas para el estado inicial
        for prop in self.initial_state:
            formula.append([prop])

        # Agregar las cláusulas para el estado objetivo
        for prop in self.goal_state:
            formula.append([-prop])

        # Agregar las cláusulas para las acciones
        for action in self.actions:
            formula.extend(action.to_clauses())

        return formula

    def plan(self):
        sat = Glucose3()

        # Convertir el problema de planificación a una instancia SAT
        formula = self.convert_to_sat()

        # Agregar cláusulas al solucionador SAT
        for clause in formula.clauses:
            sat.add_clause(clause)

        # Resolver el problema SAT
        if sat.solve():
            # Se encontró una solución, extraer el plan
            model = sat.get_model()
            plan = [action for action in self.actions if action.is_in_model(model)]
            return plan
        else:
            return None

class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

    def to_clauses(self):
        # Generar cláusulas para la acción
        clauses = []
        for effect in self.effects:
            clause = [-prop for prop in self.preconditions] + [effect]
            clauses.append(clause)
        return clauses

    def is_in_model(self, model):
        # Verificar si la acción está en el modelo
        return any(prop in model for prop in self.effects)

# Ejemplo de uso
initial_state = [1, 2]  # Estado inicial: [1, 2]
goal_state = [-3]       # Estado objetivo: [-3]
actions = [
    Action('Action1', [1], [3]),  # Action1: {1} -> {3}
    Action('Action2', [2], [4]),  # Action2: {2} -> {4}
    Action('Action3', [3], [5]),  # Action3: {3} -> {5}
    Action('Action4', [4], [6]),  # Action4: {4} -> {6}
    Action('Action5', [5, 6], [7]),  # Action5: {5, 6} -> {7}
]

sat_plan = SATPlan(initial_state, goal_state, actions)
plan = sat_plan.plan()
print("Plan:", [action.name for action in plan] if plan else "No se encontró plan.")