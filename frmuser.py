import tkinter as tk
import tkinter.messagebox as msg
import tkinter.font as tkFont
from dal.db import Db
import bll.usuarios as user

class App:
    def __init__(self, root):
        #setting title
        root.title("Usuario")
        #setting window size
        width=344
        height=136
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_76=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_76["font"] = ft
        GLabel_76["fg"] = "#333333"
        GLabel_76["justify"] = "center"
        GLabel_76["text"] = "Usuario:"
        GLabel_76.place(x=50,y=10,width=70,height=25)

        GButton_513=tk.Button(root)
        GButton_513["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_513["font"] = ft
        GButton_513["fg"] = "#000000"
        GButton_513["justify"] = "center"
        GButton_513["text"] = "Aceptar"
        GButton_513.place(x=180,y=90,width=70,height=25)
        GButton_513["command"] = self.GButton_513_command

        GLineEdit_95=tk.Entry(root, name="txtUsuario")
        GLineEdit_95["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_95["font"] = ft
        GLineEdit_95["fg"] = "#333333"
        GLineEdit_95["justify"] = "center"
        GLineEdit_95["text"] = ""
        GLineEdit_95.place(x=130,y=10,width=200,height=25)

        GLabel_106=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_106["font"] = ft
        GLabel_106["fg"] = "#333333"
        GLabel_106["justify"] = "center"
        GLabel_106["text"] = "Correo electrónico:"
        GLabel_106.place(x=0,y=50,width=120,height=25)

        GLineEdit_358=tk.Entry(root, name="txtEmail")
        GLineEdit_358["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_358["font"] = ft
        GLineEdit_358["fg"] = "#333333"
        GLineEdit_358["justify"] = "center"
        GLineEdit_358["text"] = ""
        GLineEdit_358.place(x=130,y=50,width=200,height=25)

        GButton_132=tk.Button(root)
        GButton_132["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_132["font"] = ft
        GButton_132["fg"] = "#000000"
        GButton_132["justify"] = "center"
        GButton_132["text"] = "Cancelar"
        GButton_132.place(x=260,y=90,width=70,height=25)
        GButton_132["command"] = self.GButton_132_command

    def GButton_513_command(self):
        try:
            txtUsuario = root.nametowidget("txtUsuario")
            user_name = txtUsuario.get()            

            txtEmail = root.nametowidget("txtEmail")
            email = txtEmail.get()
        
            user.agregar(user_name, email)
            msg.showinfo(title="Super", message="Registro agregado!!!!!!")
            # cerrar ventana
        except Exception as ex:
            msg.showerror(title="Super", message=str(ex))

    def GButton_132_command(self):
        root.destroy()

if __name__ == "__main__":
    Db.crear()
    root = tk.Tk()
    app = App(root)
    root.mainloop()
