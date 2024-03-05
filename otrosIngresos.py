from conexion import conectar


class OtrosIngresos:
    def __init__(self, elemento, valor, fecha):
        self.elemento = elemento
        self.valor = valor
        self.fecha = fecha

    def guardar(self):
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = "INSERT INTO otrosIngresos (elemento, valor, fecha) VALUES (%s, %s, %s)"
            values = (self.elemento, self.valor, self.fecha)
            cursor.execute(query, values)
            db_connection.commit()
            cursor.close()
            db_connection.close()
            return("Registro guardado exitosamente")
        except Exception as e:
            return f"Error al guardar datos: {e}"
            print(f"Error al guardar datos: {e}")

    @classmethod
    def consultar_todos(cls):  # "cls" is a convention, it refers to this class
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()

            query = "SELECT * FROM otrosIngresos"
            cursor.execute(query)

            # Obtener todos los resultados
            resultados = cursor.fetchall()
            text_resultado = ""
            # Imprimir o devolver los resultados, según lo que desees hacer
            for resultado in resultados:
                text_resultado += f"ID: {resultado[0]}, Elemento: {resultado[1]}, Valor: {resultado[2]}, Fecha: {resultado[3]}\n"

                print(
                    f"ID: {resultado[0]}, Elemento: {resultado[1]}, Valor: {resultado[2]}, Fecha: {resultado[3]}")

            cursor.close()
            db_connection.close()
            return text_resultado

        except Exception as e:
            return f"Error al consultar datos: {e}"
            print(f"Error al consultar datos: {e}")

    def actualizar(self, idingreso, elemento, valor, fecha):
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = "UPDATE otrosIngresos SET elemento = %s, valor = %s, fecha = %s WHERE idingreso = %s"
            values = (elemento, valor, fecha, idingreso)
            cursor.execute(query, values)
            db_connection.commit()
            cursor.close()
            db_connection.close()
            return f"Registro con ID: {idingreso} actualizado correctamente"
            print(f"Registro con ID: {idingreso} actualizado correctamente")

        except Exception as e:
            return f"Erro al modificar datos: {e}"
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
            return f"Registro con ID: {idingreso} eliminado correctamente"
            print(f"Registro con ID: {idingreso} eliminado correctamente")
        except Exception as e:
            print("Error al eliminar")
            return f"Error al eliminar: {str(e)}"
