# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#Probabilidad-Recuperación del Datos
#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-ç

import sqlite3

# Conectar a la base de datos SQLite
conn = sqlite3.connect('example.db')

# Crear un cursor para ejecutar consultas SQL
cur = conn.cursor()

# Crear la tabla 'students' si no existe
cur.execute('''CREATE TABLE IF NOT EXISTS students (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               age INTEGER NOT NULL)''')

# Insertar algunos datos de ejemplo en la tabla 'students'
cur.execute("INSERT INTO students (name, age) VALUES ('John', 25)")
cur.execute("INSERT INTO students (name, age) VALUES ('Jane', 23)")
cur.execute("INSERT INTO students (name, age) VALUES ('Alice', 22)")

# Confirmar los cambios
conn.commit()

# Definir una función para recuperar datos
def retrieve_data():
    # Ejecutar una consulta SQL para seleccionar todos los registros de la tabla 'students'
    cur.execute('SELECT * FROM students')
    # Recuperar todos los registros seleccionados
    rows = cur.fetchall()
    # Imprimir los registros recuperados
    for row in rows:
        print(row)

# Llamar a la función para recuperar datos
retrieve_data()

# Cerrar el cursor y la conexión
cur.close()
conn.close()