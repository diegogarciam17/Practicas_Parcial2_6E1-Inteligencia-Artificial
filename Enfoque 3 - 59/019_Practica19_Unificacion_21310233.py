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

def unificar(t1, t2, theta):
    """
    Función que realiza la unificación de dos términos t1 y t2.
    Args:
        t1: Primer término a unificar.
        t2: Segundo término a unificar.
        theta: Substituciones actuales.
    Returns:
        Unificación: Un diccionario representando la unificación de los términos si es posible,
                     o None si la unificación no es posible.
    """
    if theta is None:
        return None
    elif t1 == t2:  # Si los términos son iguales, no hay nada que unificar
        return theta
    elif isinstance(t1, str) and t1.islower():  # Si t1 es una variable
        return unificar_var(t1, t2, theta)
    elif isinstance(t2, str) and t2.islower():  # Si t2 es una variable
        return unificar_var(t2, t1, theta)
    elif isinstance(t1, list) and isinstance(t2, list):  # Si ambos términos son listas
        if not t1 or not t2:  # Si alguna lista está vacía, la unificación no es posible
            return None
        else:
            return unificar(t1[1:], t2[1:], unificar(t1[0], t2[0], theta))
    else:
        return None

def unificar_var(var, x, theta):
    """
    Función que realiza la unificación de una variable var con un término x.
    Args:
        var: Variable a unificar.
        x: Término a unificar con la variable.
        theta: Substituciones actuales.
    Returns:
        Unificación: Un diccionario representando la unificación de los términos si es posible,
                     o None si la unificación no es posible.
    """
    if var in theta:
        return unificar(theta[var], x, theta)
    elif x in theta:
        return unificar(var, theta[x], theta)
    elif occur_check(var, x, theta):
        return None
    else:
        theta[var] = x
        return theta

def occur_check(var, x, theta):
    """
    Función que realiza el chequeo de ocurrencia.
    Args:
        var: Variable.
        x: Término.
        theta: Substituciones actuales.
    Returns:
        ocurre: Booleano indicando si la variable ocurre en el término.
    """
    if var == x:
        return True
    elif isinstance(x, str):
        return False
    elif isinstance(x, list):
        return any(occur_check(var, xi, theta) for xi in x)
    else:
        return False

# Ejemplo de unificación
t1 = ["P", "x", "y"]
t2 = ["P", ["f", "z"], "y"]
theta = unificar(t1, t2, {})
print("Unificación:", theta)