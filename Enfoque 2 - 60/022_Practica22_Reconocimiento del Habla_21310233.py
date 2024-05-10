# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Reconocimiento del Habla
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import speech_recognition as sr

# Inicializar el reconocedor
recognizer = sr.Recognizer()

# Definir una función para reconocer el habla
def reconocer_habla():
    with sr.Microphone() as source:
        print("Di algo...")
        recognizer.adjust_for_ambient_noise(source)  # Ajustar para el ruido ambiental
        audio = recognizer.listen(source)  # Escuchar el audio del micrófono

    try:
        print("Reconociendo...")
        texto = recognizer.recognize_google(audio, language='es-ES')  # Reconocer el habla utilizando Google Speech Recognition
        print("Texto reconocido:", texto)
    except sr.UnknownValueError:
        print("No se pudo entender el habla")
    except sr.RequestError as e:
        print("Error al solicitar resultados; {0}".format(e))

# Llamar a la función para reconocer el habla
reconocer_habla()