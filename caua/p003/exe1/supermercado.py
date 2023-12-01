def inserirProduto(lista):
    print("---Inserindo um novo produto---")
    nome = input("Nome: ")
    codigo = input("Codigo (13 numeros): ")
    if len(codigo) != 13 or (not codigo.isnumeric()):
        print("Erro: o codigo deve conter apenas 13 caracteres numericos")
        return

    for i in lista:
        if codigo == i['codigo']:
            print("Erro: Codigo ja existe")
            return

    preco = input("Preco: ")
    
    try:
        preco = float(preco)
    except:
        print("Erro: Digite um valor valido")
        return
    
    if preco <= 0:
        print("Erro: Digite um valor valido")
        return

    produto = {"nome": nome.capitalize(), "codigo": codigo, "preco": preco} 
    lista.append(produto)
    
    print("Produto cadastrado com sucesso")


def excluirProduto(lista):
    if(len(lista) == 0):
        print("O estoque esta vazio")
        return
    
    print("---Excluindo um produto---")
    codigo = input("Codigo (13 numeros): ")

    if len(codigo) != 13 or (not codigo.isnumeric()):
        print("Erro: o codigo deve conter apenas 13 caracteres numericos")
        return
    
    index = -1
    check = False

    for i in lista:
        index += 1
        if(i['codigo'] == codigo):
            check = True
            break;
    
    if(check == False):
        print("Codigo nao encontrado")
        return
    
    lista.pop(index)
    print("Produto excluido com sucesso")


def listarProduto(lista):
    if(len(lista) == 0):
        print("O estoque esta vazio")
        return
    
    print("---Listando Produtos---")

    qtde = 0
    listaOrdenada = sorted(lista, key= lambda x: x['preco'])
    for i in listaOrdenada:
        if qtde%10 == 0 and qtde != 0:
            print("--------------------------")
        qtde+=1
        print("{} - {} - R${}".format(i['codigo'], i['nome'], '{0:.2f}'.format(i["preco"])))
        

def consultarProduto(lista):
    if(len(lista) == 0):
        print("O estoque esta vazio")
        return
    
    print("---Consultando um produto---")
    codigo = input("Codigo (13 numeros): ")

    if len(codigo) != 13 or (not codigo.isnumeric()):
        print("Erro: o codigo deve conter apenas 13 caracteres numericos")
        return
    
    index = -1
    check = False

    for i in lista:
        index += 1
        if(i['codigo'] == codigo):
            check = True
            break;
    
    if(check == False):
        print("Codigo nao encontrado")
        return
    
    p = lista[index]
    print("{} - {} - R${}".format(p['codigo'], p['nome'], '{0:.2f}'.format(p["preco"])))

