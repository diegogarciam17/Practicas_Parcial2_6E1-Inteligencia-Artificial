# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Procesos Estacionarios

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Generar una serie temporal no estacionaria
np.random.seed(0)
serie_temporal = pd.Series(np.random.randn(1000).cumsum(), index=pd.date_range('2022-01-01', periods=1000))

# Función para verificar la estacionariedad
def verificar_estacionariedad(serie):
    # Calcula la prueba de Dickey-Fuller
    resultado = adfuller(serie)
    print('Estadística de la prueba:', resultado[0])
    print('Valor p:', resultado[1])
    print('Valores críticos:')
    for clave, valor in resultado[4].items():
        print('\t', clave, ':', valor)
    
    # Comprueba si la estadística de la prueba es menor que el valor crítico
    if resultado[0] < resultado[4]['5%']:
        print('La serie es estacionaria')
    else:
        print('La serie no es estacionaria')

# Verificar estacionariedad de la serie temporal
verificar_estacionariedad(serie_temporal)