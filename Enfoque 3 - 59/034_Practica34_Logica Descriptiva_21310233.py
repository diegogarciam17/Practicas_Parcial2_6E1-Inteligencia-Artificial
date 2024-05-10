# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
#Reglas
# Ejemplo de regla en Python
def aplicar_descuento(edad):
    if edad < 18:
        return "Tiene derecho a un descuento del 20%."
    else:
        return "No tiene derecho a descuento."

# Aplicar la regla
print(aplicar_descuento(15))  # Salida: Tiene derecho a un descuento del 20%.
print(aplicar_descuento(20))  # Salida: No tiene derecho a descuento.