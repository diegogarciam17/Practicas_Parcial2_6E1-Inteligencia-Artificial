# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
import ast

# Función para realizar el análisis semántico
def semantic_analysis(expression):
    # Intentar evaluar la expresión para detectar errores semánticos
    try:
        # Convertir la expresión en un árbol de sintaxis abstracta (AST)
        tree = ast.parse(expression, mode='eval')
        
        # Recorrer el AST y verificar si hay nodos de tipo Name (variables) o Call (llamadas a funciones)
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                # Si se encuentra un nodo de tipo Name, verificar si es una variable no permitida
                if node.id in {'os', 'sys', 'subprocess'}:
                    raise ValueError(f'Error semántico: el uso de la variable "{node.id}" no está permitido')
            elif isinstance(node, ast.Call):
                # Si se encuentra un nodo de tipo Call, verificar si es una llamada a una función no permitida
                if isinstance(node.func, ast.Name) and node.func.id in {'eval', 'exec'}:
                    raise ValueError(f'Error semántico: el uso de la función "{node.func.id}" no está permitido')
    except SyntaxError as e:
        # Capturar errores de sintaxis en la expresión
        raise ValueError(f'Error de sintaxis: {e}')
    except Exception as e:
        # Capturar otros errores durante la evaluación de la expresión
        raise ValueError(f'Error semántico: {e}')

    # Si no se encontraron errores, la expresión es válida
    return "La expresión es válida."

# Ejemplo de uso del análisis semántico
expression = "2 * os.system('rm -rf /')"
try:
    result = semantic_analysis(expression)
    print(result)
except ValueError as e:
    print(e)
