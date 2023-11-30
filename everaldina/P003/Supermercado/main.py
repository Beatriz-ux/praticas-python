from supermercado import Supermercado as sp

def main():
    opcao = 0
    
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
                print("------ADICIONAR PRODUTO------")
                nome = input("Digite o nome do produto: ")
                preco = input("Digite o preço do produto: ")
                
                try:
                    sp.inserir_produto(nome, preco)
                except ValueError as e:
                    print(e)
                    
            case 2:
                print("------REMOVER PRODUTO------")
                id = input("Digite o código ou nome do produto: ")
                try:
                    sp.remover_produto(id)
                    print("Produto removido com sucesso.")
                except ValueError as e:
                    print(e)
            case 3:
                print("------LISTAR PRODUTOS------")
                sp.listar_produtos()
            case 4:
                print("------BUSCAR PRODUTOS------")
                codigo = input("Digite o código do produto: ")
                
                print("\nO preço do produto é R$" + str(sp.buscar_preco(codigo)))
            case 0:
                print("Saindo...")
            case _:
                print("Opção inválida. Digite novamente.")


if __name__ == "__main__":
    main()


