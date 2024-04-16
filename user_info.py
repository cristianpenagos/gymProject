import tkinter as tk
from cam import qr_cam
import time
from conexion import conectar
import cv2
from tkinter import PhotoImage
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode
from datetime import datetime, date
from asistencia import save_asistencia


class UserInfo_Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=1300, height=700, bg="black")
        self.pack_propagate(False)

        # variables
        self.name = "**BODYFIT**"
        self.dateInit = "2022-01-01"
        self.last_pay = "2022-01-01"
        numDaysLeft = "06"
        numLocker = "05"
        self.plan = 0
        self.cGrupales = 0

        # Interface Elements

        self.cgrupalesLabel = tk.Label(
            self, text="Clases\nGrupales", font='Arial 30')
        self.cgrupalesLabel.config(bg="black", fg="white")
        self.cgrupalesLabel.place(x=1050, y=170)

        self.cgrupalesData = tk.Label(
            self, text=self.cGrupales, font='Arial 30')
        self.cgrupalesData.config(text=self.cGrupales, bg="black", fg="white")
        self.cgrupalesData.place(x=1080, y=250)

        self.startLabel = tk.Label(self, text='Fecha inicio', font='Arial 30')
        self.startLabel.config(bg="black", fg="white")
        self.startLabel.place(x=130, y=200)

        self.startDate = tk.Label(
            self, text=str(self.dateInit), font='Arial 30')
        self.startDate.config(bg="black", fg="white")
        self.startDate.place(x=130, y=250)

        self.montPayLabel = tk.Label(
            self, text='Ult. Pago\nMensualidad', font='Arial 30')
        self.montPayLabel.config(bg="black", fg="white")
        self.montPayLabel.place(x=550, y=160)

        self.montPayDate = tk.Label(self, text=self.last_pay, font='Arial 30')
        self.montPayDate.config(bg="black", fg="white")
        self.montPayDate.place(x=550, y=250)

        self.planLabel = tk.Label(
            self, text="Plan:", font='Arial 30')
        self.planLabel.config(bg="black", fg="white")
        self.planLabel.place(x=915, y=200)

        self.plan_date = tk.Label(
            self, text=self.plan, font='Arial 30')
        self.plan_date.config(bg="black", fg="white")
        self.plan_date.place(x=915, y=250)

        self.lockerLabel = tk.Label(self, text='Locker', font='Arial 40')
        self.lockerLabel.config(bg="black", fg="white")
        self.lockerLabel.place(x=960, y=310)

        self.lockerNum = tk.Label(
            self, text=numLocker, font='arial 200')  # ff04b7
        self.lockerNum.config(bg="#ff04b7")
        self.lockerNum.place(x=910, y=370)

        self.remainingDaysBox = tk.Label(
            self, text='Dias Restantes', font='Arial 40')
        self.remainingDaysBox.config(bg="black", fg="white")
        self.remainingDaysBox.place(x=80, y=310)

        self.remainingDaysBoxNum = tk.Label(
            self, text=numDaysLeft, font='Arial 200')  # 28b7fe
        self.remainingDaysBoxNum.config(bg="#28b7fe")
        self.remainingDaysBoxNum.place(x=90, y=370)

        # Name User Label
        self.nameUser = tk.Label(self, text=self.name, font="Arial 40")
        self.nameUser.config(bg="black", fg="white")
        self.nameUser.place(x=450, y=80)

        # Logo Label

        # declarar como variable de clase
        self.imagen = tk.PhotoImage(file="logo2.png").subsample(
            2, 2)  # ajusta según sea necesario
        labelLogo = tk.Label(self, image=self.imagen)
        labelLogo.config(width=150, height=150, bg='black')
        self.imagen.configure(width=150, height=150)
        labelLogo.place(x=20, y=20)

     # Cámara
        self.camera_label = tk.Label(self, bg='black')
        self.camera_label.place(x=450, y=380)

        # Iniciar la cámara
        self.cap = cv2.VideoCapture(0)  # Start video capture
        self.last_qr_data = None
        self.update_camera()
        self.qr_control = 0

    def update_camera(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            resized_image = image.resize((400, 280), Image.ANTIALIAS)  #Esta linea no funciona en pc julian
            # Funciona la siguiente debido al PIL.Image:               resized_image = image.resize((350, 250), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image=resized_image)
            self.camera_label.configure(image=photo)
            self.camera_label.image = photo

            # Reconocer QR
            qr_data = self.decode_qr(frame)

            # Actualizar el número detectado en la interfaz y por consola
            if qr_data is not None and qr_data != self.last_qr_data:
                print(f"QR Code Data: {qr_data}")
                self.last_qr_data = qr_data
                save_asistencia(self.last_qr_data)
                # llamamos a update_data para consultar DB y actualizar pantalla
                self.update_data(qr_data)

            # Actualizar cada 10 milisegundos
            self.after(10, self.update_camera)
        else:
            print("Error al capturar el cuadro de la cámara.")

    def decode_qr(self, frame):
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            qr_data = obj.data.decode('utf-8')
            print(qr_data)
            if qr_data.isdigit():
                return int(qr_data)  # Devuelve el número entero del QR
        return None

    def update_data(self, last_qr_data):

        if self.qr_control != last_qr_data:

            self.qr_control = last_qr_data

            db_connection = conectar()
            cursor = db_connection.cursor()
            query = """SELECT
                        usuario.nombre,
                        usuario.fechaRegistro,
                        usuario.cGrupales,
                        MAX(mensualidad.fecha) AS ultimaFechaPago,
                        MAX(mensualidad.plan) AS ultimoPlan
                        FROM
                        usuario
                        LEFT JOIN mensualidad ON usuario.idusuario = mensualidad.usuario_idusuario
                        WHERE
                        usuario.qrAsociado = %s
                        GROUP BY
                        usuario.idusuario, usuario.nombre, usuario.fechaRegistro, usuario.cGrupales;"""
            values = (self.qr_control,)
            cursor.execute(query, values)
            results = cursor.fetchall()
            if results:  # Verificamos si hay resultados
                # Tomamos el primer elemento del primer resultado
                self.name = results[0][0]
                self.dateInit = results[0][1]
                self.cGrupales = results[0][2]
                self.last_pay = results[0][3]
                self.plan = results[0][4]
                # Actualizar el texto del label
                self.nameUser.config(text=self.name)
                self.startDate.config(text=self.dateInit)
                self.cgrupalesData.config(text=self.cGrupales)
                self.montPayDate.config(text=self.last_pay)
                self.plan_date.config(text=self.plan)
                self.remainingDaysBoxNum.config(
                    text=self.dias_restantes(self.last_pay))
                print(f"Usuario actualizado: {self.name}")
                print(self.name, self.dateInit,
                      self.cGrupales, self.last_pay, self.plan)
                print(self.cGrupales)

            db_connection.commit()
            cursor.close()
            db_connection.close()

    def dias_restantes(self, fp):
        constante = 30
        fp = fp
        fa = date.today()

        print(f'Fecha de pago: {fp}')
        print(f'Fecha actual: {fa}')

        dias_transcurridos = (fa - fp).days
        print(dias_transcurridos)
        dias_restante = max(constante - dias_transcurridos, 0)
        return dias_restante
