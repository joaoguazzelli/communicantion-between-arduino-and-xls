import tkinter as tk

root = tk.Tk()
root.geometry("300x300")
count = 0
label1 = tk.Label(master=root, text=count)
label1.pack()


def increment():
    global count
    count += 1
    label1.configure(text=count)
    root.after(100, increment)


increment()
root.mainloop()
