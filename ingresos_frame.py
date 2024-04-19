import tkinter as tk
from tkinter import ttk
# from mensualidad import Mensualidad
from tkinter import messagebox


class OtrosIngresosFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, width=1180, height=700, background="lightblue")
        self.pack_propagate(False)

        # Interface elements
