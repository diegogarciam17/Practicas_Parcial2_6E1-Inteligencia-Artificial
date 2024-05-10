# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
import re

# Definir una lista de tokens y expresiones regulares para reconocerlos
tokens = [
    ('NUMBER', r'\d+'),        # Números enteros
    ('PLUS', r'\+'),            # Suma
    ('MINUS', r'\-'),           # Resta
    ('TIMES', r'\*'),           # Multiplicación
    ('DIVIDE', r'\/'),          # División
    ('LPAREN', r'\('),          # Paréntesis izquierdo
    ('RPAREN', r'\)'),          # Paréntesis derecho
]

# Función para realizar el análisis léxico
def lexer(text):
    pos = 0  # Posición actual en el texto
    tokens_found = []  # Lista para almacenar los tokens encontrados

    # Iterar hasta que se haya analizado todo el texto
    while pos < len(text):
        longest_match_length = 0  # Longitud de la coincidencia más larga
        longest_match_type = None  # Tipo de token para la coincidencia más larga

        # Iterar sobre cada tipo de token y su expresión regular
        for token_type, pattern in tokens:
            regex = re.compile(pattern)
            match = regex.match(text, pos)
            if match:
                match_length = len(match.group(0))
                # Actualizar la coincidencia más larga si es necesario
                if match_length > longest_match_length:
                    longest_match_length = match_length
                    longest_match_type = token_type

        if longest_match_type:
            # Agregar el token encontrado a la lista de tokens
            tokens_found.append((longest_match_type, text[pos:pos + longest_match_length]))
            # Actualizar la posición actual
            pos += longest_match_length
        else:
            # Si no se encuentra ninguna coincidencia, hay un error léxico
            raise ValueError(f'Error léxico: no se pudo reconocer el token en la posición {pos}')

    return tokens_found

# Ejemplo de uso del analizador léxico
text = "3 + 4 * (2 - 1)"
tokens_found = lexer(text)
print(tokens_found)