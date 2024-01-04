import mysql.connector


class Usuario:
    def __init__(self, nombre, cedula, fechaNacimiento):
        self.nombre = nombre
        self.cedula = cedula
        self.fechaNaciemiento = fechaNacimiento


conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0123456789",
    database="objeto"
)


def guardar(usuario):

    cursor = conexion.cursor()
    sql = "INSERT INTO user (nombre, cedula, fNacimiento) VALUES (%s, %s, %s)"

    datosUsuario = (usuario.nombre, usuario.cedula, usuario.fechaNaciemiento)

    cursor.execute(sql, datosUsuario)
    conexion.commit()

    cursor.close()
    conexion.close()


nuevoUsuario = Usuario(
    nombre="Cristian", cedula="1033653257", fechaNacimiento="1993-04-18")
guardar(nuevoUsuario)
