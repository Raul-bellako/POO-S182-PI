from tkinter import Tk, Toplevel, Label, Button,Frame
from Login import *
from SignUp import *

#Ventana
win1=Tk()
win1.title("BIENVENIDO")
win1.geometry("640x480")

#Funciones
def open_signup():
    w2 = Toplevel(win1)
    w2.title("REGISTRARSE")
    w2.geometry("640x480")
    s3w2=Frame(w2)
    s3w2.pack(expand=True,fill='both')
    # Agrega widgets a la ventana_1 aquí
    def killwin2():
        w2.destroy()
        win1.deiconify()
    btnClose = Button(s3w2,text="Regresar",command=killwin2)
    btnClose.pack()

def open_login():
    w3 =  Toplevel(win1)
    w3.title("INICIO DE SESION")
    w3.geometry("640x480")
    s3w3=Frame(w3)
    s3w3.pack(expand=True,fill='both')
    # Agrega widgets a la ventana_2 aquí
    def killwin3():
        w3.destroy()
        win1.deiconify()
    btnClose = Button(s3w3,text="Regresar",command=killwin3)
    btnClose.pack()

#Etiquetas
lbWelcome = Label(win1,text="Bienvenido\n",font=("Century Gothic",36))
lbWelcome.pack()

#Botones
btnSignUp = Button(win1,text="Registrarse",bg="white",command=open_signup)
btnSignUp.config(font=("Century Gothic",16))
btnSignUp.pack()

btnLogin = Button(win1,text="Iniciar Sesion",bg="white",command=open_login)
btnLogin.config(font=("Century Gothic",16))
btnLogin.pack()

win1.mainloop()
