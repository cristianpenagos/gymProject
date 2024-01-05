from conexion import conectar
import mysql.connector.connection


class OtrosIngresos:
    def __init__(self, elemento, valor):
        self.elemento = elemento
        self.valor = valor


    def guardar(self):

        db_connection = conectar()
        cursor = db_connection.cursor()

        query = "INSERT INTO otrosIngresos (elemento, valor) VALUES (%s, %s)"
        values = (self.elemento, self.valor)

        cursor.execute(query, values)

        db_connection.commit()
        cursor.close()
        db_connection.close()

