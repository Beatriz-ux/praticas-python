
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

    @abstractmethod
    def listarEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []   
    def __iter__(self):
        return iter(self.__lista)     

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
	
    def listarEmOrdem(self):
        '''
        Este método ordena a lista e mostra os
        elementos em ordem crescente
        '''
        if len(self.__lista) == 0:
            print("Lista de nomes vazia.")
        else:
            listaOrdenada = sorted(self.__lista)
            print("Lista de nomes em ordem crescente:\n", listaOrdenada)

class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []  

    def __iter__(self):
        return iter(self.__lista)         
    
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
    
    def listarEmOrdem(self):
        '''
        Este método ordena a lista e mostra os
        elementos em ordem crescente, só é possivel ultilzar o metodo sort() pois a classe 
        Data implementa os metodos __lt__ e __gt__ que fazem a comparação entre datas de forma particionada
        '''
        if len(self.__lista) == 0:
            print("Lista de datas vazia.")
        else:
            lista_ordenada = sorted(self.__lista)
            print("Lista de datas em ordem crescente:"  )
            for data in lista_ordenada:
                print(data)

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []  
    def __iter__(self):
        return iter(self.__lista)      

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        print("------------------Entrada de Salarios------------------")
        # Pergunta a quantidade de elementos e verifica se é um número inteiro
        try:
            qnt = int(input("Quantidade de elementos na lista de salarios: "))
        except Exception:
            print("Quantidade inválida de elementos")
            return
        
        for i in range(qnt):
            salario = 0
            invalido = True
            while invalido:
                try:
                    salario = float(input("Digite o valor do salario: "))
                except:
                    print("Valor inválido.")
                
                if salario < 0:
                    print("Salario não pode ser nagativo")
                else:
                    self.__lista.append(salario)
                    print("Salario adicionado com sucesso!!")
                    invalido = False
            

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        if len(self.__lista) == 0:
            print("Lista de salarios vazia.")
            return
        ordenados = sorted(self.__lista)
        tamanho = len(self.__lista)
        mediana = -1
        if tamanho % 2 == 0:
            mediana1 = ordenados[(tamanho // 2) - 1]
            mediana2 = ordenados[tamanho // 2]
            mediana = (mediana1 + mediana2) / 2
        else:
            mediana = ordenados[tamanho // 2]

        print("Mediana de salarios: ", mediana)

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        if len(self.__lista) == 0:
            print("Lista de salarios vazia.")
            return
        ordenada = sorted(self.__lista)
        menor = ordenada[0]
        print("Menor salario: ", menor)

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        if len(self.__lista) == 0:
            print("Lista de salarios vazia.")
            return
        ordenada = sorted(self.__lista)
        maior = ordenada[-1]
        print("Maior salario: ", maior)
    
    def __str__(self):
        strLista = "--------Lista de Salarios--------\n"
        for salario in self.__lista:
            strLista += str(salario) + "\n"
        return strLista
    
    def listarEmOrdem(self):
        '''
        Este método ordena a lista e mostra os
        elementos em ordem crescente
        '''
        if len(self.__lista) == 0:
            print("Lista de salarios vazia.")
            return
        ordenada = sorted(self.__lista)
        print("Lista de salarios em ordem crescente:\n", ordenada)

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

        print("--------------Entrada de idades--------------")
        try:
            qtde = int(input("Quantidade de idades a serem incluidas: "))
        except Exception:
            print("Quantidade inválida de idades.")
            return
        
        if qtde < 0:
            print("Quantidade inválida de idades.")
            return
        
        listaAuxiliar = []
        for i in range(qtde):
            try:
                idade = int(input("Idade: "))
            except Exception:
                print("Idade invalida.")
                return
            
            if idade < 0:
                print("Idade invalida.")
                return
            
            listaAuxiliar.append(idade)
        
        for i in listaAuxiliar:
            self.__lista.append(i)

    
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''

        if len(self.__lista) == 0:
            print("A lista esta vazia")
            return
        
        listaAuxiliar = self.__lista.copy()
        listaAuxiliar.sort()
        tamanho = len(listaAuxiliar)
        mediana = 0;

        if tamanho % 2 == 0:
            mediana = (listaAuxiliar[tamanho//2] + listaAuxiliar[(tamanho//2) - 1]) / 2
        else:
            mediana = listaAuxiliar[tamanho//2]

        print("Mediana de idades: ", mediana)    
    
    def mostraMenor(self):
        '''
        Este método retorna o menor elemento da lista
        '''

        if len(self.__lista) == 0:
            print("A lista esta vazia")
            return
        
        menor = self.__lista[0]

        for i in self.__lista:
            if i < menor:
                menor = i

        print("Menor idade: ", menor)
    
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''

        if len(self.__lista) == 0:
            print("A lista esta vazia")
            return
        
        maior = self.__lista[0]

        for i in self.__lista:
            if i > maior:
                maior = i

        print("Maior idade ", maior)

    def __str__(self):
        strLista = "--------Lista de Idades--------\n"

        for i in self.__lista:
            strLista += i + "\n"
        
        return strLista
    
    def listarEmOrdem(self):
        '''
        Este método ordena a lista e mostra os
        elementos em ordem crescente
        '''
        if len(self.__lista) == 0:
            print("Lista de idades vazia.")
            return
        ordenada = sorted(self.__lista)
        print("Lista de idades em ordem crescente:\n", ordenada)

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    # #listaListas = [nomes, datas, salarios, idades]
    # listaListas = [nomes]
    # # listaListas = [datas]
    # # listaListas = [salarios]
    # # listaListas = [idades]

    # for lista in listaListas:
    #     lista.entradaDeDados()
    #     lista.mostraMediana()
    #     lista.mostraMenor()
    #     lista.mostraMaior()
    #     lista.listarEmOrdem()
    
    print("___________________")
    nomes.entradaDeDados()
    salarios.entradaDeDados()
    datas.entradaDeDados()
    for nome, salario in zip(nomes,salarios):
        print(nome, '-', salario)

    print("___Salario com Reajuste 10%___")
    for salario in map(lambda x: x * 1.1, salarios):
         print(f'{salario:.2f}')

    datasAnteriores = filter(lambda data: data.ano < 2019, datas)
    for data in datasAnteriores:
        setattr(data, 'dia', 1)
        print(data)

    # print("Fim do teste!!!")
    

if __name__ == "__main__":
    main()