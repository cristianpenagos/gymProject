import tkinter as tk



def display2(name, dateInit, dateFinish, numDaysLeft, numLocker):
    # Create and config this window

    root2 = tk.Tk()  # segunda pantalla
    root2.config(bg="Black")
    root2.geometry("1360x768")
    root2.title("BodyFit Julian Castillo")

    # icon
    # icono16 = tk.PhotoImage(file="icon16.png")
    # icono32 = tk.PhotoImage(file="icon32.png")
    # icono64 = tk.PhotoImage(file="icon64.png")
    # root2.iconphoto(False, icono16, icono32)

    root2.iconbitmap("icon.ico")

    # welcome label

    welLabel = tk.Label(root2, text='Bienvenid@', font='Arial 30')
    welLabel.config(bg="black", fg="white")
    welLabel.place(x=530, y=10)

    # date Labels

    startLabel = tk.Label(root2, text='Fecha inicio', font='Arial 30')
    startLabel.config(bg="black", fg="white")
    startLabel.place(x=130, y=200)

    startDate = tk.Label(root2, text=dateInit, font='Arial 30')
    startDate.config(bg="black", fg="white")
    startDate.place(x=130, y=250)

    montPayLabel = tk.Label(root2, text='Vencimineto Mes', font='Arial 30')
    montPayLabel.config(bg="black", fg="white")
    montPayLabel.place(x=500, y=200)

    montPayDate = tk.Label(root2, text=dateFinish, font='Arial 30')
    montPayDate.config(bg="black", fg="white")
    montPayDate.place(x=550, y=250)

    remainingDaysLabel = tk.Label(root2, text="Dias Restantes", font='Arial 30')
    remainingDaysLabel.config(bg="black", fg="white")
    remainingDaysLabel.place(x=915, y=200)

    remainingDaysDate = tk.Label(root2, text=numDaysLeft, font='Arial 30')
    remainingDaysDate.config(bg="black", fg="white")
    remainingDaysDate.place(x=915, y=250)

    lockerLabel = tk.Label(root2, text='Locker', font='Arial 40')
    lockerLabel.config(bg="black", fg="white")
    lockerLabel.place(x=150, y=310)

    lockerNum = tk.Label(root2, text=numLocker, font='arial 200') # #ff04b7
    lockerNum.config(bg="#ff04b7")
    lockerNum.place(x=90, y=370)

    remainingDaysBox = tk.Label(root2, text='Dias Restantes', font='Arial 40')
    remainingDaysBox.config(bg="black", fg="white")
    remainingDaysBox.place(x=875, y=310)

    remainingDaysBoxNum = tk.Label(root2, text=numDaysLeft, font='Arial 200') #  #28b7fe
    remainingDaysBoxNum.config(bg="#28b7fe")
    remainingDaysBoxNum.place(x=910, y=370)

    # Logo Label

    imagen = tk.PhotoImage(file="logo2.png")
    labelLogo = tk.Label(root2, image=imagen)
    labelLogo.config(width=300, height=300, bg='black')
    imagen.configure(width=300, height=300)
    labelLogo.place(x=500, y=350)

    # Name User Label
    nameUser = tk.Label(root2, text=name, font="Arial 40")
    nameUser.config(bg="black", fg="white")
    nameUser.place(x=450, y=80)

    root2.mainloop()


display2('Samuel Alvarez', "05/12/2023", "05/01/2024", "07", "03")