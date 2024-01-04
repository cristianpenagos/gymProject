import qrcode
from PIL import Image


def generarQr(texto):

    # Tomar la imagen que el usuario desea en el centro del código QR
    logo_link = 'logo.png'
    logo = Image.open(logo_link)

    # Tomar el ancho base
    basewidth = 80

    # Ajustar el tamaño de la imagen
    wpercent = (basewidth / float(logo.size[0]))
    hsize = int((float(logo.size[1]) * float(wpercent)))
    logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

    # Crear un objeto QRCode
    qr_code = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

    # Tomar la informacion para generar QR
    infoQr = texto

    # Agregar la informacion al QRCode
    qr_code.add_data(infoQr)

    # Generar el código QR
    qr_code.make()

    # Tomar el color del usuario
    qr_color = 'Black'

    # Generar la imagen del código QR
    qr_img = qr_code.make_image(
        fill_color=qr_color, back_color="white").convert('RGBA')

    # Establecer el tamaño del código QR
    pos = ((qr_img.size[0] - logo.size[0]) // 2,
           (qr_img.size[1] - logo.size[1]) // 2)

    # Superponer el logo en el código QR sin rellenar la transparencia
    qr_img.paste(logo, pos, logo)

    # Nombre del archivo QR
    nameQR = texto

    # Guardar el código QR generado
    qr_img.save(str(nameQR)+'.png')


generarQr(1771)

print('Código QR generado!')
