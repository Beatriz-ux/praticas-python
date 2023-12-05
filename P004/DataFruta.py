
from abc import ABC, abstractmethod

class Data:
    
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False
    

class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles.
        '''
        print("------------------Entrada de nomes------------------")
        try:
            qtde = int(input("Quantidade de nomes a serem incluidos: "))

            if qtde < 0:
                raise ValueError("Quantidade inválida de nomes.")
        except Exception:
            print("Quantidade inválida de nomes.")
            return

        for i in range(qtde):
            try:
                nome = input(f"Digite o nome {i+1}: ")
                self.__lista.append(nome)
            except Exception:
                print("Nome inválido.")
                i -= 1

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        if len(self.__lista) == 0:
            print("Lista de datas vazia.")
        else:
            listaOrdenada = sorted(self.__lista)

            tam = len(listaOrdenada)

            if tam <= 0:
                print("Lista de nomes vazia.")
                return

            if tam % 2 == 0:
                mediana = listaOrdenada[(tam // 2) - 1]
            else:
                mediana = listaOrdenada[(tam // 2)]

            print("Mediana de nomes: ", mediana)

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        if len(self.__lista) == 0:
            print("Lista de nomes vazia.")
        else:
            menor = self.__lista[0]

            for nome in self.__lista:
                if nome < menor:
                    menor = nome
            
            print("Menor nome: ", menor)

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        if len(self.__lista) == 0:
            print("Lista de nomes vazia.")
        else:
            maior = self.__lista[0]

            for nome in self.__lista:
                if nome > maior:
                    maior = nome
            
            print("Maior nome: ", maior)

    def __str__(self):
        strLista = "--------Lista de Nomes--------\n"

        for nome in self.__lista:
            strLista += nome + "\n"
        
        return strLista
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        
        
        print("------------------Entrada de datas------------------")
        # Pergunta a quantidade de elementos e verifica se é um número inteiro
        try:
            qnt = int(input("Quantidade de elementos na lista de datas: "))
        except Exception:
            print("Quantidade inválida de elementos")
            return
        
        for i in range(qnt):
            # Pergunta a data e verifica se é uma data válida
            # 01/34/6789
            invalido = True
            while(invalido):
                data = input("Digite a data no formato dd/mm/aaaa: ")
                try:
                    dia, mes, ano = data.split("/")
                    
                    if dia.isnumeric() == False:
                        raise ValueError("Dia inválido.")
                    if mes.isnumeric() == False:
                        raise ValueError("Mes inválido.")
                    if mes.isnumeric() == False:
                        raise ValueError("Ano inválido.")
                    
                    data = Data(int(dia), int(mes), int(ano))
                    self.__lista.append(data)
                    print("Data adicionada com sucesso!!")
                    invalido = False
                except ValueError as e:
                    print(str(e))
        
        
    
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        
        if len(self.__lista) == 0:
            print("Lista de datas vazia.")
        else:
            lista_ordenada = sorted(self.__lista)
            tamanho = len(self.__lista)
            if len(self.__lista) % 2 == 0:
                mediana =  lista_ordenada[(tamanho // 2)-1]
            else:
                mediana =  lista_ordenada[tamanho // 2]
            print("Mediana de datas: ", mediana)
     
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        if len(self.__lista) == 0:
            print("Lista de datas vazia.")
        else:
            menor = self.__lista[0]
            for data in self.__lista:
                if data < menor:
                    menor = data
            print("Menor data: ", menor)
    
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        if len(self.__lista) == 0:
            print("Lista de datas vazia.")
        else:
            maior = self.__lista[0]
            for data in self.__lista:
                if data > maior:
                    maior = data
            print("Maior data: ", maior)
    
    def __str__(self):
        strLista = "--------Lista de Datas--------\n"
        for data in self.__lista:
            strLista += str(data) + "\n"
        return strLista

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        pass

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        pass    

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        pass

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        pass
    
    def __str__(self):
        pass

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        pass
    
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        pass    
    
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        pass
    
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        pass

    def __str__(self):
        pass

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]
    # listaListas = [nomes]
    # listaListas = [datas]
    #listaListas = [salarios]
    #listaListas = [idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        print("___________________")

    print("Fim do teste!!!")
    

if __name__ == "__main__":
    main()
