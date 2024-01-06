import tkinter as tk
from otrosIngresos import OtrosIngresos

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Ingresos")

        # Elementos de la interfaz
        self.label_elemento = tk.Label(root, text="Elemento:")
        self.entry_elemento = tk.Entry(root)

        self.label_valor = tk.Label(root, text="Valor:")
        self.entry_valor = tk.Entry(root)

        self.label_fecha = tk.Label(root, text="Fecha:")
        self.entry_fecha = tk.Entry(root)

        self.btn_guardar = tk.Button(root, text="Guardar", command=self.guardar)
        self.btn_consultar = tk.Button(root, text="Consultar Todos", command=self.consultar_todos)

        # Organizar los elementos en la interfaz
        self.label_elemento.grid(row=0, column=0)
        self.entry_elemento.grid(row=0, column=1)

        self.label_valor.grid(row=1, column=0)
        self.entry_valor.grid(row=1, column=1)

        self.label_fecha.grid(row=2, column=0)
        self.entry_fecha.grid(row=2, column=1)

        self.btn_guardar.grid(row=3, column=0, columnspan=2, pady=10)
        self.btn_consultar.grid(row=4, column=0, columnspan=2, pady=10)

    def guardar(self):
        elemento = self.entry_elemento.get()
        valor = int(self.entry_valor.get())
        fecha = self.entry_fecha.get()

        ingreso = OtrosIngresos(elemento, valor, fecha)
        ingreso.guardar()

    def consultar_todos(self):
        OtrosIngresos.consultar_todos()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()