import cv2
from pyzbar.pyzbar import decode


def detect_qr_code(image_path):
    # Cargar la imagen
    image = cv2.imread(image_path)

    # Decodificar códigos QR con pyzbar
    decoded_objects = decode(image)

    # Imprimir la información del QR si se detecta
    for obj in decoded_objects:
        qr_data = obj.data.decode('utf-8')
        print(f"QR Code Data: {qr_data}")

    # Si no se detectaron códigos QR
    if not decoded_objects:
        print("No QR codes found in the image.")

    # Mostrar la imagen con los códigos QR resaltados
    cv2.imshow("QR Code Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Ruta de la imagen que contiene el código QR
    image_path = "C:\qr2.png"  # Reemplaza con la ruta de tu imagen
    detect_qr_code(image_path)
