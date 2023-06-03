from tkinter import *

#ventana principal
root = Tk()

#titulo
root.title("Ejercicio")

#entrada de datos
Label(root, text="Nombre: ").grid(column=0, row=0)
entrada_nombre= Entry(root)
entrada_nombre.grid(column=1, row=0)

Label(root, text="Edad: ").grid(column=0, row=1)
entrada_edad= Entry(root)
entrada_edad.grid(column=1, row=1)

def pulsar_boton():
    nombre= entrada_nombre.get()
    edad= entrada_edad.get()
    Label(root, text= f"Mi nombre es: {nombre}. Tengo {edad} años"). grid(column=1, row=3)
    
#boton
Button(root, text="Enviar", command=pulsar_boton).grid(column=1, row=2)

root.mainloop()
