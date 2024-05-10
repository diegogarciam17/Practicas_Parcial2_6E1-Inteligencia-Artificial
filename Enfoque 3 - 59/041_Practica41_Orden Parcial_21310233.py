# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
from pddlpy import DomainProblem

# Definir el dominio y el problema
domain = """
(define (domain planificacion)
  (:requirements :strips :typing)
  (:types accion)

  (:predicates
    (ejecutada ?x - accion)
  )

  (:action accion-1
    :parameters ()
    :precondition ()
    :effect (and (ejecutada accion-1))
  )

  (:action accion-2
    :parameters ()
    :precondition ()
    :effect (and (ejecutada accion-2))
  )
)
"""

problem = """
(define (problem planificacion-1)
  (:domain planificacion)
  (:objects)
  (:init)
  (:goal (and (ejecutada accion-1) (ejecutada accion-2)))
)
"""

# Crear el problema de planificación
planificacion = DomainProblem(domain, problem)

# Resolver el problema
solution = planificacion.solve()

# Imprimir la solución
print("Planificación de Orden Parcial:")
for action in solution:
    print(action)