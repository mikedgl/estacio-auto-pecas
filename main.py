# main.py
import tkinter as tk
from views import MainView

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Estácio Auto Peças LTDA")
        self.root.geometry("1280x720")
        self.main_view = MainView(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()