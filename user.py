
from conexion import conectar

# pylint: disable=C0103


class User:
    def __init__(self, nombre, numID, fNacimiento, celular, fRegistro, qrAsociado, cGrupales, enfermedades, objetivos, notasGenerales, direccion):
        self.nombre = nombre
        self.numID = numID
        self.fNacimiento = fNacimiento
        self.celular = celular
        self.fRegistro = fRegistro
        self.qrAsociado = qrAsociado
        self.cGrupales = cGrupales
        self.enfermedades = enfermedades
        self.objetivos = objetivos
        self.notasGenerales = notasGenerales
        self.direccion = direccion

    def save_user(self):
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = 'INSERT INTO usuario (nombre, numIdentificacion, fechaNacimiento, telefono, \
                              fechaRegistro, qrAsociado, cGrupales, enfermedades, objetivos, notasGenerales, \
                             direccion) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            values = (self.nombre, self.numID, self.fNacimiento, self.celular, self.fRegistro, self.qrAsociado,
                      self.cGrupales, self.enfermedades, self.objetivos, self.notasGenerales, self.direccion)

            cursor.execute(query, values)
            db_connection.commit()
            cursor.close()
            db_connection.close()
            return ('Usuario Registrado Exitosamente')
        except Exception as e:
            return f'Error al registrar usuario{e}'

    @classmethod
    def consult_user(cls):
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = 'SELECT * FROM usuario'
            cursor.execute(query)

            # Obtener todos los resultados
            results = cursor.fetchall()
            users_list = []

            for result in results:
                user_data = (
                    result[0],  # ID
                    result[1],  # Nombre
                    result[2],  # CC
                    result[3],  # FNacimiento
                    result[4],  # Celular
                    result[5],  # FRegistro
                    result[6],  # QR
                    result[7],  # CGrupales
                    result[8],  # Enfermedades
                    result[9],  # Objetivos
                    result[10],  # Notas Generales
                    result[11]  # Direccion
                )
                users_list.append(user_data)

            return users_list

        except Exception as e:
            return f"Error al consultar usuarios: {e}"

    @classmethod
    def update_user(self, idusuario, nombre, numIdentificacion, fechaNacimiento, telefono, fechaRegistro, qrAsociado, cGrupales, enfermedades, objetivos, notasGenerales, direccion):
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = 'UPDATE usuario SET nombre = %s, numIdentificacion =%s, fechaNacimiento = %s, telefono =%s, fechaRegistro =%s, qrAsociado =%s, cGrupales =%s, enfermedades=%s, objetivos=%s, notasGenerales=%s, direccion=%s WHERE idusuario =%s'
            values = (nombre, numIdentificacion, fechaNacimiento, telefono, fechaRegistro,
                      qrAsociado, cGrupales, enfermedades, objetivos, notasGenerales, direccion, idusuario)
            cursor.execute(query, values)
            db_connection.commit()
            cursor.close()
            db_connection.close()
            return f'Usuario con ID: {idusuario} Modificado Exitosamente'
        except Exception as e:
            return f"Erro al modificar datos: {e}"
            print(f"Erro al modificar datos: {e}")

    @classmethod
    def delete_user(cls, idusuario):
        try:
            db_connection = conectar()
            cursor = db_connection.cursor()
            query = "DELETE FROM usuario WHERE idusuario = %s"
            values = (idusuario,)
            cursor.execute(query, values)
            db_connection.commit()
            cursor.close()
            db_connection.close()
            return f"Registro con ID: {idusuario} eliminado correctamente"
        except Exception as e:
            return f"Error al eliminar: {str(e)}"
