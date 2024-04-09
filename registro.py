from conexion import conectar

def registro(self, user):

    user = user
    ###################################
    # hay que crear la nueva tabla en la base de datos, hacer el query y terminar la funcion.
    ###############################################
    ## estructura de query de ejemplo
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