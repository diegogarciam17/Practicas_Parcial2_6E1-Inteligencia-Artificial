# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""
from rdflib import Graph, Namespace, RDF, RDFS, Literal

# Cargar el grafo RDF desde el archivo
g = Graph()
g.parse("ontologia.rdf")

# Consulta SPARQL para obtener los nombres de las instancias
query = """
    PREFIX ex: <http://example.org/>
    SELECT ?nombre
    WHERE {
        ?instancia ex:name ?nombre .
    }
"""

# Ejecutar la consulta y obtener resultados
resultados = g.query(query)

# Imprimir los nombres de las instancias
print("Nombres de las instancias:")
for resultado in resultados:
    print(resultado["nombre"])

