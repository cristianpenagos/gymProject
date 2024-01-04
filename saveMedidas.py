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
query = 'INSERT INTO medidas (fecha, cuelloM, brazoM, abdomenM, caderaM, piernaAltaM, \
	                        piernaBajaM, pantorrillaM, abdomenG, bicepG, tricepG, escapulaG,  \
							piernaG, usuario_idusuario ) \
						values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# start query
cursor.execute(query, ("2024-01-01", 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.10, 11.11, 12.12, 2))

# confirm changes
connection.commit()

# cursor close
cursor.close()