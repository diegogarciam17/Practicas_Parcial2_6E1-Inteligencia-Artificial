# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Gráficos por Computador
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np
import matplotlib.pyplot as plt

# Definir la función a trazar
def f(x):
    return np.sin(x)

# Generar datos para el eje x
x = np.linspace(0, 10, 100)

# Calcular los valores de la función para cada punto en x
y = f(x)

# Crear el gráfico
plt.figure(figsize=(8, 6))  # Tamaño del gráfico
plt.plot(x, y, label='y = sin(x)')  # Trazar la función
plt.title('Gráfico de la función y = sin(x)')  # Título del gráfico
plt.xlabel('x')  # Etiqueta del eje x
plt.ylabel('y')  # Etiqueta del eje y
plt.grid(True)  # Activar cuadrícula
plt.legend()  # Mostrar leyenda
plt.show()  # Mostrar el gráfico