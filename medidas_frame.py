import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from medidas import Medidas


class MedidasFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=1180, height=690, bg='black')
        self.pack_propagate(False)

        # Interface Elements

        self.label_user = tk.Label(
            self, text="Gestion de Medidas", font=("Times new roman", 14))
        self.label_user.place(x=500, y=10)

        self.label_idusuario = tk.Label(
            self, text="ID User", font=("Times new roman", 14))
        self.entry_idusuario = tk.Entry(self, font=("Times new roman", 14))

        self.label_fecha = tk.Label(
            self, text="Fecha", font=("Times new roman", 14))
        self.entry_fecha = tk.Entry(self, font=("Times new roman", 14))

        self.label_cuelloM = tk.Label(
            self, text="CuelloM", font=("Times new roman", 14))
        self.entry_cuelloM = tk.Entry(self, font=("Times new roman", 14))

        self.label_brazoM = tk.Label(
            self, text="BrazoM", font=("Times new roman", 14))
        self.entry_brazoM = tk.Entry(self, font=("Times new roman", 14))

        self.label_abdomenM = tk.Label(
            self, text="AbdomenM", font=("Times new roman", 14))
        self.entry_abdomenM = tk.Entry(
            self, font=("Times new roman", 14), width=18)

        self.label_caderaM = tk.Label(
            self, text="CaderaM", font=("Times new roman", 14))
        self.entry_caderaM = tk.Entry(self, font=("Times new roman", 14))

        self.label_piernaAltaM = tk.Label(
            self, text="Pierna Alta M", font=("Times new roman", 14))
        self.entry_piernaAltaM = tk.Entry(self, font=("Times new roman", 14))

        self.label_piernaBajaM = tk.Label(
            self, text="Pierna Baja M", font=("Times new roman", 14))
        self.entry_piernaBajaM = tk.Entry(self, font=("Times new roman", 14))

        self.label_pantorrillaM = tk.Label(
            self, text="Pantorrilla M", font=("Times new roman", 14))
        self.entry_pantorrillaM = tk.Entry(self, font=("Times new roman", 14))

        self.label_abdomenG = tk.Label(
            self, text="AbdomenG", font=("Times new roman", 14))
        self.entry_abdomenG = tk.Entry(self, font=("Times new roman", 14))

        self.label_bicepG = tk.Label(
            self, text="Bicep G", font=("Times new roman", 14))
        self.entry_bicepG = tk.Entry(self, font=("Times new roman", 14))

        self.label_tricepG = tk.Label(
            self, text="Tricep G", font=("Times new roman", 14))
        self.entry_tricepG = tk.Entry(self, font=("Times new roman", 14))

        self.label_escapulaG = tk.Label(
            self, text="Escapula", font=("Times new roman", 14))
        self.entry_escapulaG = tk.Entry(self, font=("Times new roman", 14))

        self.label_piernaG = tk.Label(
            self, text="Pierna G", font=("Times new roman", 14))
        self.entry_piernaG = tk.Entry(self, font=("Times new roman", 14))

        self.label_idmedidas = tk.Label(
            self, text="ID Medidas", font=("Times new roman", 14))
        self.entry_idmedidas = tk.Entry(self, font=("Times new roman", 14))

        # Position elements

        self.label_idusuario.place(x=10, y=50)
        self.entry_idusuario.place(x=90, y=50)

        self.label_fecha.place(x=10, y=100)
        self.entry_fecha.place(x=90, y=100)

        self.label_cuelloM.place(x=10, y=150)
        self.entry_cuelloM.place(x=90, y=150)

        self.label_brazoM.place(x=10, y=200)
        self.entry_brazoM.place(x=90, y=200)

        self.label_abdomenM.place(x=10, y=250)
        self.entry_abdomenM.place(x=109, y=250)

        self.label_caderaM.place(x=370, y=50)
        self.entry_caderaM.place(x=490, y=50)

        self.label_piernaAltaM.place(x=370, y=100)
        self.entry_piernaAltaM.place(x=490, y=100)

        self.label_piernaBajaM.place(x=370, y=150)
        self.entry_piernaBajaM.place(x=490, y=150)

        self.label_pantorrillaM.place(x=370, y=200)
        self.entry_pantorrillaM.place(x=490, y=200)

        self.label_abdomenG.place(x=370, y=250)
        self.entry_abdomenG.place(x=490, y=250)

        self.label_bicepG.place(x=780, y=50)
        self.entry_bicepG.place(x=900, y=50)

        self.label_tricepG.place(x=780, y=100)
        self.entry_tricepG.place(x=900, y=100)

        self.label_escapulaG.place(x=780, y=150)
        self.entry_escapulaG.place(x=900, y=150)

        self.label_piernaG.place(x=780, y=200)
        self.entry_piernaG.place(x=900, y=200)

        self.label_idmedidas.place(x=780, y=250)
        self.entry_idmedidas.place(x=900, y=250)

        # BOTONES

        self.btn_save_user = tk.Button(
            self, text="Guardar", command=self.guardar_medidas)
        self.btn_save_user.place(x=350, y=290, width=80, height=80)

        self.btn_delete_user = tk.Button(
            self, text="Consultar", command=self.consultar_medidas)
        self.btn_delete_user.place(x=450, y=290, width=80, height=80)

        self.btn_update_user = tk.Button(
            self, text="Actualizar", command = self.actualizar_medidas)
        self.btn_update_user.place(x=550, y=290, width=80, height=80)

        self.btn_delete_user = tk.Button(
            self, text="Eliminar")
        self.btn_delete_user.place(x=650, y=290, width=80, height=80)

        # TreeView

        # Crear un Treeview para mostrar la tabla de usuarios
        self.treeview = ttk.Treeview(self, columns=("ID", "Nombre", "Fecha", "IDUser", "cuello", "brazoM", 'abdomenM',
                                     "caderaM", "piernaAltM", "piernaBajM", "pantorrillaM", "abdomenG", "bicepG", 'tricepG', 'escapulaG', 'piernaG'), show="headings", height=5)

        # Configurar encabezados de columnas
        for col in ("ID", "Nombre", "Fecha", "IDUser", "cuello", "brazoM", 'abdomenM',
                    "caderaM", "piernaAltM", "piernaBajM", "pantorrillaM", "abdomenG", "bicepG", 'tricepG', 'escapulaG', 'piernaG'):
            self.treeview.heading(col, text=col)

        # Posicionar el Treeview
        self.treeview.place(x=10, y=380, width=1100, height=280)

        # Crear barra de desplazamiento horizontal
        self.scrollbar_h = ttk.Scrollbar(self, orient="horizontal")

        # Vincular la barra de desplazamiento al Treeview
        self.treeview.configure(xscrollcommand=self.scrollbar_h.set)
        self.scrollbar_h.configure(command=self.treeview.xview)

        # Posicionar la barra de desplazamiento
        self.scrollbar_h.place(x=10, y=660, width=1100)

        # Crear barra de desplazamiento vertical
        self.scrollbar_v = ttk.Scrollbar(self, orient="vertical")

        # Vincular la barra de desplazamiento vertical al Treeview
        self.treeview.configure(yscrollcommand=self.scrollbar_v.set)
        self.scrollbar_v.configure(command=self.treeview.yview)

        # Posicionar la barra de desplazamiento vertical
        self.scrollbar_v.place(x=1110, y=380, height=280)

        # INSERT INTO medidas (fecha, cuelloM, brazoM, abdomenM, caderaM, piernaAltaM,
        # piernaBajaM, pantorrillaM, abdomenG, bicepG, tricepG, escapulaG, piernaGm,
        # usuario_idusuario

    def guardar_medidas(self):

        fecha = self.entry_fecha.get()
        cuelloM = self.entry_cuelloM.get()
        brazoM = self.entry_brazoM.get()
        abdomenM = self.entry_abdomenM.get()
        caderaM = self.entry_caderaM.get()
        piernaAltaM = self.entry_piernaAltaM.get()
        piernaBajaM = self.entry_piernaBajaM.get()
        pantorrillaM = self.entry_pantorrillaM.get()
        abdomenG = self.entry_abdomenG.get()
        bicepG = self.entry_bicepG.get()
        tricepG = self.entry_escapulaG.get()
        escapulaG = self.entry_escapulaG.get()
        piernaG = self.entry_piernaG.get()
        idusuario = self.entry_idusuario.get()

        new_medidas = Medidas(idusuario, fecha, cuelloM, brazoM, abdomenM, caderaM, piernaAltaM,
                              piernaBajaM, pantorrillaM, abdomenG, bicepG, tricepG, escapulaG, piernaG)
        mensaje = new_medidas.save_medidas()
        messagebox.showinfo('BodyFit', mensaje)

    def consultar_medidas(self):
        # Limpiar datos anteriores
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Consultar DB
        medidas = Medidas.consult_medidas()

        # Agregar Medidas al treeview
        for medida in medidas:
            self.treeview.insert('', 'end', values=medida)

        # ajustar anchos columnas
            self.treeview.column('ID', width=30)
            self.treeview.column("Nombre", width=150)
    
    def actualizar_medidas(self):

        idmedidas = self.entry_idmedidas.get()
        fecha = self.entry_fecha.get()
        cuelloM = self.entry_cuelloM.get()
        brazoM = self.entry_brazoM.get()
        abdomenM = self.entry_abdomenM.get()
        caderaM = self.entry_caderaM.get()
        piernaAltaM = self.entry_piernaAltaM.get()
        piernaBajaM = self.entry_piernaBajaM.get()
        pantorrillaM = self.entry_pantorrillaM.get()
        abdomenG = self.entry_abdomenG.get()
        bicepG = self.entry_bicepG.get()
        tricepG = self.entry_escapulaG.get()
        escapulaG = self.entry_escapulaG.get()
        piernaG = self.entry_piernaG.get()
        idusuario = self.entry_idusuario.get()

        modify_medidas = Medidas(fecha, cuelloM, brazoM, abdomenM, caderaM, piernaAltaM, piernaBajaM, pantorrillaM, abdomenG, bicepG, tricepG, escapulaG, piernaG, idusuario)

        mensaje = modify_medidas.update_medida(idmedidas, fecha, cuelloM, brazoM, abdomenM, caderaM, piernaAltaM, piernaBajaM, pantorrillaM, abdomenG, bicepG, tricepG, escapulaG, piernaG, idusuario)
        messagebox.showinfo('BodyFit', mensaje)

#  def update_medida(self, idmedidas, fecha, cuelloM, brazoM, abdomenM, caderaM, piernaAltaM, piernaBajaM, pantorrillaM, abdomenG, bicepG, tricepG, escapulaG, piernaG, usuario_idusuario):