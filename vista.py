import tkinter as tk
import vista2

root = tk.Tk()

root.config(bg="gray")


# Crea un botón
boton = tk.Button(root, text="Aceptar", width=10,
                  height=3, bg="gray", fg="blue")

# Coloca el botón en la ventana
boton.place(x=50, y=50)

# Inicia la ventana
root.geometry("800x600")

caja = tk.Entry(root, text="Nombre", width=200)
caja.place(x=15, y=0)

root.mainloop()
root2.mainloop()
