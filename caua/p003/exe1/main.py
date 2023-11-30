from supermercado import * 

def main():
    pass


if __name__ == "__main__":
    main()

listaProdutos = []
acao = ''

while(acao != '0'):
    print("\n---Menu do supermercado---")
    print("1 - Inserir um novo produto")
    print("2 - Excluir um produto cadastrado")
    print("3 - Listar todos os produtos")
    print("4 - Consultar o preco de um produto")
    print("0 - Sair")
    acao = input("Digite uma opcao: ")

    print()
    match acao:
        case '0': 
            print("---Finalizando sessao---")

        case "1":
            inserirProduto(listaProdutos)
            
        case '2':
            excluirProduto(listaProdutos)
            
        case '3':
            listarProduto(listaProdutos)
            
        case '4':
            consultarProduto(listaProdutos)
        
        case _:
            print("--Erro--")
            print("Opcao invalida, digite um numero de 0 a 4")
            
            