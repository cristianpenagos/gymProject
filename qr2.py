import qrcode
from PIL import Image


def generar_qr_con_espacio_en_blanco_en_medio(datos, output_filename):
    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(datos)
    qr.make(fit=True)

    # Crear la imagen del código QR
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Obtener el tamaño de la imagen del código QR
    width, height = qr_img.size

    # Tamaño del espacio en blanco en la mitad
    espacio_en_blanco_width = width // 2
    espacio_en_blanco_height = height // 2

    # Crear una nueva imagen con el espacio en blanco en la mitad
    nueva_imagen = Image.new(
        "RGB", (width + espacio_en_blanco_width, height + espacio_en_blanco_height), "white")

    # Pegar el código QR en el centro de la nueva imagen
    nueva_imagen.paste(qr_img, (espacio_en_blanco_width //
                       2, espacio_en_blanco_height // 2))

    # Guardar la imagen resultante
    nueva_imagen.save(output_filename)


if __name__ == "__main__":
    # Datos para el código QR
    datos = "https://www.ejemplo.com"

    # Nombre de archivo de salida para el código QR con espacio en blanco en la mitad
    output_filename = "qr_con_espacio_en_blanco_en_medio.png"

    # Generar el código QR con espacio en blanco en la mitad
    generar_qr_con_espacio_en_blanco_en_medio(datos, output_filename)
