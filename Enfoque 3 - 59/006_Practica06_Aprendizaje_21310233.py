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

class ClasificadorFlores:
    def __init__(self):
        self.conocimiento = [
            {"especie": "Setosa", "longitud_petalo": (0, 2), "ancho_petalo": (0, 0.7)},
            {"especie": "Versicolor", "longitud_petalo": (2.5, 5), "ancho_petalo": (0.7, 1.3)},
            {"especie": "Virginica", "longitud_petalo": (4.5, 7), "ancho_petalo": (1.3, 2.5)}
        ]

    def clasificar(self, longitud_petalo, ancho_petalo):
        for regla in self.conocimiento:
            if (regla["longitud_petalo"][0] <= longitud_petalo <= regla["longitud_petalo"][1] and
                regla["ancho_petalo"][0] <= ancho_petalo <= regla["ancho_petalo"][1]):
                return regla["especie"]
        return "Desconocida"

# Crear el clasificador
clasificador = ClasificadorFlores()

# Ejemplos de características de flores
ejemplos = [
    {"longitud_petalo": 5.1, "ancho_petalo": 0.9},
    {"longitud_petalo": 3.5, "ancho_petalo": 1.2},
    {"longitud_petalo": 6.2, "ancho_petalo": 2.1}
]

# Clasificar las flores
for ejemplo in ejemplos:
    especie = clasificador.clasificar(ejemplo["longitud_petalo"], ejemplo["ancho_petalo"])
    print("Longitud del pétalo:", ejemplo["longitud_petalo"], "- Ancho del pétalo:", ejemplo["ancho_petalo"], "- Especie:", especie)