def listaMenu():
    print("")
    print("1 - Cadastrar Produto")
    print("2 - Remover Produto")
    print("3 - Listar Produtos")
    print("4 - Consultar Preço")
    print("0 - Sair")
    print("")
    print("Digite a opção desejada: ",end="")
    opcao = int(input())
    return opcao

def cadastrarProduto(codigo,nome,preco):
    if preco <= 0 or isinstance(preco, float) == False:
        raise ValueError("Preço inválido")
    if nome == "" or nome[0].isdigit() == True:
        raise ValueError("Nome inválido")
    
    nome = nome.capitalize()
    preco = round(preco,2)
    novo_produto ={
        "codigo": codigo,
        "nome": nome,
        "preco": preco
    }
    return novo_produto
def excluirProduto(lista, codigo):
    if len(lista) == 0:
        raise ValueError("Lista vazia")
    posicao, _ =buscarProduto(lista, codigo)
    if posicao == -1:
        raise ValueError("Produto não encontrado")
    print("Removendo produto: " + lista[posicao]["nome"])
    lista.pop(posicao)
