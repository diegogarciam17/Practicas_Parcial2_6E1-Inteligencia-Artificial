# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Datos de ejemplo: correos electrónicos etiquetados como spam (1) o no spam (0)
emails = [
    ("Oferta especial, ¡compra ahora!", 1),
    ("Gana un millón de dólares fácilmente", 1),
    ("Reunión de trabajo mañana a las 10 AM", 0),
    ("Confirmación de tu pedido", 0),
    ("¡Último día para aprovechar la promoción!", 1)
]

# Dividir los datos en características (X) y etiquetas (y)
X = [email[0] for email in emails]
y = [email[1] for email in emails]

# Vectorizar los datos de texto utilizando el modelo Bag of Words
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar el clasificador Naive Bayes
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = classifier.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", accuracy)