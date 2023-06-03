# ejercicio basico de tkinter
from tkinter import *

#creacion de la ventana principal
root = Tk()

#titulo de la vewntana
root.title("Curso de Tkinder de programacion facil")

#entrada de datos
entrada= Entry(root)
entrada.insert(0, "Escriba su nombre...")
entrada.bind("<Button-1>", lambda x: entrada.delete(0, END))
entrada.pack()

def pulsar_boton():
    nombre= entrada.get()
    Label(root, text= f"{nombre}").pack()

#boton
Button(root, text="Enviar", command= pulsar_boton).pack()

#bucle de ejecucion
root.mainloop()