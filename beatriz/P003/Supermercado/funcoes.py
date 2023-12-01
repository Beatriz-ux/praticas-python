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
    

def buscarProduto(lista, codigo):
    for indice, produto in enumerate(lista):
        if produto["codigo"] == codigo:
            return indice, produto
    return -1, None

def listarProdutos(lista):
    pagina = 1
    qtd_por_pagina = 10
    if len(lista) == 0:
        raise ValueError("Lista vazia")
    print()
    while(True):
        print("Página: " + str(pagina))
        print("{:<4} {:<13} {:15} {:<10}".format("ID", "Código","Nome","Preço"))
        for indice, produto in enumerate(lista):
            if indice >= (pagina - 1) * qtd_por_pagina and indice < pagina * qtd_por_pagina:
                print("{:<4} {:<13} {:15} {:<10}".format(str(indice),produto["codigo"],produto["nome"],'{:.2f}'.format(produto["preco"])))
        print("1 - Próxima página")
        print("2 - Página anterior")
        print("3 - Voltar")
        opcao = int(input())
        if opcao == 1:
            pagina = pagina + 1
        elif opcao == 2:
            pagina = pagina - 1
        elif opcao == 3:
            break
        else:
            print("Opção inválida")

def consultarPrecos(lista, codigo):
    posicao, produto = buscarProduto(lista, codigo)
    if posicao == -1:
        raise ValueError("Produto não encontrado")
    print("Produto: " + produto["nome"])
    print("Preço: " + '{:.2f}'.format(produto["preco"]))

def criaCodigo(semente):
    return str(semente + 1).zfill(13)