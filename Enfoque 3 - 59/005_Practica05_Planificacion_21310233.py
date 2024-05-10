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

class Enfermedad:
    def __init__(self, nombre, sintomas):
        self.nombre = nombre
        self.sintomas = sintomas

# Base de conocimiento de enfermedades y sus síntomas
enfermedades = [
    Enfermedad("Resfriado", ["Tos", "Congestión nasal", "Estornudos"]),
    Enfermedad("Gripe", ["Fiebre", "Dolor de cabeza", "Fatiga"]),
    Enfermedad("Alergia", ["Picazón en los ojos", "Estornudos", "Congestión nasal"])
]

# Función para diagnosticar enfermedades basadas en los síntomas
def diagnosticar(sintomas):
    enfermedades_diagnosticadas = []
    for enfermedad in enfermedades:
        if all(sintoma in enfermedad.sintomas for sintoma in sintomas):
            enfermedades_diagnosticadas.append(enfermedad.nombre)
    return enfermedades_diagnosticadas

# Síntomas del paciente
sintomas_paciente = ["Estornudos", "Congestión nasal"]

# Realizar diagnóstico
enfermedades_diagnosticadas = diagnosticar(sintomas_paciente)

# Mostrar resultados
if enfermedades_diagnosticadas:
    print("El paciente podría tener:", ", ".join(enfermedades_diagnosticadas))
else:
    print("No se pudo determinar la enfermedad.")