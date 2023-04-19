from tkinter import *

#creacion ventana principal
root = Tk()

#titulo ventana
root.title("Curso de Tkinter")

#tamaño ventana
root.geometry("800x600+300+200")

#creacion etiqueta
mensaje1=Label(root, text="Mi primera linea").grid(row=0, column=0)
mensaje2=Label(root, text="Esta es la segunda linea").grid(row=1, column=1)

#muestra las etiquetas



#bucle ejecucion
root.mainloop()