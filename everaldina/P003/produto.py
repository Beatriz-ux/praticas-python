class Produto:
    __id = 0
    
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco
        self.__id = Produto.__id
        Produto.__id += 1

    def get_nome(self):
        return self.__nome
    def get_preco(self):
        return self.__preco
    
    def set_nome(self, nome):
        self.__nome = nome
    def set_preco(self, preco):
        self.__preco = preco
        
    def __str__(self):
        return "Cod.: " + str(self.__id) + " - " + self.__nome + " - R$" + str(self.__preco)
