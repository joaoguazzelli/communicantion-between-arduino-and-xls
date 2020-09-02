import tkinter as tk


def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Eu tenho doutorado')
    root.config(padx=10, pady=10, background='#fff')
    root.resizable(False, False)
    return root


def make_result(root) -> tk.Label:
    label = tk.Label(root, text='Processando', anchor='e', justify='right', background='#fff')
    label.grid(row=0, column=0)
    return label

