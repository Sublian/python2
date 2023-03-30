from tkinter import *
from PIL import Image, ImageTk
import time
import locale
locale.setlocale(locale.LC_TIME, "es")


def configure(event):
    w, h = event.width, event.height
    hancho = ((w/6)+20)
    fancho = (w/15)
    Hancho = int(round(hancho))
    Fancho = int(round(fancho))
    hora.config(font=(("times", Hancho, "bold")))
    fecha.config(font=(("times", Fancho, "bold")))


def times():
    current_time = time.strftime("%I:%M:%S")
    hora.config(text=current_time)
    hora.after(1000, times)


root = Tk()
root.resizable(True, True)
root.configure(bg="grey")
root.title("Reloj Digital Personal")
root.grid_columnconfigure(1, weight=1)

img = Image.open("1.png")
img = img.resize((300, 260), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)
logo = Label(root, image=img, bg="grey")
logo.image = img
logo.grid(row=0, column=1, pady=2, padx=2, sticky=N+S+E+W)

hora = Label(root, bg="grey", fg="yellow", text="00:00:00")
hora.grid(row=1, column=1, pady=2, padx=2, sticky=N+S+E+W)
hora.bind("<Configure>", configure)
fecha = Label(root, bg="black", fg="yellow",
              text=""+time.strftime("%A %d de %B"))
fecha.grid(row=2, column=1, pady=2, padx=2, sticky=N+S+E+W)

times()
root.mainloop()
