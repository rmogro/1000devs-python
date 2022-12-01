from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import bll.usuarios as user

class Users(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master        
        self.title("Listado de Usuarios")        
        width=800
        height=500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_464=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#333333"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "Usuarios:"
        GLabel_464.place(x=10,y=10,width=70,height=25)

        tv = ttk.Treeview(self, columns=("usuario", "apellido", "nombre", "email", "rol"))
        tv.column("#0", width=78)
        tv.column("usuario", width=100, anchor=CENTER)
        tv.column("apellido", width=150, anchor=CENTER)
        tv.column("nombre", width=150, anchor=CENTER)
        tv.column("email", width=150, anchor=CENTER)
        tv.column("rol", width=120, anchor=CENTER)

        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("usuario", text="Usuario", anchor=CENTER)
        tv.heading("apellido", text="Apellido", anchor=CENTER)
        tv.heading("nombre", text="Nombre", anchor=CENTER)
        tv.heading("email", text="Correo electrónico", anchor=CENTER)
        tv.heading("rol", text="Rol", anchor=CENTER)        
        
        usuarios = user.listar()
        for usuario in usuarios:
            tv.insert("", END, text=usuario[0], values=(usuario[6], usuario[1], usuario[2], usuario[5], usuario[8]))        
        tv.place(x=10,y=40,width=750,height=300)