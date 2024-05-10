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

# Definición de variables y conjuntos
hombres = ["Diego", "Pedro", "Luis"]
mujeres = ["Ana", "María", "Sofía"]

# Relaciones binarias entre elementos
es_padre = [("Diego", "Pedro"), ("Pedro", "Luis")]
es_madre = [("Ana", "Pedro"), ("María", "Luis")]

# Funciones de pertenencia a conjuntos
def es_hombre(persona):
    return persona in hombres

def es_mujer(persona):
    return persona in mujeres

# Funciones de relación
def es_padre_de(padre, hijo):
    return (padre, hijo) in es_padre

def es_madre_de(madre, hijo):
    return (madre, hijo) in es_madre

# Ejemplos de afirmaciones lógicas
juan_es_padre_de_pedro = es_padre_de("Juan", "Pedro")
ana_es_madre_de_pedro = es_madre_de("Ana", "Pedro")

# Impresión de resultados
print("Diego es padre de Pedro:", juan_es_padre_de_pedro)
print("Ana es madre de Pedro:", ana_es_madre_de_pedro)

# Ejemplo de cuantificación existencial
def existe_padre():
    for hijo in hombres:
        for padre in hombres:
            if es_padre_de(padre, hijo):
                return True
    return False

print("Existe al menos un padre:", existe_padre())

# Ejemplo de cuantificación universal
def todas_mujeres_son_madres():
    for mujer in mujeres:
        if not es_madre_de(mujer, "alguien"):
            return False
    return True

print("Todas las mujeres son madres:", todas_mujeres_son_madres())