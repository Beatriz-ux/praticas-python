class Supermercado:
    # id um string de 13 carateres, iniciado com 13 zeros
    __id = "0" * 13
    
    def __init__(self):
        self.__produtos = []
        self.__qntd_produtos = 0
    
    # Getters e Setters
    def get_produtos(self):
        return self.__produtos
    def get_qntd_produtos(self):
        return self.__qntd_produtos
    
    def set_produtos(self, produtos):
        self.__produtos = produtos
    def set_qntd_produtos(self, qntd_produtos):
        self.__qntd_produtos = qntd_produtos
    
    
    def inserir_produto(self, nome, preco):
        
        # verifica se o nome é uma string nao nula começada com uma letra
        if nome == "" or nome == None:
            raise ValueError("Nome invalido")
        if not nome.capitalize()[0].isalpha():
            raise ValueError("Nome invalido")
       
        # verifica se o preço é um número
        try:
            preco = float(preco)
        except ValueError:
            raise ValueError("Preco invalido")
        
        # trunca o preço para duas casas decimais
        preco_formatado = float(str(preco)[0: str(preco).find(".") + 3])
        
        # verifica se o preço é negativo
        if preco_formatado < 0:
            raise ValueError("Preco invalido")
        
        # cria um dicionário com os dados do produto e adiciona aos produtos
        p = {"codigo": Supermercado.__id, "nome": nome, "preco": preco_formatado}
        self.__produtos.append(p)
        
        # incrementa o id
        Supermercado.__id = str(int(Supermercado.__id) + 1).zfill(13)
        return True
        
    def remover_produto(self, identificador):
        # converte o identificador para inteiro
        try:
            identificador = int(identificador)
        except ValueError:
            pass
        
        # remove o produto com o id informado
        for p in self.__produtos:
            if int(p["codigo"]) == identificador: # ignora o zero a esquerda
                self.__produtos.remove(p)
                return True
        return False

    def listar_produtos(self):
        lista_ordenada = sorted(self.__produtos, key=lambda k: k["preco"])
        
        # imprime os produtos em grupos de 10
        for i in range(0, len(lista_ordenada), 10):
            sub_lista = lista_ordenada[i: i + 10]
            for p in sub_lista:
                print("Cod.: " + p["codigo"] + " - " + p["nome"] + " - R$" + "{:.2f}".format(p["preco"]))
            input()

    def buscar_preco(self, cod):
        # converte o código para inteiro
        try:
            cod = int(cod)
        except ValueError:
            pass
        
        # retorna o preço do produto com o código informado
        for p in self.__produtos:
            if int(p["codigo"]) == cod:
                return p["preco"]