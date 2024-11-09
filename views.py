# views.py
import tkinter as tk


class MainView:
    def __init__(self, root):
        self.root = root
        self.create_navbar()
        self.create_main_content()

    def create_navbar(self):
        bg_color = "#05265c"
        color = "#fff"
        font_button = ("Arial", 14, "bold")

        nav_bar = tk.Frame(self.root, bg=bg_color, height=50)
        nav_bar.pack(fill=tk.X)

        logo = tk.Label(nav_bar, text="Estácio Auto Peças LTDA", bg=bg_color, fg=color, font=("Arial", 22, "bold"))
        logo.pack(side=tk.LEFT, padx=20, pady=20)

        links_frame = tk.Frame(nav_bar, bg=bg_color)
        links_frame.pack(side=tk.RIGHT)

        self.create_nav_button(links_frame, "Peças", self.home_action, bg_color, color, font_button)
        self.create_nav_button(links_frame, "Fornecedores", self.fornecedores_action, bg_color, color, font_button)
        self.create_nav_button(links_frame, "Fabricantes", self.fabricantes_action, bg_color, color, font_button)
        self.create_nav_button(links_frame, "Veículos", self.veiculos_action, bg_color, color, font_button)

    def create_nav_button(self, parent, text, command, bg, fg, font):
        button = tk.Button(parent, text=text, bg=bg, fg=fg, relief=tk.FLAT, font=font, cursor="hand2",
                           activebackground=bg, activeforeground=fg, command=command)
        button.pack(side=tk.LEFT, padx=10)

    def create_main_content(self):
        main_content = tk.Frame(self.root)
        main_content.pack(fill=tk.BOTH, expand=True)
        label = tk.Label(main_content, text="Bem-vindo ao Projeto Tkinter!", font=("Arial", 16))
        label.pack(pady=20)

    def home_action(self):
        print("Peças")

    def fornecedores_action(self):
        print("Fornecedores")

    def fabricantes_action(self):
        print("Fabricantes")

    def veiculos_action(self):
        print("Veículos")
