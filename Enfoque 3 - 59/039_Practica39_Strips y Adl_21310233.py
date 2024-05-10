# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
class Estado:
    def __init__(self, predicados):
        self.predicados = predicados

    def agregar_predicado(self, predicado):
        self.predicados.append(predicado)

    def eliminar_predicado(self, predicado):
        self.predicados.remove(predicado)

class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

    def ejecutar(self, estado):
        if all(predicado in estado.predicados for predicado in self.precondiciones):
            for efecto in self.efectos:
                if efecto.startswith('~'):
                    estado.eliminar_predicado(efecto[1:])
                else:
                    estado.agregar_predicado(efecto)

class PlanificadorSTRIPS:
    def __init__(self, estado_inicial, estado_objetivo, acciones):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo
        self.acciones = acciones

    def planificar(self):
        plan = []
        estado_actual = self.estado_inicial

        while not self.objetivo_cumplido(estado_actual):
            accion = self.seleccionar_accion(estado_actual)
            plan.append(accion)
            accion.ejecutar(estado_actual)

        return plan

    def objetivo_cumplido(self, estado_actual):
        return all(predicado in estado_actual.predicados for predicado in self.estado_objetivo.predicados)

    def seleccionar_accion(self, estado_actual):
        for accion in self.acciones:
            if all(predicado in estado_actual.predicados for predicado in accion.precondiciones):
                return accion

# Definir estados inicial y objetivo
estado_inicial = Estado(['EnCasa', 'SinComida'])
estado_objetivo = Estado(['EnCasa', 'ConComida'])

# Definir acciones disponibles
acciones = [
    Accion('IrAlSupermercado', ['EnCasa'], ['~SinComida', 'ConComida']),
    Accion('RegresarACasa', ['FueraDeCasa'], ['EnCasa']),
]

# Crear el planificador y planificar
planificador = PlanificadorSTRIPS(estado_inicial, estado_objetivo, acciones)
plan = planificador.planificar()

# Mostrar el plan resultante
print("Plan generado:")
for accion in plan:
    print("-", accion.nombre)