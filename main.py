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

