from funcoes import *
def main():
    opcao = None
    codigoSemente = 0
    listaProdutos = []
    while(True):
        match listaMenu():
            case 1:
                try:
                    print("Digite o nome do produto: ",end="")
                    nome = input()
                    print("Digite o preço do produto: ",end="")
                    preco = float(input())
                    codigo = criaCodigo(codigoSemente)
                    codigoSemente = codigoSemente + 1
                    listaProdutos.append(cadastrarProduto(codigo,nome,preco))
                except ValueError as e:
                    print(e)

                
            case 2:
                print("Qual o código do produto que deseja remover?")
                codigo = (input())
                codigo = codigo.zfill(2)
                try:
                    excluirProduto(listaProdutos,codigo)
                except ValueError as e:
                    print(e)
            case 3:
                try:
                    listarProdutos(listaProdutos)
                except ValueError as e:
                    print(e)
            case 4:
                print("Qual o código do produto que deseja buscar?")
                codigo = (input())
                codigo = codigo.zfill(2)
                try:
                    consultarPrecos(listaProdutos,codigo)
                except ValueError as e:
                    print(e)
            case 0:
                print("Saindo...")
                exit()
            case _:
                print("Opção inválida")
        

if __name__ == '__main__':
    main()