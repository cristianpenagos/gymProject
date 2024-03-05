import cv2
from pyzbar.pyzbar import decode


def qr_cam():

    import cv2
    from pyzbar.pyzbar import decode
    # Inicializar la cámara
    cap = cv2.VideoCapture(0)

    qr_data = 0

    while True:
        # Capturar un frame desde la cámara
        ret, frame = cap.read()

        # Decodificar códigos QR con pyzbar
        decoded_objects = decode(frame)

        # Imprimir la información del QR si se detecta
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            print(f"QR Code Data: {qr_data}")

        # Mostrar el frame resultante
        cv2.imshow("QR Code Scanner", frame)

        # Romper el bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        return qr_data

    # Liberar la cámara y cerrar la ventana
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    qr_cam()
