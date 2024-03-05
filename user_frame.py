import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from user import User


class UserFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=1300, height=700, bg='lightblue')
        self.pack_propagate(False)

        # Interface Elements

        self.label_user = tk.Label(self, text="Gestion de Usuarios", font=("Times new roman", 14))
        self.label_user.place(x=600, y=10)

        self.name_label = tk.Label(self, text="Nombre", font=("Times new roman", 14))
        self.entry_name = tk.Entry(self, font=("Times new roman", 14))

        self.label_cedula = tk.Label(self, text='Cedula', font=("Times new roman", 14))
        self.entry_cedula = tk.Entry(self, font=("Times new roman", 14))

        self.label_fNacimiento = tk.Label(self, text='F. Nacimiento', font=("Times new roman", 14))
        self.entry_fNacimiento = tk.Entry(self, font=("Times new roman", 14))

        self.label_telefono = tk.Label(self, text='Telefono', font=("Times new roman", 14))
        self.entry_telefono = tk.Entry(self, font=("Times new roman", 14))

        self.label_fRegistro = tk.Label(self, text='F. Registro', font=("Times new roman", 14))
        self.entry_fRegistro = tk.Entry(self, font=("Times new roman", 14))

        self.label_qr = tk.Label(self, text='QR', font=("Times new roman", 14))
        self.entry_qr = tk.Entry(self, font=("Times new roman", 14))

        self.label_cGrupales = tk.Label(self, text='Cl. Grupales', font=("Times new roman", 14))
        self.entry_cGrupales = tk.Entry(self, font=("Times new roman", 14))

        self.label_enfermedades = tk.Label(self, text='Enfermedades', font=("Times new roman", 14))
        self.entry_enfermedades = tk.Entry(self, font=("Times new roman", 14))

        self.label_objetivos = tk.Label(self, text='Objetivos', font=("Times new roman", 14))
        self.entry_objetivos = tk.Entry(self, font=("Times new roman", 14))

        self.label_notasGenerales = tk.Label(self, text='Notas \n Generales', font=("Times new roman", 14))
        self.entry_notasGenerales = tk.Entry(self, font=("Times new roman", 14))

        self.label_direccion = tk.Label(self, text='Dirección', font=("Times new roman", 14))
        self.entry_direccion = tk.Entry(self, font=("Times new roman", 14))

        self.label_IDBD = tk.Label(self, text="ID Base \nde Datos", font=("Times new roman", 14))
        self.entry_IDBD = tk.Entry(self, font=("Times new roman", 14))

        # Crear un Treeview para mostrar la tabla de usuarios
        self.treeview = ttk.Treeview(self, columns=("ID", "Nombre", "Cedula", "FNacimiento", "Telefono", "FRegistro",
                                     "QR", "Cl. Grupales", "Enfermedades", "Objetivos", "NGenerales", "Direccion"), show="headings", height=5)

        # Configurar encabezados de columnas
        for col in ("ID", "Nombre", "Cedula", "FNacimiento", "Telefono", "FRegistro", "QR", "Cl. Grupales", "Enfermedades", "Objetivos", "NGenerales", "Direccion"):
            self.treeview.heading(col, text=col)

        # Posicionar el Treeview
        self.treeview.place(x=10, y=300, width=1100, height=280)

        # Botón para cargar y mostrar usuarios
        self.btn_consultar = tk.Button(
            self, text="Consultar Usuarios", command=self.consultar_usuarios)
        self.btn_consultar.place(x=300, y=250)

        # Position elements

        self.name_label.place(x=10, y=50)
        self.entry_name.place(x=80, y=50)

        self.label_cedula.place(x=10, y=100)
        self.entry_cedula.place(x=80, y=100)

        self.label_fNacimiento.place(x=10, y=150)
        self.entry_fNacimiento.place(x=80, y=150)

        self.label_telefono.place(x=10, y=200)
        self.entry_telefono.place(x=80, y=200)

        self.label_fRegistro.place(x=350, y=50)
        self.entry_fRegistro.place(x=450, y=50)

        self.label_qr.place(x=350, y=100)
        self.entry_qr.place(x=450, y=100)

        self.label_cGrupales.place(x=350, y=150)
        self.entry_cGrupales.place(x=450, y=150)

        self.label_enfermedades.place(x=350, y=200)
        self.entry_enfermedades.place(x=450, y=200)

        self.label_objetivos.place(x=800, y=50)
        self.entry_objetivos.place(x=900, y=50)

        self.label_notasGenerales.place(x=800, y=100)
        self.entry_notasGenerales.place(x=900, y=100)

        self.label_direccion.place(x=800, y=150)
        self.entry_direccion.place(x=900, y=150)

        self.label_IDBD.place(x=800, y=200)
        self.entry_IDBD.place(x=900, y=200)

        self.btn_save_user = tk.Button(
            self, text="Guardar", command=self.guardar_usuario)
        self.btn_save_user.place(x=100, y=250)

        self.btn_update_user = tk.Button(
            self, text="Actualizar", command=self.update_user)
        self.btn_update_user.place(x=500, y=250)

        self.btn_delete_user = tk.Button(
            self, text="Eliminar", command=self.delete_user)
        self.btn_delete_user.place(x=600, y=250)

    def guardar_usuario(self):

        nombre = self.entry_name.get()
        numIdentificacion = self.entry_cedula.get()
        fechaNacimiento = self.entry_fNacimiento.get()
        telefono = self.entry_telefono.get()
        fechaRegistro = self.entry_fRegistro.get()
        qrAsociado = self.entry_qr.get()
        cGrupales = self.entry_cGrupales.get()
        enfermedades = self.entry_enfermedades.get()
        objetivos = self.entry_objetivos.get()
        notasGenerales = self.entry_notasGenerales.get()
        direccion = self.entry_direccion.get()

        new_user = User(nombre, numIdentificacion, fechaNacimiento, telefono, fechaRegistro,
                        qrAsociado, cGrupales, enfermedades, objetivos, notasGenerales, direccion)
        mensaje = new_user.save_user()
        messagebox.showinfo("BodyFIT", mensaje)

    def consultar_usuarios(self):
        # Limpiar datos anteriores del Treeview
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Consultar usuarios desde la base de datos
        users = User.consult_user()

        # Agregar usuarios al Treeview
        for user in users:
            self.treeview.insert("", "end", values=user)

        # Ajustar anchos de columna después de insertar datos
        self.treeview.column("ID", width=30)
        self.treeview.column("Nombre", width=120)
        self.treeview.column("Cedula", width=90)
        self.treeview.column("FNacimiento", width=100)
        self.treeview.column("Telefono", width=91)
        self.treeview.column("Fecha Registro", width=70)
        self.treeview.column("QR", width=30)
        self.treeview.column("Cl. Grupales", width=30)
        self.treeview.column("Enfermedades", width=120)
        self.treeview.column("Objetivos", width=120)
        self.treeview.column("Notas Generales", width=91)
        self.treeview.column("Direccion", width=91)

    def update_user(self):
        idusuario = self.entry_IDBD.get()
        nombre = self.entry_name.get()
        numIdentificacion = self.entry_cedula.get()
        fechaNacimiento = self. entry_fNacimiento.get()
        telefono = self.entry_telefono.get()
        fechaRegistro = self.entry_fRegistro.get()
        qrAsociado = self.entry_qr.get()
        cGrupales = self.entry_cGrupales.get()
        enfermedades = self.entry_enfermedades.get()
        objetivos = self.entry_objetivos.get()
        notasGenerales = self.entry_notasGenerales.get()
        direccion = self.entry_direccion.get()

        modify_user = User(nombre, numIdentificacion, fechaNacimiento, telefono, fechaRegistro,
                           qrAsociado, cGrupales, enfermedades, objetivos, notasGenerales, direccion)

        mensaje = modify_user.update_user(idusuario, nombre, numIdentificacion, fechaNacimiento, telefono, fechaRegistro,
                                          qrAsociado, cGrupales, enfermedades, objetivos, notasGenerales, direccion)
        messagebox.showinfo("BodyFit", mensaje)

    def delete_user(self):

        userToDelete = self.entry_IDBD.get()
        mensaje = User.delete_user(userToDelete)
        messagebox.showinfo("BodyFit", mensaje)
