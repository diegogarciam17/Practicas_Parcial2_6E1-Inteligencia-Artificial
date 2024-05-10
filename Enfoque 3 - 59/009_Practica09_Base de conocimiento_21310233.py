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

class BaseConocimiento:
    def __init__(self):
        self.hechos = []
        self.reglas = []

    def agregar_hecho(self, hecho):
        self.hechos.append(hecho)

    def agregar_regla(self, regla):
        self.reglas.append(regla)

    def consultar(self, hecho):
        for regla in self.reglas:
            if all(antecedente in self.hechos for antecedente in regla.antecedente):
                if regla.consecuente == hecho:
                    return True
        return False

class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente
        self.consecuente = consecuente

# Crear una base de conocimiento
base_conocimiento = BaseConocimiento()

# Agregar hechos
base_conocimiento.agregar_hecho("El cielo está nublado")
base_conocimiento.agregar_hecho("Es temporada de lluvias")
base_conocimiento.agregar_hecho("La temperatura es baja")

# Definir reglas
regla1 = Regla(["El cielo está nublado", "Es temporada de lluvias"], "Probabilidad de lluvia alta")
regla2 = Regla(["La temperatura es baja"], "Probabilidad de lluvia moderada")

# Agregar reglas a la base de conocimiento
base_conocimiento.agregar_regla(regla1)
base_conocimiento.agregar_regla(regla2)

# Consultar la base de conocimiento
hecho_a_consultar = "Probabilidad de lluvia alta"
resultado = base_conocimiento.consultar(hecho_a_consultar)

# Mostrar el resultado
if resultado:
    print(f"La base de conocimiento indica que: {hecho_a_consultar}")
else:
    print(f"No se puede inferir {hecho_a_consultar} a partir de la base de conocimiento.")