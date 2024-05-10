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

def diagnosticar_sintomas(sintomas, reglas):
    for enfermedad, condiciones in reglas.items():
        if all(condicion in sintomas for condicion in condiciones):
            return enfermedad
    return "No se pudo diagnosticar la enfermedad"

def causas_efectos(evento, reglas):
    if evento in reglas:
        return reglas[evento]
    return "No se encontraron causas para el evento"

# Reglas de diagnóstico
reglas_diagnosticos = {
    "faringitis": ["fiebre", "dolor de garganta"],
    "sarampion": ["fiebre", "erupcion cutanea"]
}

# Reglas causales
reglas_causales = {
    "incendio forestal": ["temperaturas altas", "humedad baja"],
    "deslizamiento de tierra": ["cantidad de lluvia alta", "terreno inclinado"]
}

# Ejemplo de diagnóstico
sintomas_paciente = ["fiebre", "dolor de garganta"]
print("Diagnóstico:", diagnosticar_sintomas(sintomas_paciente, reglas_diagnosticos))

# Ejemplo de causa-efecto
evento = "incendio forestal"
print("Causas:", causas_efectos(evento, reglas_causales))