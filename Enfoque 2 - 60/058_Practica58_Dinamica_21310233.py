# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Dinámica y Control
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import numpy as np
import matplotlib.pyplot as plt

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def update(self, setpoint, measured_value):
        error = setpoint - measured_value
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        return output

# Sistema de ejemplo: tanque de agua
class WaterTank:
    def __init__(self, max_water_level):
        self.max_water_level = max_water_level
        self.water_level = 0

    def update(self, flow_rate):
        # Simula el flujo de agua dentro y fuera del tanque
        self.water_level += flow_rate
        self.water_level = np.clip(self.water_level, 0, self.max_water_level)  # Limita el nivel de agua al máximo del tanque
        return self.water_level

# Parámetros del controlador PID
kp = 0.5
ki = 0.1
kd = 0.2

# Crear controlador PID
controller = PIDController(kp, ki, kd)

# Crear sistema de ejemplo: tanque de agua con capacidad máxima de 100 unidades
water_tank = WaterTank(max_water_level=100)

# Simulación de control de nivel de agua en el tanque
setpoint = 80
time = np.arange(0, 100, 0.1)
measured_values = []
controller_outputs = []

for t in time:
    # Medida del nivel de agua actual
    measured_value = water_tank.water_level
    measured_values.append(measured_value)

    # Actualización del controlador PID
    control_signal = controller.update(setpoint, measured_value)
    controller_outputs.append(control_signal)

    # Simulación del sistema: flujo de entrada al tanque
    flow_rate = control_signal  # El controlador PID ajusta el flujo de entrada al tanque
    water_tank.update(flow_rate)

# Gráfico de resultados
plt.plot(time, measured_values, label='Nivel de Agua Medido')
plt.plot(time, controller_outputs, label='Salida del Controlador PID')
plt.axhline(setpoint, color='r', linestyle='--', label='Punto de Ajuste')
plt.title('Control PID de Nivel de Agua en Tanque')
plt.xlabel('Tiempo')
plt.ylabel('Nivel de Agua')
plt.legend()
plt.grid(True)
plt.show()