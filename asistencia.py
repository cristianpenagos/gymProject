from conexion import conectar

import datetime


def save_asistencia(qr):
    try: 
        db_connection = conectar()
        cursor = db_connection.cursor()

        fecha_actual = datetime.datetime.now()
        idUsuario = consultarIDUsuario(qr)

        query = "INSERT INTO asistencia (fecha, qrUsuario, usuario_idusuario) VALUES(%s, %s, %s)"
        values = (fecha_actual, qr, idUsuario)

        cursor.execute(query, values)
        db_connection.commit()
        cursor.close()
        db_connection.close()
        return 'Asistencua guardada exitosamente'
    except Exception as e:
        return f'Error al guardar asistencia: {e}'
    ###
    






def consultarIDUsuario( qr):
    try:
        db_connection = conectar()
        cursor = db_connection.cursor()

        query = "SELECT idusuario FROM usuario WHERE qrAsociado = %s"
        values = (qr,)
        
        cursor.execute(query, values)
        #db_connection.commit()

        #Obtener resultado

        resultado = cursor.fetchone()

        cursor.close()
        db_connection.close()

        if resultado:
            idusuario = resultado[0]
            return idusuario
        else:
            return None
        
        
    
    except Exception as e:
        print(f"Error al consultar el idUsuario por QR: {e}")
        return None

#prueba = save_asistencia(11)
#print(prueba)
