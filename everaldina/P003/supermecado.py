import produto

def inserir_produto(produtos, nome, preco, quantidade):
    if quantidade >=0 and type(quantidade) == int:
        p = produto.Produto(nome, preco, quantidade)
        produtos.append(p)
    else:
        raise ValueError("Quantidade invalida")
    
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
            return p

def main():
    produtos = []
    qntd_produtos = 0
    
    
    

if __name__ == "__main__":
    main()