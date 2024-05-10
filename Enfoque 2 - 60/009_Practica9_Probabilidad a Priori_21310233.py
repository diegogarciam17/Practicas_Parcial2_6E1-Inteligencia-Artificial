# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Probabilidad a Priori
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

def calcular_probabilidad_a_priori(evento, espacio_muestral):
    """
    Calcula la probabilidad a priori de un evento dado en un espacio muestral.

    Args:
    - evento: El evento para el cual se calculará la probabilidad a priori.
    - espacio_muestral: El conjunto de todos los posibles resultados o eventos en el espacio muestral.

    Returns:
    - probabilidad: La probabilidad a priori del evento dado.
    """
    # Contar la cantidad de veces que ocurre el evento en el espacio muestral
    conteo_evento = espacio_muestral.count(evento)
    
    # Calcular la probabilidad a priori dividiendo el conteo del evento por el tamaño del espacio muestral
    probabilidad = conteo_evento / len(espacio_muestral)
    
    return probabilidad

# Definir el espacio muestral y el evento de interés
espacio_muestral = ['Cara', 'Cruz', 'Cara', 'Cara', 'Cruz']
evento = 'Cara'

# Calcular la probabilidad a priori del evento
probabilidad_a_priori = calcular_probabilidad_a_priori(evento, espacio_muestral)

# Imprimir el resultado
print("La probabilidad a priori del evento", evento, "es:", probabilidad_a_priori)