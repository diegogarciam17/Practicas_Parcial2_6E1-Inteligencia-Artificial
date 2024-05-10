# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Preprocesado: Filtros
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Generar datos de ejemplo (señal ruidosa)
np.random.seed(0)
t = np.linspace(0, 2*np.pi, 100)
signal = np.sin(t) + np.random.normal(0, 0.3, 100)

# Aplicar filtro de suavizado (filtro de Savitzky-Golay)
smoothed_signal = savgol_filter(signal, window_length=15, polyorder=2)

# Graficar la señal original y la señal suavizada
plt.figure(figsize=(10, 6))
plt.plot(t, signal, label='Señal Original')
plt.plot(t, smoothed_signal, label='Señal Suavizada', linewidth=2)
plt.title('Filtro de Suavizado (Savitzky-Golay)')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)
plt.show()