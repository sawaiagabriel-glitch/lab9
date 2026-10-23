from model.cliente import Cliente
from model.conta import Conta


class ContaController:
    def __init__(self, banco_dados, view):
        self.banco_dados = banco_dados
        self.view = view

        self.view.botao_criar.config(command=self.criar_conta)

    def criar_conta(self):
        nome, cpf, saldo = self.view.obter_dados()

        if not nome or not cpf or not saldo:
            self.view.exibir_erro("Preencha todos os campos.")
            return

        try:
            saldo = float(saldo)
        except ValueError:
            self.view.exibir_erro("O saldo deve ser um número.")
            return

        cliente = Cliente(nome, cpf)
        conta = Conta(cliente, saldo)

        self.banco_dados.salvar_conta(conta)

        self.view.exibir_conta(conta)