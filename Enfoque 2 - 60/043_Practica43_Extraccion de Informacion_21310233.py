# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Extracción de Información
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import re

# Texto de ejemplo
texto = "Mi número de teléfono es 123-456-7890 y mi otro número es 987-654-3210."

# Patrón de expresión regular para números de teléfono en el formato XXX-XXX-XXXX
patron = r'\d{3}-\d{3}-\d{4}'

# Buscar todas las coincidencias del patrón en el texto
numeros_telefono = re.findall(patron, texto)

# Imprimir los números de teléfono encontrados
print("Números de teléfono encontrados:")
for numero in numeros_telefono:
    print(numero)