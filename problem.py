import cv2
from pyzbar.pyzbar import decode


def main():
    # Inicializar la cámara
    cap = cv2.VideoCapture(0)

    while True:
        # Capturar un frame desde la cámara
        ret, frame = cap.read()

        # Decodificar códigos QR
        decoded_objects = decode(frame)

        # Dibujar los resultados en el frame
        for obj in decoded_objects:
            # Extraer la información del QR
            qr_data = obj.data.decode('utf-8')
            print(f"QR Code Data: {qr_data}")

            # Dibujar un rectángulo alrededor del código QR
            points = obj.polygon
            if len(points) == 4:
                hull = cv2.convexHull(points)
                cv2.polylines(frame, [hull], True, (0, 255, 0), 2)

        # Mostrar el frame resultante
        cv2.imshow("QR Code Scanner", frame)

        # Romper el bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la cámara y cerrar la ventana
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
