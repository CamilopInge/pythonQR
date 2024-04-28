import cv2
from pyzbar.pyzbar import decode
from datetime import datetime

def leer_qr():
    # Inicializar la cámara
    cap = cv2.VideoCapture(0)

    while True:
        # Leer un frame de la cámara
        ret, frame = cap.read()

        # Decodificar el código QR
        qr_codes = decode(frame)

        # Si se detecta un código QR, imprimir su contenido
        if qr_codes:
            contenido_qr = qr_codes[0].data.decode('utf-8')
            print("Contenido del código QR:", contenido_qr)
            break

        # Mostrar el frame en una ventana
        cv2.imshow('QR Scanner', frame)

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la cámara y cerrar la ventana
    cap.release()
    cv2.destroyAllWindows()

# Leer el código QR y mostrar su contenido
leer_qr()
