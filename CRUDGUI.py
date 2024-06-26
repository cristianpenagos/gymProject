import tkinter as tk
from otrosIngresos import OtrosIngresos
from datetime import datetime
from tkinter import messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Ingresos")
        self.root.geometry("600x400")

        # Elementos de la interfaz
        self.label_elemento = tk.Label(root, text="Elemento:")
        self.entry_elemento = tk.Entry(root)

        self.label_consultas = tk.Label(root, text="Consultas: ")
        self.label_viewConsultas = tk.Label(root, text="")
        self.update_queries()

        self.label_valor = tk.Label(root, text="Valor:")
        self.entry_valor = tk.Entry(root)

        self.label_fecha = tk.Label(root, text="Fecha:")
        self.entry_fecha = tk.Entry(root)
        self.entry_fecha.insert(0, self.fechaActual())

        self.btn_guardar = tk.Button(
            root, text="Guardar", command=self.guardar)
        self.btn_consultar = tk.Button(
            root, text="Consultar", command=self.update_queries)
        self.btn_modificar = tk.Button(
            root, text="Modificar", command=self.modificar)
        self.btn_eliminar = tk.Button(
            root, text="Eliminar", command=self.eliminar)

        # Organizar los elementos en la interfaz
        self.label_elemento.grid(row=0, column=0)
        self.entry_elemento.grid(row=0, column=1)

        self.label_consultas.grid(row=0, column=3)
        self.label_viewConsultas.grid(row=1, column=3)

        self.label_valor.grid(row=1, column=0)
        self.entry_valor.grid(row=1, column=1)

        self.label_fecha.grid(row=2, column=0)
        self.entry_fecha.grid(row=2, column=1)

        self.btn_guardar.grid(row=3, column=0)
        self.btn_consultar.grid(row=3, column=1)

        self.btn_modificar.grid(row=5, column=0)
        self.btn_eliminar.grid(row=5, column=1)

    def fechaActual(self):
        return datetime.now().strftime("%Y-%m-%d")

    def guardar(self):
        elemento = self.entry_elemento.get()
        valor = int(self.entry_valor.get())
        fecha = self.entry_fecha.get()

        ingreso = OtrosIngresos(elemento, valor, fecha)
        mensaje = ingreso.guardar()
        messagebox.showinfo("BodyFit", mensaje)

    def update_queries(self):
        text_consulta = OtrosIngresos.consultar_todos()
        self.label_viewConsultas.config(text=text_consulta)

    def modificar(self):

        # Creacion de la emergente
        window_update = tk.Toplevel(self.root)
        window_update.title("Modificar Ingreso")
        window_update.geometry("250x150")

        # Elementos Emergente

        self.id = tk.Label(window_update, text="ID:")
        self.entry_id = tk.Entry(window_update)

        self.mod_elemento = tk.Label(window_update, text="Elemento")
        self.entry_mod_elemento = tk.Entry(window_update)

        self.mod_valor = tk.Label(window_update, text="Valor: ")
        self.entry_mod_valor = tk.Entry(window_update)

        self.mod_fecha = tk.Label(window_update, text="Fecha: ")
        self.entry_mod_fecha = tk.Entry(window_update)

        self.btn_mod = tk.Button(
            window_update, text="Modificar", command=self.acept_mod)

        # acomodar elementos en el grid

        self.id.grid(row=0, column=0)
        self.entry_id.grid(row=0, column=1)

        self.mod_elemento.grid(row=1, column=0)
        self.entry_mod_elemento.grid(row=1, column=1)

        self.mod_valor.grid(row=3, column=0)
        self.entry_mod_valor.grid(row=3, column=1)

        self.mod_fecha.grid(row=4, column=0)
        self.entry_mod_fecha.grid(row=4, column=1)

        self.btn_mod.grid(row=5, column=1)

    def acept_mod(self):

        id_element = self.entry_id.get()
        name_element = self.entry_mod_elemento.get()
        valor_elemento = self.entry_mod_valor.get()
        fecha_elemento = self.entry_mod_fecha.get()
        element_to_mod = OtrosIngresos(
            name_element, valor_elemento, fecha_elemento)
        mensaje = element_to_mod.actualizar(
            id_element, name_element, valor_elemento, fecha_elemento)

        messagebox.showinfo("bodyFit", mensaje)

        # confirmacion_box = tk.Toplevel(self.root)
        # mess_label = tk.Label(confirmacion_box, text=mensaje)
        # mess_label.grid(row=0, column=0)

    def eliminar(self):

        # Creacion de la emergente
        window_delete = tk.Toplevel(self.root)
        window_delete.title("Eliminar")
        window_delete.geometry("250x80")

        # Elementos de la emergente
        self.id = tk.Label(window_delete, text="ID:")
        self.entry_id_delete = tk.Entry(window_delete)

        self.confirm_eliminar = tk.Button(
            window_delete, text="Eliminar", command=self.confirmar_eliminar)

        # Acomodar elementos en el grid
        self.id.grid(row=0, column=2)
        self.entry_id_delete.grid(row=0, column=4)
        self.confirm_eliminar.grid(row=1, column=3, columnspan=2, pady=10)

    def confirmar_eliminar(self):

        id_delete = self.entry_id_delete.get()

        mensaje = OtrosIngresos.eliminar(id_delete)

        messagebox.showinfo("BodyFit", mensaje)

        # confirmacion_box = tk.Toplevel(self.root)
        # confirm_mes = tk.Label(confirmacion_box, text=mensaje)

        # confirm_mes.grid(row=0, column=0)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
