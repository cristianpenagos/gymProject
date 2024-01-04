import cv2
from pyzbar.pyzbar import decode


def leer_codigo_qr():
    # Inicializar la cámara
    cap = cv2.VideoCapture(0)

    # Configurar la resolución a 1920x1080
    # cap.set(3, 1920)  # Ancho de la resolución
    # cap.set(4, 1080)  # Altura de la resolución

    # Configurar la tasa de fotogramas a 30 FPS+
    cap.set(cv2.CAP_PROP_FPS, 60)

    while True:
        # Capturar un fotograma de la cámara
        ret, frame = cap.read()

        # Decodificar los códigos QR en el fotograma
        codigos_qr = decode(frame)

        # Mostrar el fotograma
        cv2.imshow('QR Code Scanner', frame)

        # Comprobar si se ha encontrado algún código QR
        if codigos_qr:
            # Imprimir el contenido del código QR
            for codigo_qr in codigos_qr:
                print("Contenido del código QR:",
                      codigo_qr.data.decode('utf-8'))

            # Detener la captura de video
            break

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la cámara y cerrar la ventana
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    leer_codigo_qr()
