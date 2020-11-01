from tkinter import *
from PIL import ImageTk, Image

root = Tk()

my_img = ImageTk.PhotoImage(Image.open("Cabecalho.jpg"))

my_label = Label(image=my_img)

my_label.pack()

root.mainloop()