import tkinter as tk

def mostrar_texto():
    texto_ingresado = entrada_texto.get()
    etiqueta_resultado.config(text=texto_ingresado)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Tkinter")

# Crear una entrada de texto
entrada_texto = tk.Entry(ventana, width=30)
entrada_texto.pack(pady=10)

# Crear un botón que al presionarse llame a la función mostrar_texto
boton_mostrar = tk.Button(ventana, text="Mostrar Texto", command=mostrar_texto)
boton_mostrar.pack()

# Crear una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

# Iniciar el bucle principal de Tkinter
ventana.mainloop()