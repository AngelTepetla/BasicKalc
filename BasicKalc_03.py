import Tkinter  #Llamar librerias
import tkMessageBox

from os import system

calcu = Tkinter.Tk() # Creacion del GUI
calcu.title("    Calculadora - mB")
calcu.geometry("400x280+400+200") # Dimensiones (ancho, alto, posicion x, posicion y)
calcu.configure(bg="#ffffff")

operacion = 0
numero_uno = 0
numero_dos = 0
tipo = 0
resultado = 0
display = "0"

i = 0
j = 0

def habla(texto):  # Rutina 1
    texto = str(texto)
    #system('espeak -v es+m3 -p40 -s190 " "' + texto)
    system('espeak -v es+f2 -p50 -s195 " "' + texto)


def habla_num(numero):  # Rutina 1

    global numero_uno
    global numero_dos

    if numero_uno == 0:
        numero_uno = ""

    if numero_dos == 0:
        numero_dos = ""

    if operacion == 0:
        numero_uno = str(numero_uno) + str(numero)
        numer.configure(text = numero_uno)
        #system('espeak -v es+f3 -p40 -s190 " "' + numero_uno)

    elif operacion == 1:
        numero_dos = str(numero_dos) + str(numero)
        numer.configure(text = numero_dos)
        #system('espeak -v es+f3 -p40 -s190 " "' + numero_dos)

    numero = str(numero)

    if numero == ".":
        numero = "punto"

    #system('espeak -v es+m3 -p40 -s190 " "' + texto)

    #system('espeak -v es+f3 -p40 -s190 " "' + numero)


def Yo():  # Rutina 2
    numer.configure(text = "by devOne")
    tkMessageBox.showinfo( "developed by", "Angel Tepetla  \n    mB - 2019")

def she():  # Rutina 33
    numer.configure(text = "Ella + Yo")

def tu():  # Rutina 33
    numer.configure(text = "Tu + Yo")


def Sumy():  # Rutina 2

    habla(numero_uno)
    habla("mas")

    global operacion
    operacion = 1

    global tipo
    tipo = 1


def Resy(): # Rutina 2

    habla(numero_uno)
    habla("menos")

    global operacion
    operacion = 1

    global tipo
    tipo = 2


def Multy():

    habla(numero_uno)
    habla("Por")

    global operacion
    operacion = 1

    global tipo
    tipo = 3


def Divy():

    habla(numero_uno)
    habla("entre")

    global operacion
    operacion = 1

    global tipo
    tipo = 4


def calcula(): # Rutina final

    global tipo
    global numero_uno
    global numero_dos

    #habla(numero_uno)
    habla(numero_dos)
    habla("=a")

    if tipo == 1:
        resultado = float(numero_uno) + float(numero_dos)
        resultado = round(resultado, 2)
    elif tipo == 2:
        resultado = float(numero_uno) - float(numero_dos)
        resultado = round(resultado, 2)
    elif tipo == 3:
        resultado = float(numero_uno) * float(numero_dos)
        resultado = round(resultado, 2)
    elif tipo == 4:
        resultado = float(numero_uno) / float(numero_dos)
        resultado = round(resultado, 2)
    else:
        resultado = "Error"

    global operacion
    operacion = 0

    numero_uno = ""
    numero_dos = ""

    numer.configure(text = resultado)

    tipo = 0
    habla(resultado)


def limpia():
    habla("limpio")

    global operacion
    global numero_uno
    global numero_dos
    global tipo

    operacion = 0
    numero_uno = 0
    numero_dos = 0
    tipo = 0

    numer.configure(text = "0")



A = Tkinter.Button(calcu, text ="/", width=2, bg="#dfe1e5", highlightbackground="#ffffff", highlightthickness="3", activebackground="#d7d9dd", fg="#000000", font=("Open Sans", 15), command = Divy)
B = Tkinter.Button(calcu, text ="*", width=2, bg="#dfe1e5", highlightbackground="#ffffff", highlightthickness="3", activebackground="#d7d9dd", fg="#000000", font=("Open Sans", 15), command = Multy)
C = Tkinter.Button(calcu, text ="-", width=2, bg="#dfe1e5", highlightbackground="#ffffff", highlightthickness="3", activebackground="#d7d9dd", fg="#000000", font=("Open Sans", 15), command = Resy)
D = Tkinter.Button(calcu, text ="+", width=2, bg="#dfe1e5", highlightbackground="#ffffff", highlightthickness="3", activebackground="#d7d9dd", fg="#000000", font=("Open Sans", 15), command = Sumy)

E = Tkinter.Button(calcu, text ="=", width=7, bg="#4285f4", highlightbackground="#ffffff", highlightthickness="3", activebackground="#4d8bf1", fg="#f1f3f4", activeforeground="#ffffff", font=("Open Sans", 15), command = calcula) # =
F = Tkinter.Button(calcu, text =".", width=7, bg="#f1f3f4", highlightbackground="#ffffff", highlightthickness="3", fg="#000000", font=("Open Sans", 15), command= lambda: habla_num(".")) # =
G = Tkinter.Button(calcu, text ="AC", width=7, bg="#f1f3f4", highlightbackground="#ffffff", highlightthickness="3", activebackground="#4d8bf1", fg="#000000", activeforeground="#ffffff", font=("Open Sans", 15), command = limpia) # =

#e8eaeb
numral1 = Tkinter.Button(calcu, text ="7", width=2, bg="#f1f3f4", highlightbackground="#ffffff", highlightthickness="3", activebackground="#e8eaeb", fg="#000000", font=("Open Sans", 15), command= lambda: habla_num(7))
numral2 = Tkinter.Button(calcu, text ="8", width=2, bg="#f1f3f4", highlightbackground="#ffffff", highlightthickness="3", activebackground="#e8eaeb", fg="#000000", font=("Open Sans", 15), command= lambda: habla_num(8))
numral3 = Tkinter.Button(calcu, text ="9", width=2, bg="#f1f3f4", highlightbackground="#ffffff", highlightthickness="3", activebackground="#e8eaeb", fg="#000000", font=("Open Sans", 15), command= lambda: habla_num(9))
numral4 = Tkinter.Button(calcu, text ="4", width=2, bg="#f1f3f4", highlightbackground="#ffffff", highlightthickness="3", activebackground="#e8eaeb", fg="#000000", font=("Open Sans", 15), command= lambda: habla_num(4))
numral5 = Tkinter.Button(calcu, text ="5", width=2, bg="#f1f3f4", highlightbackground="#ffffff", highlightthickness="3", activebackground="#e8eaeb", fg="#000000", font=("Open Sans", 15), command= lambda: habla_num(5))
numral6 = Tkinter.Button(calcu, text ="6", width=2, bg="#f1f3f4", highlightbackground="#ffffff", highlightthickness="3", activebackground="#e8eaeb", fg="#000000", font=("Open Sans", 15), command= lambda: habla_num(6))
numral7 = Tkinter.Button(calcu, text ="1", width=2, bg="#f1f3f4", highlightbackground="#ffffff", highlightthickness="3", activebackground="#e8eaeb", fg="#000000", font=("Open Sans", 15), command= lambda: habla_num(1))
numral8 = Tkinter.Button(calcu, text ="2", width=2, bg="#f1f3f4", highlightbackground="#ffffff", highlightthickness="3", activebackground="#e8eaeb", fg="#000000", font=("Open Sans", 15), command= lambda: habla_num(2))
numral9 = Tkinter.Button(calcu, text ="3", width=2, bg="#f1f3f4", highlightbackground="#ffffff", highlightthickness="3", activebackground="#e8eaeb", fg="#000000", font=("Open Sans", 15), command= lambda: habla_num(3))
numral0 = Tkinter.Button(calcu, text ="0", width=2, bg="#f1f3f4", highlightbackground="#ffffff", highlightthickness="3", activebackground="#e8eaeb", fg="#000000", font=("Open Sans", 15), command= lambda: habla_num(0))

espacio0 = Tkinter.Button(calcu, text ="", width=1, bd=0, command=she)
espacio2 = Tkinter.Button(calcu, text ="", width=1, bd=0, command=tu)
espacio3 = Tkinter.Button(calcu, text ="", width=1, bd=0, command=Yo)

numer = Tkinter.Label(calcu, text=display, font=("Arial Bold", 25))
numer.grid(column=2, row=1, columnspan=5, sticky="e")
numer.configure(bg="#ffffff", highlightbackground="#ffffff", highlightthickness="3")

A.grid(column=6, row=4)
B.grid(column=5, row=4)
C.grid(column=6, row=5)
D.grid(column=5, row=5)
E.grid(column=5, row=6, columnspan=2, sticky="e") # =
F.grid(column=2, row=6, columnspan=2, sticky="w") # =
G.grid(column=5, row=3, columnspan=2, sticky="e") # =

numral1.grid(column=1, row=3)
numral2.grid(column=2, row=3)
numral3.grid(column=3, row=3)
numral4.grid(column=1, row=4)
numral5.grid(column=2, row=4)
numral6.grid(column=3, row=4)
numral7.grid(column=1, row=5)
numral8.grid(column=2, row=5)
numral9.grid(column=3, row=5)
numral0.grid(column=1, row=6)

espacio0.grid(column=0, row=2)
espacio2.grid(column=4, row=1)
espacio3.grid(column=0, row=0)

espacio0.configure(bg="#ffffff", highlightbackground="#ffffff", activebackground="#ffffff")
espacio2.configure(bg="#ffffff", highlightbackground="#ffffff", activebackground="#ffffff")
espacio3.configure(bg="#ffffff", highlightbackground="#ffffff", activebackground="#ffffff")


calcu.mainloop()  #Loop principal del TKinter!
