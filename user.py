
import conexion

# pylint: disable=C0103


class User:
    def __init__(self, nombre, numID, fechaNacimiento, celular, fechaRegistro, qrAsociado, cGrupales, enfermedades, objetivos, notasGenerales, direccion):
        self.nombre = nombre
        self.numID = numID
        self.fechaNacimiento = fechaNacimiento
        self.celular = celular
        self.fechaRegistro = fechaRegistro
        self.qrAsociado = qrAsociado
        self.cGrupales = cGrupales
        self.enfermedades = enfermedades
        self.objetivos = objetivos
        self.notasGenerales = notasGenerales
        self.direccion = direccion

    def guardar(self, connection):

        cursor = connection.cursor()
        query = 'INSERT INTO usuario (nombre, numIdentificacion, fechaNacimiento, telefono, \
                              fechaRegistro, qrAsociado, cGrupales, enfermedades, objetivos, notasGenerales, \
                             direccion) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        cursor.execute(query, (self.nombre, self.numID, self.fechaNacimiento, self.celular,
                               self.fechaRegistro, self.qrAsociado, self.cGrupales, self.enfermedades,
                               self.objetivos, self.notasGenerales, self.direccion))
        connection.commit()
        cursor.close()
        connection.close()
