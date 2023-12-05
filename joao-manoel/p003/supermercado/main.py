import random

def adcionarProduto(Produtos):
    print()
    codigo = gerarCodigo()
    nome = input("Digite o nome do produto: ")
    nome = nome.capitalize()
    preco = input("Digite o preco do produto: ")
    print()

    produto = {'codigo': codigo, 'nome': nome, 'preco': float(preco)}
    addProduto(produto, Produtos)

def addProduto(produto: dict, Produtos: list):
    Produtos.append(produto)

def gerarCodigo():
    codigo = ""

    for i in range(13):
        codigo += str(random.randint(0, 9))

    return codigo

def delProduto(codigo: str, Produtos: list):
    for produto in Produtos:
        if produto['codigo'] == codigo:
            Produtos.remove(produto)
            return True
    return False

def listaProdutos(Produtos):
    print("\n----------------------------------------------------------------")
    print("Lista de produtos:")
    
    Produtos.sort(key=lambda produto: produto['preco'], reverse=True)

    for i in range(0, len(Produtos), 10):
        print("Codigo".ljust(13),"\t-\tNome".ljust(25), "\t-\tPreço")

        for produto in Produtos[i:i+10]:
            print(f'{produto["codigo"]}\t-\t{produto["nome"].ljust(20)}\t-\t{produto["preco"]:0.2f}')

        if i+10 < len(Produtos):
            input("\nPressione enter para mostrar mais produtos")

    print("\n----------------------------------------------------------------\n")

def consultaPreco(codigo: str, Produtos: list):
    flag = True

    for produto in Produtos:
        if produto['codigo'] == codigo:
            print(f'Preço de {produto["nome"]}: {produto["preco"]:0.2f}\n')
            flag = False

    if flag:
        print("Produto não encontrado")


def main():
    Produtos = []

    # Testes
    for i in range(25):
        codigo = gerarCodigo()
        nome = "Produto " + str(i)
        preco = random.randint(1, 1000)

        produto = {'codigo': codigo, 'nome': nome, 'preco': float(preco)}
        addProduto(produto, Produtos)

    # Menu
    while True:
        print("1. Inserir um novo produto")
        print("2. Excluir um produto cadastrado")
        print("3. Listar todos os produtos com seus respectivos códigos e preços")
        print("4. Consultar o preço de um produto através de seu código.")
        print("0. Sair")

        op = int(input("Digite uma opção: "))

        if op == 1:
            adcionarProduto(Produtos)
        elif op == 2:
            codigo = input("Digite o codigo do produto: ")
            delProduto(codigo, Produtos)
            print()
        elif op == 3:
            listaProdutos(Produtos)
        elif op == 4:
            codigo = input("Digite o codigo do produto: ")
            consultaPreco(codigo, Produtos)
        elif op == 0:
            exit()
        else:
            print("Opção invalida")


if __name__ == "__main__":
    main()


