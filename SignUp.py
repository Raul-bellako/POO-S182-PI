from tkinter import messagebox, Entry

class SignUp:
    
    def __init__(self):
        self.nombres = []
        self.correos = []
        self.contraseñas = []
    
    def registrar_usuario(self):
        nombre = Entry("Ingrese su nombre: ")
        correo = Entry("Ingrese su correo electrónico: ")
        contraseña = Entry("Ingrese su contraseña: ")
        
        self.nombres.append(nombre)
        self.correos.append(correo)
        self.contraseñas.append(contraseña)
        
        messagebox.showinfo("Exito","Registro existoso")