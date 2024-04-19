import tkinter as tk
from user_frame import UserFrame
from mensualidad_frame import MensualidadFrame
from user_info import UserInfo_Frame
from backup import backup
from tkinter import messagebox
from medidas_frame import MedidasFrame


class UserGui:
    def __init__(self, root):

        self.iconUser = tk.PhotoImage(file = 'asets/iconUser.png')
        self.iconMedidas = tk.PhotoImage(file = "asets/iconMedidas.png")
        self.iconMensualidad = tk.PhotoImage(file = "asets/iconMensualidad.png")
        self.iconQr = tk.PhotoImage(file = "asets/iconQr.png")
        self.iconBackup = tk.PhotoImage(file = "asets/iconBackup.png")

        # Principal Window
        self.root = root
        self.root.title('BODY FIT')
        self.root.geometry('1300x700')

        
        self.btm_user = tk.Button(
            root, image=self.iconUser, text="Gestión \nUsuarios", font=("Times new roman", 14), command=self.show_user_frame)
        self.btm_medidas = tk.Button(
            root, image=self.iconMedidas, text="Medidas", font=("Times new roman", 14), command=self.show_medidas_frame)
        self.btm_mensualidad = tk.Button(
            root, image=self.iconMensualidad, text='Mensualidad', font=("Times new roman", 14), command=self.show_mensualidad_frame)
        self.btn_qr = tk.Button(root, image=self.iconQr, text="Activar QR",
                                font=("Times new roman", 14), command=self.active_qr)
        self.btm_backup = tk.Button(
            root, image=self.iconBackup, text='BackUp', font=("Times new roman", 14), command=self.respaldo)
        self.btm_ingresos = tk.Button()
    
        self.btm_user.place(x=10, y=10, width=100, height=100)
        self.btm_medidas.place(x=10, y=120, width=100, height=100)
        self.btm_mensualidad.place(x=10, y=240, width=100, height=100)
        self.btn_qr.place(x=10, y=480, width=100, height=100)
        self.btm_backup.place(x=10, y=580, width=100, height=100)

        self.user_frame = UserFrame(root)
        self.mensualidad_frame = MensualidadFrame(root)
        self.medidas_frame = MedidasFrame(root)
        # self.medidas_frame = tk.Frame(
        #    root, width=300, height=300, bg='lightgreen')

    def show_user_frame(self):
        self.hide_frames()
        self.user_frame.place(x=130, y=10)

    def show_medidas_frame(self):
        self.hide_frames()
        self.medidas_frame.place(x=130, y=10)

    def show_mensualidad_frame(self):
        self.hide_frames()
        self.mensualidad_frame.place(x=130, y=10)

    def hide_frames(self):
        self.user_frame.place_forget()
        self.medidas_frame.place_forget()
        self.mensualidad_frame.place_forget()

    def active_qr(self):
        window_detect = tk.Toplevel()
        window_detect.title("BodyFit")
        window_detect.geometry("1300x700")

        user_info_frame = UserInfo_Frame(window_detect)
        user_info_frame.pack()

    def respaldo(self):

        mensaje = backup()
        messagebox.showinfo('BodyFit', mensaje)


if __name__ == "__main__":
    root = tk.Tk()
    usergui = UserGui(root)
    root.mainloop()
