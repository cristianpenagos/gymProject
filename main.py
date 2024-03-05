import tkinter as tk
from gui import UserGui
from vista2 import display2  # Asegúrate de importar la función desde el módulo correcto

if __name__ == "__main__":
    root = tk.Tk()
    usergui = UserGui(root)

    # Oculta temporalmente la ventana principal
    root.withdraw()

    # Muestra la segunda ventana (display2)
    display2('Samuel Alvarez', "05/12/2023", "05/01/2024", "07", "03")

    # Vuelve a mostrar la ventana principal
    root.deiconify()

    # Muestra la primera ventana (UserGui)
    usergui.show_user_frame()

    root.mainloop()