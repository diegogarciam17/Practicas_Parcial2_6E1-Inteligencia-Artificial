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

class InferenciaLogica:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def modus_ponens(self, p, q):
        # Si tenemos p y la regla p => q en la base de conocimiento, entonces podemos inferir q
        if self.base_conocimiento.consultar(p) and self.base_conocimiento.consultar(f"{p} => {q}"):
            return q
        else:
            return None

# Clase para representar la base de conocimiento
class BaseConocimiento:
    def __init__(self):
        self.hechos = []

    def agregar_hecho(self, hecho):
        self.hechos.append(hecho)

    def consultar(self, hecho):
        return hecho in self.hechos

# Crear la base de conocimiento
base_conocimiento = BaseConocimiento()
base_conocimiento.agregar_hecho("p")
base_conocimiento.agregar_hecho("p => q")

# Crear el motor de inferencia
motor_inferencia = InferenciaLogica(base_conocimiento)

# Realizar inferencia modus ponens
resultado = motor_inferencia.modus_ponens("p", "q")

# Mostrar el resultado
if resultado:
    print(f"Se dedujo la proposición: {resultado}")
else:
    print("La inferencia no fue posible.")