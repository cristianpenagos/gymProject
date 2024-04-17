import tkinter as tk

class UserGui:
    def __init__(self, root):
        self.iconUser = tk.PhotoImage(file='asets/iconUser.png')

        self.root = root
        self.root.title('BODY FIT')
        self.root.geometry('1300x700')

        self.boton = tk.Button(root, image=self.iconUser, command=lambda: print("Botón clickeado"))
        self.boton.pack()

if __name__ == "__main__":
    root = tk.Tk()
    usergui = UserGui(root)
    root.mainloop()