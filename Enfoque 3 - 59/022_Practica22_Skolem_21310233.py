# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

class FuncionSkolem:
    """
    Clase que representa una función de Skolem.
    """

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


def skolemizar(formula):
    """
    Función que aplica la resolución Skolem a una fórmula en lógica de primer orden.

    Args:
        formula (str): La fórmula en lógica de primer orden con cuantificadores existenciales.

    Returns:
        str: La fórmula skolemizada, sin cuantificadores existenciales.
    """
    partes = formula.split("∃")
    resultado = partes[0]  # La primera parte no se modifica

    for parte in partes[1:]:
        # Buscar la posición de la conjunción lógica siguiente
        pos_conjuncion = parte.find("∧")
        if pos_conjuncion != -1:
            variables = parte[:pos_conjuncion].strip()
            resto = parte[pos_conjuncion:].strip()
        else:
            # Si no hay más conjunciones, tomar toda la parte como variables
            variables = parte.strip()
            resto = ""

        # Crear la función de Skolem
        funcion_skolem = FuncionSkolem("S(" + variables + ")")
        # Agregar la función de Skolem al resultado
        resultado += str(funcion_skolem) + (" ∧ " if resto else "") + resto

    return resultado

# Ejemplo de uso
formula_original = "∃x (H(x) ∧ ¬E(x))"
formula_skolemizada = skolemizar(formula_original)
print("Fórmula original:", formula_original)
print("Fórmula skolemizada:", formula_skolemizada)