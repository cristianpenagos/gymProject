from user import User
import conexion

with conexion.conectar() as connection:

    user = User(
        nombre='Ariana',
        numID='99089',
        fechaNacimiento='2022-04-19',
        celular='3147748687',
        fechaRegistro='2023-01-03',
        qrAsociado=12,
        cGrupales=0,
        enfermedades='Sin Enfermedades',
        objetivos='Aumento de masa muscular',
        notasGenerales='Sin notas generales',
        direccion='Medellin')


# connection = conexion.conectar()

user.guardar(connection)

connection.close()
