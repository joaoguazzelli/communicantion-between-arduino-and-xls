import tkinter as tk
from typing import List


class GUI:
    def __init__(self, root: tk.Tk, labels: List[List[tk.Label]]):
        self.root = root
        self.labels = labels


