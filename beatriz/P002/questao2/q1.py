nome_arquivo = './beatriz/P002/questao2/arquivo.txt'

if not os.path.exists(nome_arquivo):
    # Verifica se o diretório existe, se não, cria o diretório
    diretorio = os.path.dirname(nome_arquivo)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    # Cria o arquivo vazio
    with open(nome_arquivo, 'w') as arquivo:
        pass  # Arquivo criado, mas vazio
