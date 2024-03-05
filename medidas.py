from conexion import conectar


class Medidas:
    def __init__(self, usuario_idusuario, fecha, cuelloM, brazoM, abdomenM, caderaM, piernaAltaM, piernaBajaM, pantorrillaM, abdomenG, bicepG, tricepG, escapulaG, piernaG):
        self.usuario_idusuario = usuario_idusuario
        self.fecha = fecha
        self.cuelloM = cuelloM
        self.brazoM = brazoM
        self.abdomenM = abdomenM
        self.caderaM = caderaM
        self.piernaAltaM = piernaAltaM
        self.piernaBajaM = piernaBajaM
        self.pantorrillaM = pantorrillaM
        self.abdomenG = abdomenG
        self.bicepG = bicepG
        self.tricepG = tricepG
        self.escapulaG = escapulaG
        self.piernaG = piernaG

    def save_medidas(self):
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = 'INSERT INTO medidas (fecha, cuelloM, brazoM, abdomenM, caderaM, piernaAltaM, piernaBajaM, pantorrillaM, abdomenG, bicepG, tricepG, escapulaG, piernaG, usuario_idusuario) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            values = (self.fecha, self.cuelloM, self.brazoM, self.abdomenM, self.caderaM, self.piernaAltaM, self.piernaBajaM,
                      self.pantorrillaM, self.abdomenG, self.bicepG, self.tricepG, self.escapulaG, self.piernaG, self.usuario_idusuario)

            cursor.execute(query, values)
            db_connection.commit()
            cursor.close()
            db_connection.close()
            return 'Medidas Registradas Exitosamente'
        except Exception as e:
            return f'Error al registrar medidas: {e}'

    @classmethod
    def consult_medidas(cls):
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = 'SELECT medidas.idmedidas,\
                            usuario.nombre,\
                            medidas.fecha,\
                            medidas.usuario_idusuario,\
                            medidas.cuelloM,\
                            medidas.brazoM,\
                            medidas.abdomenM,\
                            medidas.caderaM,\
                            medidas.piernaAltaM,\
                            medidas.piernaBajaM,\
                            medidas.pantorrillaM,\
                            medidas.abdomenG,\
                            medidas.bicepG,\
                            medidas.tricepG,\
                            medidas.escapulaG,\
                            medidas.piernaG\
                            FROM usuario\
                            JOIN medidas ON usuario.idusuario = medidas.usuario_idusuario;'
            cursor.execute(query)

            # Obtener todos los resultados
            results = cursor.fetchall()
            medidas_list = []

            for result in results:
                medidas_data = (
                    result[0],  # ID
                    result[1],  # Nombre
                    result[2],  # Fecha
                    result[3],  # Fecha
                    result[4],  # Fecha
                    result[5],  # Fecha
                    result[6],  # Fecha
                    result[7],  # Fecha
                    result[8],  # Fecha
                    result[9],  # Fecha
                    result[10],  # Fecha
                    result[11],  # Fecha
                    result[12],  # Fecha
                    result[13],  # Fecha
                    result[14],  # Fecha
                    result[15],  # Fecha
                )
                medidas_list.append(medidas_data)
            return medidas_list

        except Exception as e:
            return f"Error al consultar usuarios: {e}"

    @classmethod
    def update_medida(self, idmedidas, fecha, cuelloM, brazoM, abdomenM, caderaM, piernaAltaM, piernaBajaM, pantorrillaM, abdomenG, bicepG, tricepG, escapulaG, piernaG, usuario_idusuario):

        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = 'UPDATE medidas SET fecha = %s,\
                                        cuelloM = %s,\
                                        brazoM = %s,\
                                        abdomenM = %s,\
                                        caderaM = %s,\
                                        piernaAltaM = %s,\
                                        piernaBajaM = %s,\
                                        pantorrillaM = %s,\
                                        abdomenG = %s,\
                                        bicepG = %s,\
                                        tricepG = %s,\
                                        escapulaG = %s,\
                                        piernaG = %s,\
                                        usuario_idusuario = %s\
                                        WHERE idmedidas = %s'
            values = (fecha, cuelloM, brazoM, abdomenM, caderaM, piernaAltaM,
                      piernaBajaM, pantorrillaM, abdomenG, bicepG, tricepG, escapulaG, piernaG, usuario_idusuario, idmedidas)
            cursor.execute(query, values)
            db_connection.commit()
            cursor.close()
            db_connection.close()
            return f'Medidas con ID: {idmedidas} Modificado Exitosamente'
        except Exception as e:
            return f"Erro al modificar medidas: {e}"
            print(f"Erro al modificar medidas: {e}")

    @classmethod
    def delete_medida(cls, idmedidas):
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = "DELETE FROM medidas WHERE idmedidas = %s"
            values = (idmedidas,)
            cursor.execute(query, values)
            db_connection.commit()
            cursor.close()
            db_connection.close()
            return f"Registro con ID: {idmedidas} eliminado correctamente"
        except Exception as e:
            return f"Error al eliminar: {str(e)}"
