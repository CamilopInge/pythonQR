import qrcode
from datetime import datetime

def generar_qr(id_usuario):
    # Obtener la fecha y hora actual
    fecha_actual = datetime.now().strftime('%Y-%m-%d')
    hora_actual = datetime.now().strftime('%H:%M:%S')

    # Combinar el ID de usuario, la fecha y la hora actual
    datos_qr = f"ID: {id_usuario}, FECHA: {fecha_actual}, HORA: {hora_actual}"

    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(datos_qr)
    qr.make(fit=True)

    # Crear una imagen del código QR
    imagen = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen
    nombre_archivo = f"codigo_qr_{id_usuario}_{fecha_actual}_{hora_actual.replace(':', '')}.png"
    imagen.save(nombre_archivo)

    print(f"Se ha generado el código QR y se ha guardado en el archivo {nombre_archivo}")

# Generar y guardar el código QR


  # ID de usuario (por ejemplo)
print(f"Ingrese el ID del usuario")
id_usuario = input() 

generar_qr(id_usuario)
