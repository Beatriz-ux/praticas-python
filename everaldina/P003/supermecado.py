import produto

class Supermercado:
    __id = "0" * 13
    
    def __init__(self):
        self.__produtos = []
        self.__qntd_produtos = 0
        
    def get_produtos(self):
        return self.__produtos
    def get_qntd_produtos(self):
        return self.__qntd_produtos
    
    def set_produtos(self, produtos):
        self.__produtos = produtos
    def set_qntd_produtos(self, qntd_produtos):
        self.__qntd_produtos = qntd_produtos
    
    def inserir_produto(self, nome, preco):
        if not nome.capitalize()[0].isalpha():
            raise ValueError("Nome invalido")
        else:
            p = {"codigo": Supermercado.__id, "nome": nome, "preco": preco}
            self.__produtos.append(p)
            Supermercado.__id = str(int(Supermercado.__id) + 1).zfill(13)
        
    def remover_produto(self, identificador):
        if type(identificador) == int:
            for p in self.__produtos:
                if p["codigo"] == identificador:
                    self.__produtos.remove(p)
                    return True
            return False
        elif type(identificador) == str:
            for p in self.__produtos:
                if p["nome"] == identificador:
                    self.__produtos.remove(p)
                    return True
            return False
        else:
            raise ValueError("Identificador invalido")

    def listar_produtos(self):
        for p in self.__produtos:
            print("Cod.: " + p["codigo"] + " - " + p["nome"] + " - R$" + p["preco"])

    def buscar_preco(self, cod):
        for p in self.__produtos:
            if p["codigo"] == cod:
                return p["preco"]