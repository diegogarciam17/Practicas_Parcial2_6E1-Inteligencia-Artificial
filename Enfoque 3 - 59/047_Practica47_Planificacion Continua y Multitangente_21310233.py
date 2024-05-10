# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
import random
import heapq

# Definir una clase para representar los vehículos autónomos
class Vehiculo:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def __str__(self):
        return f"Vehículo {self.nombre} en {self.ubicacion}"

# Definir una clase para representar las tareas
class Tarea:
    def __init__(self, nombre, ubicacion_destino):
        self.nombre = nombre
        self.ubicacion_destino = ubicacion_destino

    def __str__(self):
        return f"Tarea {self.nombre} con destino {self.ubicacion_destino}"

# Definir una función para generar tareas aleatorias
def generar_tareas(num_tareas, ubicaciones):
    tareas = []
    for i in range(num_tareas):
        nombre = f"T{i+1}"
        ubicacion_destino = random.choice(ubicaciones)
        tarea = Tarea(nombre, ubicacion_destino)
        tareas.append(tarea)
    return tareas

# Definir una función para planificar las tareas para cada vehículo
def planificar_tareas(vehiculos, tareas):
    for tarea in tareas:
        vehiculo = random.choice(vehiculos)
        vehiculo.agregar_tarea(tarea)

# Definir una función para simular la entrega de tareas
def entregar_tareas(vehiculos):
    for vehiculo in vehiculos:
        if vehiculo.tareas:
            tarea = vehiculo.tareas.pop(0)
            print(f"{vehiculo} entrega {tarea}")

# Crear vehículos autónomos y generar tareas aleatorias
vehiculos = [Vehiculo("V1", "Depósito"), Vehiculo("V2", "Depósito")]
ubicaciones = ["Tienda A", "Tienda B", "Tienda C", "Tienda D"]
tareas = generar_tareas(6, ubicaciones)

# Planificar las tareas para cada vehículo
planificar_tareas(vehiculos, tareas)

# Simular la entrega de tareas
print("Entrega de tareas:")
entregar_tareas(vehiculos)