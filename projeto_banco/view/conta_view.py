import tkinter as tk
from tkinter import messagebox


class ContaView:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento Bancário")
        self.root.geometry("350x300")

        tk.Label(root, text="Nome:").pack(pady=5)
        self.nome_entry = tk.Entry(root)
        self.nome_entry.pack()

        tk.Label(root, text="CPF:").pack(pady=5)
        self.cpf_entry = tk.Entry(root)
        self.cpf_entry.pack()

        tk.Label(root, text="Saldo Inicial:").pack(pady=5)
        self.saldo_entry = tk.Entry(root)
        self.saldo_entry.pack()

        self.botao_criar = tk.Button(root, text="Criar Conta")
        self.botao_criar.pack(pady=15)

        self.resultado = tk.Label(root, text="", justify="left")
        self.resultado.pack(pady=10)

    def obter_dados(self):
        nome = self.nome_entry.get()
        cpf = self.cpf_entry.get()
        saldo = self.saldo_entry.get()

        return nome, cpf, saldo

    def exibir_conta(self, conta):
        texto = (
            f"Conta criada com sucesso!\n\n"
            f"Nome: {conta.cliente.nome}\n"
            f"CPF: {conta.cliente.cpf}\n"
            f"Saldo: R$ {conta.saldo:.2f}"
        )

        self.resultado.config(text=texto)

    def exibir_erro(self, mensagem):
        messagebox.showerror("Erro", mensagem)