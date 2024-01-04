import mysql.connector

# DB Connection

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0123456789',
    database='gymdb'
)

# cursor
cursor = connection.cursor()

# Query
query = 'INSERT INTO usuario (nombre, numIdentificacion, fechaNacimiento, telefono, \
                              fechaRegistro, qrAsociado, cGrupales, enfermedades, objetivos, notasGenerales, \
                             direccion) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# start query
cursor.execute(query, ('Ariana', '9089', '2022-04-19', '3147748687', '2023-01-03',
                       4, 0, 'Sin Enfermedades', 'Aumento de masa muscular',
                       'Sin notas generales', 'Medellin'))

# confirm changes
connection.commit()

# cursor close
cursor.close()
