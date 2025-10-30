import csv
import os
from datetime import datetime


DADOS_DIR = "dados"
ARQ_PRODUTOS = os.path.join(DADOS_DIR, "produtos.csv")
ARQ_LOG = os.path.join(DADOS_DIR, "log.txt")
CSV_HEADERS = ["id","nome","categoria","tamanho","preco","quantidade","descricao"]


def garantir_arquivos():
    """Garante existência da pasta e arquivos com cabeçalho."""
    os.makedirs(DADOS_DIR, exist_ok=True)
    if not os.path.exists(ARQ_PRODUTOS):
        try:
            with open(ARQ_PRODUTOS, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
                writer.writeheader()
        except Exception as e:
            print(f"Erro ao criar arquivo de produtos: {e}")
    if not os.path.exists(ARQ_LOG):
        try:
            open(ARQ_LOG, "a", encoding="utf-8").close()
        except Exception as e:
            print(f"Erro ao criar arquivo de log: ")

