# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Probabilidad Condicionada y Normalización
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

def calcular_probabilidad_condicionada(evento_A, evento_B, espacio_muestral):
    """
    Calcula la probabilidad condicionada P(A | B) de un evento A dado que ha ocurrido un evento B.

    Args:
    - evento_A: El evento de interés cuya probabilidad se condiciona a la ocurrencia de evento_B.
    - evento_B: El evento condicionante.
    - espacio_muestral: El conjunto de todos los posibles resultados o eventos en el espacio muestral.

    Returns:
    - probabilidad_condicionada: La probabilidad condicionada P(A | B).
    """
    # Contar la cantidad de veces que ocurren ambos eventos simultáneamente
    conteo_AB = sum(1 for a, b in zip(evento_A, evento_B) if a == evento_A and b == evento_B)
    
    # Contar la cantidad de veces que ocurre el evento condicionante
    conteo_B = espacio_muestral.count(evento_B)
    
    # Verificar que el conteo_B sea diferente de cero antes de realizar la división
    if conteo_B != 0:
        # Calcular la probabilidad condicionada dividiendo el conteo_AB por el conteo_B
        probabilidad_condicionada = conteo_AB / conteo_B
        return probabilidad_condicionada
    else:
        # En caso de que el evento condicionante no ocurra en el espacio muestral, devolver None
        return None
