from conexion import conectar


class OtrosIngresos:
    def __init__(self, elemento, valor, fecha):
        self.elemento = elemento
        self.valor = valor
        self.fecha = fecha

    def guardar(self):

        db_connection = conectar()
        cursor = db_connection.cursor()
        query = "INSERT INTO otrosIngresos (elemento, valor, fecha) VALUES (%s, %s, %s)"
        values = (self.elemento, self.valor, self.fecha)
        cursor.execute(query, values)
        db_connection.commit()
        cursor.close()
        db_connection.close()

    @classmethod
    def consultar_todos(cls):  # "cls" is a convention, it refers to this class
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()

            query = "SELECT * FROM otrosIngresos"
            cursor.execute(query)

            # Obtener todos los resultados
            resultados = cursor.fetchall()

            # Imprimir o devolver los resultados, según lo que desees hacer
            for resultado in resultados:
                print(
                    f"ID: {resultado[0]}, Elemento: {resultado[1]}, Valor: {resultado[2]}, Fecha: {resultado[3]}")

            cursor.close()
            db_connection.close()

        except Exception as e:
            print(f"Error al consultar datos: {e}")

    def actualizar(self, idingreso):
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = "UPDATE otrosIngresos SET elemento = %s, valor = %s, fecha = %s WHERE idingreso = %s"
            values = (self.elemento, self.valor, self.fecha, idingreso)
            cursor.execute(query, values)
            db_connection.commit()
            cursor.close()
            db_connection.close()
            print(f"Registro con ID: {idingreso} actualizado correctamente")

        except Exception as e:
            print(f"Erro al modificar datos: {e}")

    @classmethod
    def eliminar(cls, idingreso):
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = "DELETE FROM otrosIngresos WHERE idingreso = %s"
            values = (idingreso,)
            cursor.execute(query, values)
            db_connection.commit()
            cursor.close()
            db_connection.close()
            print(f"Registro con ID: {idingreso} eliminado correctamente")
        except Exception as e:
            print("Error al eliminar")
