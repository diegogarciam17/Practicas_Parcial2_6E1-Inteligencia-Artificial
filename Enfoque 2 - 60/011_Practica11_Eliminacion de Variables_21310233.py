# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Eliminación de Variables

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos Iris
iris = load_iris()
X, y = iris.data, iris.target

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inicializar el modelo de clasificación (usaremos Random Forest como ejemplo)
clf = RandomForestClassifier(random_state=42)

# Entrenar el modelo base con todas las características
clf.fit(X_train, y_train)

# Evaluar la precisión del modelo base en el conjunto de prueba
y_pred_base = clf.predict(X_test)
accuracy_base = accuracy_score(y_test, y_pred_base)
print("Precisión del modelo base:", accuracy_base)

# Inicializar una lista para almacenar las características seleccionadas
selected_features = []

# Iterar a través de las características y agregar la más predictiva una por una
while len(selected_features) < X.shape[1]:
    best_feature = None
    best_accuracy = 0
    
    # Iterar a través de las características no seleccionadas
    for feature_idx in range(X.shape[1]):
        if feature_idx not in selected_features:
            # Copiar las características seleccionadas junto con la nueva característica candidata
            features_subset = selected_features + [feature_idx]
            
            # Entrenar el modelo con el subconjunto de características
            clf.fit(X_train[:, features_subset], y_train)
            
            # Evaluar la precisión del modelo en el conjunto de prueba
            y_pred = clf.predict(X_test[:, features_subset])
            accuracy = accuracy_score(y_test, y_pred)
            
            # Actualizar la mejor característica si se obtiene una mejor precisión
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_feature = feature_idx
    
    # Agregar la mejor característica al conjunto de características seleccionadas
    selected_features.append(best_feature)
    
    # Imprimir el progreso
    print("Característica seleccionada en la iteración", len(selected_features), ":", best_feature)
    print("Precisión del modelo con características seleccionadas:", best_accuracy)

# Entrenar y evaluar el modelo final con características seleccionadas
clf.fit(X_train[:, selected_features], y_train)
y_pred_final = clf.predict(X_test[:, selected_features])
accuracy_final = accuracy_score(y_test, y_pred_final)
print("Precisión del modelo final con características seleccionadas:", accuracy_final)