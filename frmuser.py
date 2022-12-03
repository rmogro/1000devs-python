import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.usuarios as user
import bll.roles as rol

class User(tk.Toplevel):
    def __init__(self, master=None, isAdmin = False, user_id = None):
        super().__init__(master)
        self.master = master        
        self.title("Registro de cuenta")        
        width=443
        height=423
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_243=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_243["font"] = ft
        GLabel_243["fg"] = "#333333"
        GLabel_243["anchor"] = "e"
        GLabel_243["text"] = "Apellido:"
        GLabel_243.place(x=10,y=10,width=124,height=30)

        GLineEdit_871=tk.Entry(self, name="txtApellido")
        GLineEdit_871["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_871["font"] = ft
        GLineEdit_871["fg"] = "#333333"
        GLineEdit_871["justify"] = "left"
        GLineEdit_871["text"] = ""
        GLineEdit_871.place(x=140,y=10,width=284,height=30)

        GLabel_599=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_599["font"] = ft
        GLabel_599["fg"] = "#333333"
        GLabel_599["anchor"] = "e"
        GLabel_599["text"] = "Nombre:"
        GLabel_599.place(x=10,y=50,width=122,height=30)

        GLineEdit_911=tk.Entry(self, name="txtNombre")
        GLineEdit_911["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_911["font"] = ft
        GLineEdit_911["fg"] = "#333333"
        GLineEdit_911["justify"] = "left"
        GLineEdit_911["text"] = ""
        GLineEdit_911.place(x=140,y=50,width=285,height=30)        

        GLabel_600=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_600["font"] = ft
        GLabel_600["fg"] = "#333333"
        GLabel_600["anchor"] = "e"
        GLabel_600["text"] = "Fecha Nacimiento:"
        GLabel_600.place(x=10,y=90,width=123,height=30)

        GLineEdit_208=tk.Entry(self, name="txtFechaNac")
        GLineEdit_208["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_208["font"] = ft
        GLineEdit_208["fg"] = "#333333"
        GLineEdit_208["justify"] = "left"
        GLineEdit_208["text"] = ""
        GLineEdit_208.place(x=140,y=90,width=94,height=30)

        GLabel_737=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_737["font"] = ft
        GLabel_737["fg"] = "#333333"
        GLabel_737["anchor"] = "e"
        GLabel_737["text"] = "DNI:"
        GLabel_737.place(x=10,y=130,width=121,height=30)

        GLineEdit_234=tk.Entry(self, name="txtDni")
        GLineEdit_234["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_234["font"] = ft
        GLineEdit_234["fg"] = "#333333"
        GLineEdit_234["justify"] = "left"
        GLineEdit_234["text"] = ""
        GLineEdit_234.place(x=140,y=130,width=133,height=30)

        GLabel_454=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_454["font"] = ft
        GLabel_454["fg"] = "#333333"
        GLabel_454["anchor"] = "e"
        GLabel_454["text"] = "Correo electrónico:"
        GLabel_454.place(x=10,y=170,width=124,height=30)

        GLineEdit_384=tk.Entry(self, name="txtEmail")
        GLineEdit_384["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_384["font"] = ft
        GLineEdit_384["fg"] = "#333333"
        GLineEdit_384["justify"] = "left"
        GLineEdit_384["text"] = ""
        GLineEdit_384.place(x=140,y=170,width=285,height=30)

        GLabel_616=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_616["font"] = ft
        GLabel_616["fg"] = "#333333"
        GLabel_616["anchor"] = "e"
        GLabel_616["text"] = "Usuario:"
        GLabel_616.place(x=10,y=210,width=123,height=30)

        GLineEdit_481=tk.Entry(self, name="txtUsuario")
        GLineEdit_481["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_481["font"] = ft
        GLineEdit_481["fg"] = "#333333"
        GLineEdit_481["justify"] = "left"
        GLineEdit_481["text"] = ""
        GLineEdit_481.place(x=140,y=210,width=286,height=30)

        GLabel_61=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_61["font"] = ft
        GLabel_61["fg"] = "#333333"
        GLabel_61["anchor"] = "e"
        GLabel_61["text"] = "Contraseña:"
        GLabel_61.place(x=10,y=250,width=124,height=30)

        GLineEdit_366=tk.Entry(self, show="*", name="txtContrasenia")
        GLineEdit_366["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_366["font"] = ft
        GLineEdit_366["fg"] = "#333333"
        GLineEdit_366["justify"] = "left"
        GLineEdit_366["text"] = ""
        GLineEdit_366.place(x=140,y=250,width=286,height=30)        

        GLabel_524=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_524["font"] = ft
        GLabel_524["fg"] = "#333333"
        GLabel_524["anchor"] = "e"
        GLabel_524["text"] = "Confirme contraseña:"
        GLabel_524.place(x=10,y=290,width=125,height=30)

        GLineEdit_126=tk.Entry(self, show="*", name="txtConfirmacion")
        GLineEdit_126["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_126["font"] = ft
        GLineEdit_126["fg"] = "#333333"
        GLineEdit_126["justify"] = "left"
        GLineEdit_126["text"] = ""
        GLineEdit_126.place(x=140,y=290,width=285,height=30)        

        GLabel_975=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_975["font"] = ft
        GLabel_975["fg"] = "#333333"
        GLabel_975["anchor"] = "e"
        GLabel_975["text"] = "Rol:"
        GLabel_975.place(x=10,y=330,width=122,height=30)
        
        roles = dict(rol.listar())
        if isAdmin:
            cb_roles = ttk.Combobox(self, state="readonly", values=list(roles.values()), name="cbRoles")
        else:
            cb_roles = ttk.Combobox(self, state="disabled", values=list(roles.values()), name="cbRoles")
            cb_roles.set(roles[4])
        cb_roles.place(x=140,y=330,width=283,height=30)

        GButton_825=tk.Button(self)
        GButton_825["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_825["font"] = ft
        GButton_825["fg"] = "#000000"
        GButton_825["justify"] = "center"
        GButton_825["text"] = "Aceptar"
        GButton_825.place(x=270,y=370,width=70,height=25)
        GButton_825["command"] = self.GButton_825_command
        
        GButton_341=tk.Button(self)
        GButton_341["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_341["font"] = ft
        GButton_341["fg"] = "#000000"
        GButton_341["justify"] = "center"
        GButton_341["text"] = "Cancelar"
        GButton_341.place(x=350,y=370,width=70,height=25)
        GButton_341["command"] = self.GButton_341_command        

    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def GButton_341_command(self):
        self.destroy()

    def GButton_825_command(self):
        try:            
            apellido = self.get_value("txtApellido")
            nombre = self.get_value("txtNombre")            
            fecha_nac = self.get_value("txtFechaNac")            
            dni = self.get_value("txtDni")
            email = self.get_value("txtEmail")            
            usuario = self.get_value("txtUsuario")

            contrasenia = self.get_value("txtContrasenia")            
            confirmacion = self.get_value("txtConfirmacion")
            rol_id = self.get_index("cbRoles")

            # TODO validar los datos antes de ingresar
            if not user.existe(usuario):
                user.agregar(apellido, nombre, fecha_nac, dni, email, usuario, contrasenia, rol_id)
                tkMsgBox.showinfo(self.master.title(), "Registro agregado!!!!!!")                
                try:
                    self.master.refrescar()
                except Exception as ex:
                    print(ex)
                self.destroy()                
            else:
                tkMsgBox.showwarning(self.master.title(), "Usuario existente en nuestros registros")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))