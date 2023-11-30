import produto

class Supermercado:
    def __init__(self):
        self.__produtos = []
        self.qntd_produtos = 0
    
    def inserir_produto(produtos, nome, preco):
        p = produto.Produto(nome, preco)
        produtos.append(p)
        
    def remover_produto(produtos, identificador):
        if type(identificador) == int:
            for p in produtos:
                if p.get_id() == identificador:
                    produtos.remove(p)
                    return True
            return False
        elif type(identificador) == str:
            for p in produtos:
                if p.get_nome() == identificador:
                    produtos.remove(p)
                    return True
            return False
        else:
            raise ValueError("Identificador invalido")

    def listar_produtos(produtos):
        for p in produtos:
            print(p)    

    def buscar_produto(produtos, cod):
        for p in produtos:
            if p.get_id() == cod:
                return p.get_preço