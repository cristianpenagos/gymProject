import mysql.connector


def conectar():
    dbConnection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456789',
        database='gymdb'
    )
    if dbConnection.is_connected():
        return dbConnection
    else:
        raise ValueError('No se pudo conectar a la base de datos')
