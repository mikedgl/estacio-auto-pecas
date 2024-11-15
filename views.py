import tkinter as tk
import tkinter.messagebox as messagebox
from functools import partial
import database

class MainView:
    def __init__(self, root):
        database.create_table()
        self.root = root
        self.create_navbar()
        self.create_form_section()
        self.create_search_section()
        self.create_list_section()

        self.selected_fornecedor_id = None

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

            entry = tk.Entry(form_section, font=("Arial", 14), bg="#c9c9c9")
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

    def create_search_section(self):
        search_section = tk.Frame(self.root, pady=10)
        search_section.pack(padx=20, pady=10, fill=tk.X)

        self.razao_entry = tk.Entry(search_section, font=("Arial", 14), bg="#c9c9c9")
        self.razao_entry.insert(0, "Razão Social")
        self.razao_entry.bind("<FocusIn>", partial(self.clear_placeholder, self.razao_entry, "Razão Social"))
        self.razao_entry.bind("<FocusOut>", partial(self.restore_placeholder, self.razao_entry, "Razão Social"))
        self.razao_entry.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.cnpj_entry = tk.Entry(search_section, font=("Arial", 14), bg="#c9c9c9")
        self.cnpj_entry.insert(0, "CNPJ")
        self.cnpj_entry.bind("<FocusIn>", partial(self.clear_placeholder, self.cnpj_entry, "CNPJ"))
        self.cnpj_entry.bind("<FocusOut>", partial(self.restore_placeholder, self.cnpj_entry, "CNPJ"))
        self.cnpj_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        search_button = tk.Button(search_section, text="Pesquisar", font=("Arial", 12), bg="#103a63", fg="#fff",
                                  command=self.search_action, cursor="hand2", width=15,
                                  activebackground="#0d2e47", activeforeground="#fff")
        search_button.grid(row=0, column=2, padx=10, pady=5)

        search_section.grid_columnconfigure(0, weight=1)
        search_section.grid_columnconfigure(1, weight=1)


    def create_list_section(self):
        self.list_section = tk.Frame(self.root, pady=10)
        self.list_section.pack(padx=20, pady=10, fill=tk.X)

        header = tk.Frame(self.list_section)
        header.pack(fill=tk.X)

        tk.Label(header, text="Razão Social", font=("Arial", 12, "bold"), width=25, anchor="w").pack(side=tk.LEFT)
        tk.Label(header, text="CNPJ", font=("Arial", 12, "bold"), width=20, anchor="w").pack(side=tk.LEFT)
        tk.Label(header, text="Celular", font=("Arial", 12, "bold"), width=15, anchor="w").pack(side=tk.LEFT)
        tk.Label(header, text="E-mail", font=("Arial", 12, "bold"), width=30, anchor="w").pack(side=tk.LEFT)

        records = database.find_all_fornecedores()
        self.update_list_section(records)

    def clear_form_fields(self):
        placeholders = ["Razão Social", "CNPJ", "Nome do Representante Legal", "CPF do Representante Legal",
                        "Celular", "E-mail", "Endereço Completo"]

        for entry, placeholder in zip(self.entries, placeholders):
            entry.delete(0, tk.END)
            entry.insert(0, placeholder)

    def update_list_section(self, records):
        for widget in self.list_section.winfo_children():
            widget.destroy()

        header = tk.Frame(self.list_section)
        header.pack(fill=tk.X)

        tk.Label(header, text="Razão Social", font=("Arial", 12, "bold"), width=25, anchor="w").pack(side=tk.LEFT)
        tk.Label(header, text="CNPJ", font=("Arial", 12, "bold"), width=20, anchor="w").pack(side=tk.LEFT)
        tk.Label(header, text="Celular", font=("Arial", 12, "bold"), width=15, anchor="w").pack(side=tk.LEFT)
        tk.Label(header, text="E-mail", font=("Arial", 12, "bold"), width=30, anchor="w").pack(side=tk.LEFT)
        tk.Label(header, text="Ações", font=("Arial", 12, "bold"), width=10, anchor="w").pack(side=tk.LEFT)

        for record in records:
            record_frame = tk.Frame(self.list_section)
            record_frame.pack(fill=tk.X, pady=5)

            tk.Label(record_frame, text=record[1], font=("Arial", 12), width=25, anchor="w").pack(side=tk.LEFT)
            tk.Label(record_frame, text=record[2], font=("Arial", 12), width=20, anchor="w").pack(side=tk.LEFT)
            tk.Label(record_frame, text=record[3], font=("Arial", 12), width=15, anchor="w").pack(side=tk.LEFT)
            tk.Label(record_frame, text=record[4], font=("Arial", 12), width=30, anchor="w").pack(side=tk.LEFT)

            update_button = tk.Button(record_frame, text="Atualizar", font=("Arial", 12), bg="#103a63", fg="#fff",
                                      command=partial(self.update_action, record[0]), cursor="hand2", width=15,
                                      activebackground="#0d2e47", activeforeground="#fff")
            update_button.pack(side=tk.RIGHT, padx=10)

            delete_button = tk.Button(record_frame, text="Excluir", font=("Arial", 12), bg="#103a63", fg="#fff",
                                      command=partial(self.delete_action, record[0]), cursor="hand2", width=15,
                                      activebackground="#0d2e47", activeforeground="#fff")
            delete_button.pack(side=tk.RIGHT, padx=10)

            view_button = tk.Button(record_frame, text="Visualizar", font=("Arial", 12), bg="#103a63", fg="#fff",
                                    command=partial(self.view_action, record[0]), cursor="hand2", width=15,
                                    activebackground="#0d2e47", activeforeground="#fff")
            view_button.pack(side=tk.RIGHT, padx=10)

            separator = tk.Frame(self.list_section, height=1, bg="#c9c9c9")
            separator.pack(fill=tk.X, pady=5)

    def view_action(self, fornecedor_id):
        fornecedor = database.find_fornecedor_by_id(fornecedor_id)

        modal = tk.Toplevel(self.root)
        modal.title("Detalhes do Fornecedor")
        modal.geometry("400x300")

        labels = ["Razão Social", "CNPJ", "Representante Legal", "CPF do Representante Legal", "Celular", "E-mail",
                  "Endereço Completo"]
        for idx, (label_text, value) in enumerate(zip(labels, fornecedor[1:])):
            label = tk.Label(modal, text=f"{label_text}: {value}", font=("Arial", 12))
            label.pack(pady=5)

        close_button = tk.Button(modal, text="Fechar", font=("Arial", 12), command=modal.destroy)
        close_button.pack(pady=10)

    def delete_action(self, fornecedor_id):
        database.delete_fornecedor(fornecedor_id)
        records = database.find_all_fornecedores()
        self.update_list_section(records)

    def clear_placeholder(self, entry, placeholder, event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)

    def restore_placeholder(self, entry, placeholder, event):
        if not entry.get():
            entry.insert(0, placeholder)

    def search_action(self):
        razao = self.razao_entry.get()
        cnpj = self.cnpj_entry.get()

        if razao == "Razão Social" and cnpj == "CNPJ":
            records = database.find_all_fornecedores()
        else:
            records = database.find_all_fornecedores(razao, cnpj)

        self.update_list_section(records)

    def save_action(self):
        data = [entry.get() for entry in self.entries]

        for value in data:
            if value == "" or value == "Razão Social" or value == "CNPJ" or value == "Nome do Representante Legal" or value == "CPF do Representante Legal" or value == "Celular" or value == "E-mail" or value == "Endereço Completo":
                tk.messagebox.showwarning("Campos Obrigatórios", "Por favor, preencha todos os campos obrigatórios.")
                return

        cnpj = data[1]  # O CNPJ está no índice 1 da lista de dados
        if self.selected_fornecedor_id:
            existing_fornecedor = database.find_fornecedor_by_cnpj_except(cnpj, self.selected_fornecedor_id)
        else:
            existing_fornecedor = database.find_fornecedor_by_cnpj(cnpj)

        if existing_fornecedor:
            tk.messagebox.showwarning("CNPJ Já Cadastrado",
                                      "Já existe um fornecedor com esse CNPJ. O salvamento foi impedido.")
            return

        if self.selected_fornecedor_id:
            database.update_fornecedor(self.selected_fornecedor_id, data)
        else:
            database.insert_fornecedor(data)

        records = database.find_all_fornecedores()
        self.update_list_section(records)

        self.clear_form_fields()

        self.selected_fornecedor_id = None

    def update_action(self, fornecedor_id):
        fornecedor = database.find_fornecedor_by_id(fornecedor_id)

        for i, entry in enumerate(self.entries):
            entry.delete(0, tk.END)
            entry.insert(0, fornecedor[i + 1])

        self.selected_fornecedor_id = fornecedor_id

    def cancel_action(self):
        self.clear_form_fields()

    def clear_form_fields(self):
        placeholders = ["Razão Social", "CNPJ", "Nome do Representante Legal", "CPF do Representante Legal",
                        "Celular", "E-mail", "Endereço Completo"]

        for entry, placeholder in zip(self.entries, placeholders):
            entry.delete(0, tk.END)
            entry.insert(0, placeholder)

    def home_action(self):
        pass

    def fornecedores_action(self):
        pass

    def fabricantes_action(self):
        pass

    def veiculos_action(self):
        pass