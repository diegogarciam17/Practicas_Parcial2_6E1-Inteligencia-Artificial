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

# Definir una clase para el analizador sintáctico
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        self.pos = 0
        return self.expr()

    def expr(self):
        result = self.term()
        while self.pos < len(self.tokens):
            token_type, token_value = self.tokens[self.pos]
            if token_type == 'PLUS':
                self.pos += 1
                result += self.term()
            elif token_type == 'MINUS':
                self.pos += 1
                result -= self.term()
            else:
                break
        return result

    def term(self):
        result = self.factor()
        while self.pos < len(self.tokens):
            token_type, token_value = self.tokens[self.pos]
            if token_type == 'TIMES':
                self.pos += 1
                result *= self.factor()
            elif token_type == 'DIVIDE':
                self.pos += 1
                result /= self.factor()
            else:
                break
        return result

    def factor(self):
        token_type, token_value = self.tokens[self.pos]
        if token_type == 'NUMBER':
            self.pos += 1
            return int(token_value)
        elif token_type == 'LPAREN':
            self.pos += 1
            result = self.expr()
            if self.tokens[self.pos][0] != 'RPAREN':
                raise ValueError('Error sintáctico: se esperaba ")"')
            self.pos += 1
            return result
        else:
            raise ValueError('Error sintáctico: se esperaba un número o "("')

# Ejemplo de uso del analizador léxico y sintáctico
text = "3 + 4 * (2 - 1)"
tokens_found = lexer(text)
parser = Parser(tokens_found)
result = parser.parse()
print("Resultado:", result)
