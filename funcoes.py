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
def agora_str():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def log_action(acao):
    """Grava no arquivo de log a ação com data/hora."""
    garantir_arquivos()
    linha = f"[{agora_str()}] {acao}\n"
    try:
        with open(ARQ_LOG, "a", encoding="utf-8") as f:
            f.write(linha)
    except Exception as e:
        print(f"Erro ao gravar log: ")


def carregar_produtos():
    """Lê produtos do CSV e retorna lista de dicionários."""
    garantir_arquivos()
    produtos = []
    try:
        with open(ARQ_PRODUTOS, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row and row.get("id"):
                    row["preco"] = float(row["preco"]) if row.get("preco") else 0.0
                    row["quantidade"] = int(row["quantidade"]) if row.get("quantidade") else 0
                    produtos.append(row)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Erro ao carregar produtos: ")
    return produtos


def salvar_produtos(produtos):
    """Salva lista de dicionários no CSV (sobrescreve)."""
    garantir_arquivos()
    try:
        with open(ARQ_PRODUTOS, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
            writer.writeheader()
            for p in produtos:
                line = {
                    "id": p["id"],
                    "nome": p["nome"],
                    "categoria": p.get("categoria",""),
                    "tamanho": p.get("tamanho",""),
                    "preco": f'{float(p.get("preco",0.0)):.2f}',
                    "quantidade": str(int(p.get("quantidade",0))),
                    "descricao": p.get("descricao","")
                }
                writer.writerow(line)
    except Exception as e:
        print(f"Erro ao salvar produtos: ")


def gerar_id(produtos):
    """Gera novo ID numérico (string) incremental."""
    ids = [int(p["id"]) for p in produtos if p.get("id") and str(p["id"]).isdigit()]
    novo = max(ids)+1 if ids else 1
    return str(novo)


def cadastrar_produto(produtos):
    """Interage com o usuário para cadastrar um produto; retorna True se cadastrado."""
    try:
        print(f"\n--- Cadastro de Produto ---")
        nome = input("Nome: ").strip()
        if not nome:
            print(f"Nome não pode ser vazio. Cadastro cancelado.")
            return False
        categoria = input("Categoria (ex: Camiseta, Calça, Acessório): ").strip()
        tamanho = input("Tamanho (ex: P, M, G, 38): ").strip()
        while True:
            preco_str = input("Preço (ex: 59.90): ").replace(",",".").strip()
            try:
                preco = float(preco_str)
                break
            except:
                print(f"Preço inválido. Tente novamente.")
        while True:
            qtd_str = input("Quantidade em estoque: ").strip()
            try:
                quantidade = int(qtd_str)
                break
            except:
                print(f"Quantidade inválida. Tente novamente.")
        descricao = input("Descrição (opcional): ").strip()
        novo_id = gerar_id(produtos)
        novo = {
            "id": novo_id,
            "nome": nome,
            "categoria": categoria,
            "tamanho": tamanho,
            "preco": preco,
            "quantidade": quantidade,
            "descricao": descricao
        }
        produtos.append(novo)
        salvar_produtos(produtos)
        log_action(f"Cadastro de novo produto: id={novo_id}, nome='{nome}'")
        print(f"Cadastro realizado com sucesso! (ID {novo_id})")
        return True
    except Exception as e:
        print(f"Erro durante cadastro: ")
        return False
        
def agora_str():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def log_action(acao):
    """Grava no arquivo de log a ação com data/hora."""
    garantir_arquivos()
    linha = f"[{agora_str()}] {acao}\n"
    try:
        with open(ARQ_LOG, "a", encoding="utf-8") as f:
            f.write(linha)
    except Exception as e:
        print(f"Erro ao gravar log: ")


def carregar_produtos():
    """Lê produtos do CSV e retorna lista de dicionários."""
    garantir_arquivos()
    produtos = []
    try:
        with open(ARQ_PRODUTOS, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row and row.get("id"):
                    row["preco"] = float(row["preco"]) if row.get("preco") else 0.0
                    row["quantidade"] = int(row["quantidade"]) if row.get("quantidade") else 0
                    produtos.append(row)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Erro ao carregar produtos: ")
    return produtos


def salvar_produtos(produtos):
    """Salva lista de dicionários no CSV (sobrescreve)."""
    garantir_arquivos()
    try:
        with open(ARQ_PRODUTOS, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
            writer.writeheader()
            for p in produtos:
                line = {
                    "id": p["id"],
                    "nome": p["nome"],
                    "categoria": p.get("categoria",""),
                    "tamanho": p.get("tamanho",""),
                    "preco": f'{float(p.get("preco",0.0)):.2f}',
                    "quantidade": str(int(p.get("quantidade",0))),
                    "descricao": p.get("descricao","")
                }
                writer.writerow(line)
    except Exception as e:
        print(f"Erro ao salvar produtos: ")


def gerar_id(produtos):
    """Gera novo ID numérico (string) incremental."""
    ids = [int(p["id"]) for p in produtos if p.get("id") and str(p["id"]).isdigit()]
    novo = max(ids)+1 if ids else 1
    return str(novo)


def cadastrar_produto(produtos):
    """Interage com o usuário para cadastrar um produto; retorna True se cadastrado."""
    try:
        print(f"\n--- Cadastro de Produto ---")
        nome = input("Nome: ").strip()
        if not nome:
            print(f"Nome não pode ser vazio. Cadastro cancelado.")
            return False
        categoria = input("Categoria (ex: Camiseta, Calça, Acessório): ").strip()
        tamanho = input("Tamanho (ex: P, M, G, 38): ").strip()
        while True:
            preco_str = input("Preço (ex: 59.90): ").replace(",",".").strip()
            try:
                preco = float(preco_str)
                break
            except:
                print(f"Preço inválido. Tente novamente.")
        while True:
            qtd_str = input("Quantidade em estoque: ").strip()
            try:
                quantidade = int(qtd_str)
                break
            except:
                print(f"Quantidade inválida. Tente novamente.")
        descricao = input("Descrição (opcional): ").strip()
        novo_id = gerar_id(produtos)
        novo = {
            "id": novo_id,
            "nome": nome,
            "categoria": categoria,
            "tamanho": tamanho,
            "preco": preco,
            "quantidade": quantidade,
            "descricao": descricao
        }
        produtos.append(novo)
        salvar_produtos(produtos)
        log_action(f"Cadastro de novo produto: id={novo_id}, nome='{nome}'")
        print(f"Cadastro realizado com sucesso! (ID {novo_id})")
        return True
    except Exception as e:
        print(f"Erro durante cadastro: ")
        return False

