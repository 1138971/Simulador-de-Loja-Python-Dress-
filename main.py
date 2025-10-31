from funcoes import (
    garantir_arquivos, carregar_produtos, cadastrar_produto,
    listar_produtos, editar_produto, excluir_produto, log_action
)

import os
import sys
import time


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausa():
    input("\nPressione Enter para continuar...")

def menu_principal():
    garantir_arquivos()
    produtos = carregar_produtos()

    while True:
        limpar_tela()
        print("="*50)
        print("             Loja de Roupa Python Dress")
        print("="*50)
        print("1) Cadastrar produto")
        print("2) Listar produtos")
        print("3) Editar produto")
        print("4) Excluir produto")
        print("5) Ver contador de registros / Contagem por categoria")
        print("6) Ver log (últimas linhas)")
        print("0) Sair")
        print("-"*50)
