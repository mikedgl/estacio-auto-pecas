# views.py
import tkinter as tk
from functools import partial


class MainView:
    def __init__(self, root):
        self.root = root
        self.create_navbar()
        self.create_form_section()

    def create_navbar(self):
        bg_color = "#103a63"
        color = "#fff"
        font_button = ("Arial", 14, "bold")

        nav_bar = tk.Frame(self.root, bg=bg_color, height=50, padx=20, pady=20)
        nav_bar.pack(fill=tk.X)

        logo = tk.Label(nav_bar, text="Estácio Auto Peças LTDA", bg=bg_color, fg=color, font=("Arial", 22, "bold"))
        logo.pack(side=tk.LEFT)

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

    def create_form_section(self):
        form_section = tk.Frame(self.root, pady=10)
        form_section.pack(padx=20, pady=10, fill=tk.X)

        title = tk.Label(form_section, text="Gerir Fornecedores", font=("Arial", 18, "bold"), fg="#103a63")
        title.grid(row=0, column=0, padx=10, pady=(0, 10), sticky="w")

        placeholders = ["Razão Social", "CNPJ", "Nome do Representante Legal", "CPF do Representante Legal",
                        "Celular", "E-mail", "Endereço Completo"]
        self.entries = []

        for i, placeholder in enumerate(placeholders):
            row = (i // 4) + 1
            col = i % 4

            entry = tk.Entry(form_section, font=("Arial", 12))
            entry.insert(0, placeholder)
            entry.bind("<FocusIn>", partial(self.clear_placeholder, entry, placeholder))
            entry.bind("<FocusOut>", partial(self.restore_placeholder, entry, placeholder))
            entry.grid(row=row, column=col, padx=10, pady=5, sticky="ew")

            self.entries.append(entry)

        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.X, padx=20, pady=(5, 10))

        save_button = tk.Button(button_frame, text="Salvar", font=("Arial", 12), bg="#103a63", fg="#fff",
                                command=self.save_action, cursor='hand2', width=20,
                                activebackground="#0d2e47", activeforeground="#fff")
        save_button.pack(side=tk.RIGHT, padx=5)

        cancel_button = tk.Button(button_frame, text="Cancelar", font=("Arial", 12), bg="#4a4a4a", fg="#fff",
                                  command=self.cancel_action, cursor='hand2', width=20,
                                  activebackground="#6c6c6c", activeforeground="#fff")
        cancel_button.pack(side=tk.RIGHT, padx=5)

        for col in range(4):
            form_section.grid_columnconfigure(col, weight=1, uniform="equal")

    def clear_placeholder(self, entry, placeholder, event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)

    def restore_placeholder(self, entry, placeholder, event):
        if not entry.get():
            entry.insert(0, placeholder)

    def home_action(self):
        print("Peças")

    def fornecedores_action(self):
        print("Fornecedores")

    def fabricantes_action(self):
        print("Fabricantes")

    def veiculos_action(self):
        print("Veículos")

    def save_action(self):
        print("Dados salvos!")

    def cancel_action(self):
        print("Ação cancelada!")
