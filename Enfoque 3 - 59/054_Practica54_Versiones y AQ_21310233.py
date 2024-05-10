# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
def aq_algorithm(examples):
    # Inicializar el espacio de versiones con la hipótesis más general y la más específica
    version_space = [((), set())]  # (hipótesis, ejemplos cubiertos)

    for x, y in examples:
        # Actualizar el espacio de versiones para cada ejemplo
        new_version_space = []

        for hypothesis, covered_examples in version_space:
            if tuple(x) in covered_examples:
                # Si el ejemplo ya está cubierto por la hipótesis, continuar
                continue

            if y == 1:  # Si el ejemplo es positivo
                if len(hypothesis) == 0:
                    # Si la hipótesis es la más general, no se puede hacer más general
                    new_version_space.append((hypothesis, covered_examples))
                else:
                    # Crear una nueva hipótesis más general eliminando un atributo
                    new_hypothesis = hypothesis[:-1]
                    new_version_space.append((new_hypothesis, covered_examples))
            else:  # Si el ejemplo es negativo
                if len(hypothesis) == len(x):
                    # Si la hipótesis es la más específica, no se puede hacer más específica
                    continue
                else:
                    # Crear una nueva hipótesis más específica agregando un atributo
                    new_hypothesis = hypothesis + (x[len(hypothesis)],)
                    new_version_space.append((new_hypothesis, covered_examples | {tuple(x)}))

        version_space = new_version_space

    # Devolver la mejor hipótesis final
    return version_space[-1][0]

# Ejemplo de datos de entrenamiento
examples = [
    ([1, 1, 1], 1),
    ([1, 0, 0], 0),
    ([0, 1, 0], 1),
    ([0, 0, 1], 0),
]

# Ejecutar el algoritmo AQ
best_hypothesis = aq_algorithm(examples)
print("Mejor hipótesis:", best_hypothesis)