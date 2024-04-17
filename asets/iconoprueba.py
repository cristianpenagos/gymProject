import tkinter as tk

# Creamos la ventana principal
root = tk.Tk()

# Cargamos la imagen
icono = tk.PhotoImage(file="asets/iconUser.png")

# Creamos un botón y le asignamos el icono
boton = tk.Button(root, image=icono, text="Gestión \nUsuarios", font=("Times new roman", 14), command=lambda: print("Haz clic en el botón"))
boton.place(x=10, y=10, width=100, height=100)

# Iniciamos el bucle de eventos
root.mainloop()