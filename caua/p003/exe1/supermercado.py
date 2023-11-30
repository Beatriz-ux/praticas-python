class Produto:
    codigo = ""
    nome = ""
    preco = 0.0

    def __init__(self, nome, codigo, preco):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
    
class Supermercado:
    produtos = []

    def inserirProduto(self):
        print("---Inserindo um novo produto---")
        nome = input("Nome: ")
        codigo = input("Codigo (13 numeros): ")
        preco = float(input("Preco: "))

        produto = Produto(nome.capitalize(), codigo, preco)
        self.produtos.append(produto)
        
        print("Produto cadastrado com sucesso")


    def excluirProduto(self):
        if(self.produtos.count() == 0):
            print("O estoque esta vazio")
            return
        
        print("---Excluindo um produto---")
        codigo = input("Codigo (13 numeros): ")

        index = -1
        check = False

        for i in self.produtos:
            index += 1
            if(i.codigo == codigo):
                check = True
                break;
        
        if(check == False):
            print("Codigo nao encontrado")
            return
        
        self.produtos.remove(index)
        print("Produto excluido com sucesso")
    

    def listarProduto(self):
        if(self.produtos.count() == 0):
            print("O estoque esta vazio")
            return
        
        print("---Listando Produtos---")

        for i in self.produtos:
            print("{} - {} - R${}".format(i.codigo, i.nome, format(i.preco, "2f")))


    def consultarProduto(self):
        if(self.produtos.count() == 0):
            print("O estoque esta vazio")
            return
        
        print("---Consultando um produto---")
        codigo = input("Codigo (13 numeros): ")

        index = -1
        check = False

        for i in self.produtos:
            index += 1
            if(i.codigo == codigo):
                check = True
                break;
        
        if(check == False):
            print("Codigo nao encontrado")
            return
        
        p = self.produtos[i]
        print("{} - {} - R${}".format(p.codigo, p.nome, format(p.preco, "2f")))
    

        
        
