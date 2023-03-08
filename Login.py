from tkinter import messagebox

class Login:
    
    def __init__(self,contra,correo):
        self.__correo = correo
        self.__contra = contra
    
    def login(self,correo,contra):
        if correo == self.__correo and contra == self.__contra:
            messagebox.showinfo("Exito", "Bienvenido")
        elif correo != self.__correo or contra != self.__contra:
            messagebox.showerror("Error","Datos incorrectos")
        elif correo == "" and contra == "":
            messagebox.showwarning("Advertencia","Sin datos que validar")