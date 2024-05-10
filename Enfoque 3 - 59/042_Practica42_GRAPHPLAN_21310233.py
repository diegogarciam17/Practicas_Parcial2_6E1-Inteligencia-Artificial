# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
from pddlpy import DomainProblem

class GraphPlan:
    def __init__(self, initial_state, goal_state, actions):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions

    def plan(self):
        frontier = [(self.initial_state, [])]
        explored = set()

        while frontier:
            current_state, plan = frontier.pop(0)
            if current_state == self.goal_state:
                return plan
            explored.add(current_state)
            for action in self.actions:
                next_state = action.apply(current_state)
                if next_state not in explored:
                    frontier.append((next_state, plan + [action]))

        return None

class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

    def apply(self, state):
        if all(condition in state for condition in self.preconditions):
            next_state = set(state)
            next_state.update(self.effects)
            return frozenset(next_state)
        else:
            return state

# Ejemplo de uso
initial_state = frozenset(['A'])
goal_state = frozenset(['D'])
actions = [
    Action('Action1', {'A'}, {'B'}),
    Action('Action2', {'B'}, {'C'}),
    Action('Action3', {'C'}, {'D'})
]

graph_plan = GraphPlan(initial_state, goal_state, actions)
plan = graph_plan.plan()
print("Plan:", [action.name for action in plan] if plan else "No se encontró plan.")