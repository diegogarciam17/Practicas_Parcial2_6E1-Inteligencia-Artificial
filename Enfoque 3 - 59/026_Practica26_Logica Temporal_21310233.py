# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
class TemporalLogicParser:
    def __init__(self):
        self.propositions = set()
        self.temporal_operators = {'◇', '□', 'F', 'G', 'U'}

    def parse(self, expression):
        tokens = expression.split()
        temporal_operator = None
        propositions = []

        for token in tokens:
            if token in self.temporal_operators:
                temporal_operator = token
            else:
                propositions.append(token)

        return temporal_operator, propositions


class TemporalLogicSystem:
    def __init__(self):
        self.parser = TemporalLogicParser()

    def evaluate(self, expression, current_time):
        temporal_operator, propositions = self.parser.parse(expression)

        if temporal_operator == '◇':
            # Evaluación de la modalidad "eventualmente"
            result = any(propositions)
        elif temporal_operator == '□':
            # Evaluación de la modalidad "siempre"
            result = all(propositions)
        elif temporal_operator == 'F':
            # Evaluación de la modalidad "eventualmente en el futuro"
            result = any(propositions[current_time:])
        elif temporal_operator == 'G':
            # Evaluación de la modalidad "siempre en el futuro"
            result = all(propositions[current_time:])
        elif temporal_operator == 'U':
            # Evaluación de la modalidad "hasta que"
            # Evaluamos si la primera proposición se mantiene verdadera hasta que la segunda sea verdadera
            p1, p2 = propositions
            result = any(p1[i] and all(p2[i:]) for i in range(current_time, len(propositions)))
        else:
            # Sin operador temporal, asumimos una proposición simple
            result = True if propositions else False

        return result


# Ejemplo de uso
logic_system = TemporalLogicSystem()
expression = 'F P'  # Eventualmente P (P ocurrirá en algún momento en el futuro)
current_time = 3  # Tiempo actual
result = logic_system.evaluate(expression, current_time)
print(f"Resultado de la expresión '{expression}' en el tiempo {current_time}: {result}")