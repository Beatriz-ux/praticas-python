from supermercado import Supermercado

def main():
    sp = Supermercado()
    opcao = -1
    
    sp.inserir_produto("Arroz", 10.50)
    sp.inserir_produto("Feijão", 7.50)
    sp.inserir_produto("Macarrão", 5.50)
    sp.inserir_produto("Farinha", 3.50)
    sp.inserir_produto("Açucar", 4.50)
    sp.inserir_produto("Café", 6.50)
    sp.inserir_produto("Óleo", 8.50)
    sp.inserir_produto("Sal", 2.50)
    sp.inserir_produto("Leite", 3.50)
    sp.inserir_produto("Manteiga", 5.50)
    sp.inserir_produto("Queijo", 7.50)
    sp.inserir_produto("Presunto", 9.50)
    sp.inserir_produto("Mortadela", 11.50)
    sp.inserir_produto("Pão", 1.50)
    sp.inserir_produto("Biscoito", 3.50)
    sp.inserir_produto("Bolacha", 5.50)
    
    
    while opcao != 0:
        print("1. Inserir produto")
        print("2. Excluir produto")
        print("3. Listar produtos")
        print("4. Cosultar preço")
        print("0. Sair")
        
        while True:
            try:
                opcao = int(input("Digite a opção desejada: "))
                if opcao < 0 or opcao > 4:
                    raise ValueError
                break
            except ValueError:
                print("Opção inválida. Digite novamente.")
                
        match opcao:
            case 1:
                print("\n------ADICIONAR PRODUTO------")
                nome = input("Digite o nome do produto: ")
                preco = input("Digite o preço do produto: ")
                
                
                try:
                    if(sp.inserir_produto(nome, preco)):
                        print("Produto inserido com sucesso.")
                except ValueError as e:
                    print(str(e))
                    
            case 2:
                print("\n------REMOVER PRODUTO------")
                id = input("Digite o código do produto: ")
                try:
                    if(sp.remover_produto(id)):
                        print("Produto removido com sucesso.")
                    else:
                        print("Produto não encontrado.")
                except ValueError as e:
                    print(e)
            case 3:
                print("\n------LISTAR PRODUTOS------")
                sp.listar_produtos()
            case 4:
                print("\n------BUSCAR PRODUTOS------")
                codigo = input("Digite o código do produto: ")
                
                preco = sp.buscar_preco(codigo)
                
                if preco != None:
                    print("O preço do produto é R$" + str(sp.buscar_preco(codigo)))
                else:
                    print("Produto não encontrado.")
            case 0:
                print("\nSaindo...")
            case _:
                print("Opção inválida. Digite novamente.")
        input()

if __name__ == "__main__":
    main()


