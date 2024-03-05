import tkinter as tk
from tkinter import ttk
from mensualidad import Mensualidad
from tkinter import messagebox


class MensualidadFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=1180, height=700, background="lightblue")
        self.pack_propagate(False)

        # Interface elements

        self.label_mensualidad = tk.Label(
            self, text="MENSUALIDAD", font=("Times new roman", 14))
        self.label_mensualidad.place(x=500, y=10)

        self.label_fecha = tk.Label(
            self, text="Fecha\n de pago", font=("Times new roman", 14))
        self.entry_fecha = tk.Entry(self, font=("Times new roman", 14))

        self.label_valor = tk.Label(
            self, text="Valor", font=("Times new roman", 14))
        self.entry_valor = tk.Entry(self, font=("Times new roman", 14))

        self.label_plan = tk.Label(
            self, text="Plan", font=("Times new roman", 14))
        self.entry_plan = tk.Entry(self, font=("Times new roman", 14))

        self.label_usuario = tk.Label(
            self, text="Usuario\nID", font=("Times new roman", 14))
        self.entry_usuario = tk.Entry(self, font=("Times new roman", 14))

        self.label_Mensualidad_ID = tk.Label(
            self, text='Mensualidad\nID', font=("Times new roman", 14))
        self.entry_Mensualidad_ID = tk.Entry(
            self, font=("Times new roman", 14))

        self.btn_save_user = tk.Button(
            self, text="Guardar", command=self.guardar_mensualidad)
        self.btn_save_user.place(x=100, y=250)

        self.btn_save_user = tk.Button(
            self, text="Consultar", command=self.read_mensualidad)
        self.btn_save_user.place(x=200, y=250)

        self.btn_update_user = tk.Button(
            self, text="Actualizar", command=self.update_mensualidad)
        self.btn_update_user.place(x=500, y=250)

        self.btn_delete_user = tk.Button(
            self, text="Eliminar", command=self.delete_mensualidad)
        self.btn_delete_user.place(x=600, y=250)

        # Position elements

        self.label_fecha.place(x=10, y=50)
        self.entry_fecha.place(x=80, y=50)

        self.label_valor.place(x=10, y=100)
        self.entry_valor.place(x=80, y=100)

        self.label_plan.place(x=10, y=150)
        self.entry_plan.place(x=80, y=150)

        self.label_usuario.place(x=10, y=200)
        self.entry_usuario.place(x=80, y=200)

        self.label_Mensualidad_ID.place(x=350, y=50)
        self.entry_Mensualidad_ID.place(x=450, y=50)

        # Crear TreeView
        self.treeview = ttk.Treeview(self, columns=('ID',
                                                    'Fecha', 'Valor', 'Plan', 'Usuario ID', 'Nombre'), show="headings", height=5)

        # Configurar encabezados de columnas
        for col in ('ID', 'Fecha', "Valor", "Plan", "Usuario ID", 'Nombre'):
            self.treeview.heading(col, text=col)

        # Posicionar el Treeview
        self.treeview.place(x=10, y=300, width=1100)

    def guardar_mensualidad(self):
        fecha = self.entry_fecha.get()
        valor = self.entry_valor.get()
        plan = self.entry_plan.get()
        usuario = self.entry_usuario.get()

        new_mensualidad = Mensualidad(fecha, valor, plan, usuario)
        mensaje = new_mensualidad.save_mensualidad()
        messagebox.showinfo('BodyFit', mensaje)

    def read_mensualidad(self):

        # Limpiar datos anteriores del Treeview
        for row in self.treeview.get_children():
            self.treeview.delete(row)

        # Consultar pagos desde la base de datos
        pagos = Mensualidad.consult_mensualidades()

        # Agregar pagos al Treeview
        for pago in pagos:
            self.treeview.insert("", "end", values=pago)

        # Ajustar anchos de columna después de insertar datos
        self.treeview.column("ID", width=30)
        self.treeview.column("Fecha", width=120)
        self.treeview.column("Valor", width=100)
        self.treeview.column("Plan", width=91)
        self.treeview.column("Usuario ID", width=70)
        self.treeview.column("Nombre", width=70)

    def update_mensualidad(self):
        idmensualidad = self.entry_Mensualidad_ID.get()
        fecha = self.entry_fecha.get()
        valor = self.entry_valor.get()
        plan = self.entry_plan.get()
        usuario = self.entry_usuario.get()

        mensaje = Mensualidad.update_pay(
            idmensualidad, fecha, valor, plan, usuario)
        messagebox.showinfo('BodyFit', mensaje)

    def delete_mensualidad(self):

        mensualidad_to_delete = self.entry_Mensualidad_ID.get()
        mensaje = Mensualidad.delete_pay(mensualidad_to_delete)
        messagebox.showwarning("BodyFit", mensaje)
