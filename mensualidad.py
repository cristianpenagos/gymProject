from conexion import conectar


class Mensualidad:
    def __init__(self, fecha, valor, plan, usuario_id):
        self.fecha = fecha
        self.valor = valor
        self.plan = plan
        self.usuario_id = usuario_id

    def save_mensualidad(self):
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = 'INSERT INTO mensualidad (fecha, valor, plan, usuario_idusuario) VALUES(%s, %s, %s, %s)'
            values = (self.fecha, self.valor, self.plan, self.usuario_id)
            cursor.execute(query, values)
            db_connection.commit()
            cursor.close()
            db_connection.close()
            return ('Mensualidad Registrada Exitosamente')
        except Exception as e:
            return f'Error al registrar mensualidad{e}'

    @classmethod
    def consult_mensualidades(cls):
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = '''SELECT mensualidad.*,
                              usuario.nombre
                                FROM mensualidad
                                LEFT JOIN usuario ON mensualidad.usuario_idusuario = usuario.idusuario;'''
            cursor.execute(query)

            # obtener resultados

            results = cursor.fetchall()
            pay_list = []

            for result in results:
                pay_data = (
                    result[0],  # idmensualidad
                    result[1],  # fecha
                    result[2],  # valor
                    result[3],  # plan
                    result[4],  # usuario_idusuario
                    result[5],  # nombre
                )
                pay_list.append(pay_data)
            return pay_list
        except Exception as e:
            return f"Error al consultar pagos: {e}"

    @classmethod
    def update_pay(self, idmensualidad, fecha, valor, plan, usuario_id):
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = 'UPDATE mensualidad SET fecha = %s, valor =%s, plan = %s, usuario_idusuario =%s WHERE idmensualidad =%s'
            values = (fecha, valor, plan, usuario_id, idmensualidad)
            cursor.execute(query, values)
            db_connection.commit()
            cursor.close()
            db_connection.close()
            return f'Pago con ID: {idmensualidad} Modificado Exitosamente'
        except Exception as e:
            return f"Erro al modificar datos: {e}"

    @classmethod
    def delete_pay(cls, idmensualidad):
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = "DELETE FROM mensualidad WHERE idmensualidad = %s"
            values = (idmensualidad,)
            cursor.execute(query, values)
            db_connection.commit()
            cursor.close()
            db_connection.close()
            return f"Mensualidad con ID: {idmensualidad} eliminado correctamente"
        except Exception as e:
            return f"Error al eliminar: {str(e)}"
