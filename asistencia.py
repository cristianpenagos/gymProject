from conexion import conectar

#def save_asistencia():



def consultarIDUsuario(cls, qr):
    try:
        db_connection = conectar()
        cursor = db_connection.cursor()

        query = "SELECT idusuario FROM usuario WHERE qrAsociado = %s"
        values = (qr)
        
        cursor.execute(query, values)
        db_connection.commit()

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



prueba = consultarIDUsuario(1)
print(prueba)