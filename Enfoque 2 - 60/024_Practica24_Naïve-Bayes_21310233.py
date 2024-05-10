# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Naïve-Bayes
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar el clasificador Naïve Bayes
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)

# Predecir las etiquetas de clase para el conjunto de prueba
y_pred = nb_classifier.predict(X_test)

# Calcular la precisión del clasificador Naïve Bayes
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del clasificador Naïve Bayes:", accuracy)