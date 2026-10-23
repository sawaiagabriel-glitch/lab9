import tkinter as tk

from model.banco_dados import BancoDados
from view.conta_view import ContaView
from controller.conta_controller import ContaController


root = tk.Tk()

banco = BancoDados()
view = ContaView(root)

controller = ContaController(banco, view)

root.mainloop()