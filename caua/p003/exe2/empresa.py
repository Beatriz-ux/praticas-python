def cadastrarFuncionario(lista):
    print("---Cadastrando um novo funcionario---")
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    
    anoNascimento = input("Ano de nascimento: ")
    if (not anoNascimento.isnumeric()):
        print("Erro: digite um ano valido")
        return
    anoNascimento = int(anoNascimento)

    rg = input("RG (9 numeros): ")
    if len(rg) != 9 or (not rg.isnumeric()):
        print("Erro: o RG deve conter apenas 9 caracteres numericos")
        return
    for i in lista:
        if rg == i['rg']:
            print("Erro: RG ja Cadastrado")
            return
        
    anoAdmissao = input("Ano de admissao: ")
    if (not anoAdmissao.isnumeric()):
        print("Erro: digite um ano valido")
        return
    anoAdmissao = int(anoAdmissao)

    salario = input("Salario: ")
    try:
        salario = float(salario)
    except:
        print("Erro: Digite um valor valido")
        return
    if salario <= 0:
        print("Erro: Digite um valor valido")
        return

    funcionario = {"nome": nome.capitalize(), "sobrenome": sobrenome.capitalize(), 'anoNascimento': anoNascimento, 'rg': rg, "anoAdmissao": anoAdmissao, 'salario': salario} 
    lista.append(funcionario)
    
    print("Funcionario cadastrado com sucesso")


def removerFuncionario(lista):
    if(len(lista) == 0):
        print("A lista esta vazia")
        return
    
    print("---Removendo um funcionario---")
    rg = input("RG (9 numeros): ")

    if len(rg) != 9 or (not rg.isnumeric()):
        print("Erro: o RG deve conter apenas 9 caracteres numericos")
        return
    
    index = -1
    check = False

    for i in lista:
        index += 1
        if(i['rg'] == rg):
            check = True
            break;
    
    if(check == False):
        print("RG nao encontrado")
        return
    
    lista.pop(index)
    print("Funcionario removido com sucesso")


def listarFuncionario(lista):
    if(len(lista) == 0):
        print("A lista esta vazia")
        return
    
    print("---Listando Funcionarios---")

    qtde = 0
    listaOrdenada = sorted(lista, key= lambda x: x['salario'])
    for i in listaOrdenada:
        if qtde%10 == 0 and qtde != 0:
            print("--------------------------")
        qtde+=1
        print("{} {} - {} - {} - {} - R${}".format(i['nome'], i['sobrenome'], i['anoNascimento'], i['rg'], i['anoAdmissao'], '{0:.2f}'.format(i["salario"])))
        

def consultarFuncionario(lista):
    if(len(lista) == 0):
        print("A lista esta vazia")
        return
    
    print("---Consultando um funcionario---")
    rg = input("RG (9 numeros): ")

    if len(rg) != 9 or (not rg.isnumeric()):
        print("Erro: o RG deve conter apenas 9 caracteres numericos")
        return
    
    index = -1
    check = False

    for i in lista:
        index += 1
        if(i['rg'] == rg):
            check = True
            break;
    
    if(check == False):
        print("RG nao encontrado")
        return
    
    p = lista[index]
    print("{} {} - {} - {} - {} - R${}".format(i['nome'], i['sobrenome'], i['anoNascimento'], i['rg'], i['anoAdmissao'], '{0:.2f}'.format(i["salario"])))


def Reajusta_dez_porcento(lista):
    if(len(lista) == 0):
        print("A lista esta vazia")
        return
    
    print("---Reajustando salario---")

    for i in range(len(lista)):
        lista[i]['salario'] *= 1.1

    print("Salario de todos os funcionarios aumentado em 10%")