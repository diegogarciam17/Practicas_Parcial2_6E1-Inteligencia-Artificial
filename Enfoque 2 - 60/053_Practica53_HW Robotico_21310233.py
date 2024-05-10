# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-HW Robótico: Sensores y Actuadores
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import RPi.GPIO as GPIO
import time

# Configurar los pines GPIO
sensor_pin = 18  # Pin del sensor de proximidad
led_pin = 23     # Pin del LED

# Configurar el modo de los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # Leer el estado del sensor de proximidad
        sensor_state = GPIO.input(sensor_pin)

        # Encender o apagar el LED según el estado del sensor
        if sensor_state == GPIO.HIGH:
            GPIO.output(led_pin, GPIO.HIGH)
            print("Objeto detectado")
        else:
            GPIO.output(led_pin, GPIO.LOW)
            print("No hay objeto")

        # Esperar un breve tiempo antes de leer nuevamente el sensor
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Programa detenido por el usuario")

finally:
    # Limpiar los pines GPIO y apagar el LED
    GPIO.cleanup()