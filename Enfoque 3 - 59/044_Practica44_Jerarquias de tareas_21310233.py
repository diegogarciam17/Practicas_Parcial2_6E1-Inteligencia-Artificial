# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
# Definición de la red jerárquica de tareas
tareas = {
    'Proyecto': {
        'Investigación': {
            'Recopilar información': None,
            'Revisar literatura': None
        },
        'Desarrollo': {
            'Diseñar prototipo': None,
            'Implementar funcionalidades': None
        },
        'Pruebas': {
            'Ejecutar pruebas unitarias': None,
            'Realizar pruebas de integración': None
        }
    }
}

# Función para imprimir la red jerárquica de tareas
def imprimir_tareas(tareas, nivel=0):
    for tarea, sub_tareas in tareas.items():
        print('  ' * nivel + tarea)
        if sub_tareas:
            imprimir_tareas(sub_tareas, nivel + 1)

# Imprimir la red jerárquica de tareas
imprimir_tareas(tareas)