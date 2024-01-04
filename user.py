
import _mysql_connector
import mysql.connector


class User:
    def __init__(self, nombre, apellido, numID, fechaNacimiento, celular, fechaRegistro, fechaMensualidad, qrAsociado):
        self.nombre = nombre
        self.apellido = apellido
        self.numID = numID
        self.fechaNacimiento = fechaNacimiento
        self.celular = celular
        self.fechaRegistro = fechaRegistro
        self.fechaMensualidad = fechaMensualidad
        self.qrAsociado = qrAsociado


conexion = mysql.connector.connect(

    host='localhost',
    user='root',
    password='123456789',
    database='gymdb'
)


def guardar(User):

    cursor = conexion.cursor()

    sql = 'INSERT INTO user(nombre, apellido, numID,numID, fechaNacimiento, celular, fechaRegistro, fechaMensualidad, qrAsociado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
    valores = (User.nombre, User.apellido, User.numID, User.fechaNacimiento,
               User.celular, User.fechaRegistro, User.fechaMensualidad, User.qrAsociado)

    cursor.execute(sql, valores)
    conexion.commit()

    cursor.close()
    conexion.close()


# Imprimir los datos del usuario
print("Nombre:", nuevo_usuario.nombre)
print("Apellido:", nuevo_usuario.apellido)
print("Número de Identificación:", nuevo_usuario.numID)
print("Fecha de Nacimiento:", nuevo_usuario.fechaNacimiento)
print("Celular:", nuevo_usuario.celular)
print("Fecha de Registro:", nuevo_usuario.fechaRegistro)
print("Fecha de Mensualidad:", nuevo_usuario.fechaMensualidad)
print("QR Asociado:", nuevo_usuario.qrAsociado)


# Crear un objeto de la clase User
nuevo_usuario = User(
    nombre="Juan",
    apellido="Pérez",
    numID=123456789,
    fechaNacimiento="1990-05-15",
    celular=5551234567,
    fechaRegistro="2023-01-01",
    fechaMensualidad="2023-02-01",
    qrAsociado=1234
)

guardar(nuevo_usuario)
