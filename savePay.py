import mysql.connector

#DB Connection

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0123456789",
    database="gymdb"
)

#cursor
cursor=connection.cursor()

#Query

query = "INSERT INTO mensualidad (fecha, valor, plan, usuario_idusuario) VALUES (%s, %s, %s, %s)"

#Start Query

cursor.execute(query, ("2024-01-04", 65000, 5, 6 ))

#Confirm Changes

connection.commit()

cursor.close()
