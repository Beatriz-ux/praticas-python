import os 
import json
def abrirArquivo(nomeArquivo):
    if not os.path.exists(nomeArquivo):
    # Verifica se o diretório existe, se não, cria o diretório
        diretorio = os.path.dirname(nomeArquivo)
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

        # Cria o arquivo vazio
        with open(nomeArquivo, 'w') as arquivo:
            pass  # Arquivo criado, mas vazio


def atualizarArquivo(lista, nomeArquivo):
    with open(nomeArquivo, 'w') as arquivo:
        json.dump(lista, arquivo)
    print("Arquivo salvo com sucesso!")

def lerArquivo(nomeArquivo):
    with open(nomeArquivo, 'r') as arquivo:
        lista = json.load(arquivo)
    return lista