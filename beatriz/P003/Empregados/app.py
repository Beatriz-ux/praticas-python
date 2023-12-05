def cadastrarFuncionario(nome, sobrenome, anoNasc,rg,anoAdm,salario):
    nome = nome.strip() #remove espaços em branco no inicio e no fim
    sobrenome = sobrenome.strip() #remove espaços em branco no inicio e no fim
    if nome == "" or nome[0].isdigit() == True:
        raise ValueError("Nome inválido")
    if sobrenome == "" or sobrenome[0].isdigit() == True:
        raise ValueError("Sobrenome inválido")
    if anoNasc < 1900 or anoNasc > 2021:
        raise ValueError("Ano de nascimento inválido")
    if anoAdm < 1900 or anoAdm > 2023:
        raise ValueError("Ano de admissão inválido")
    if anoAdm < anoNasc:
        raise ValueError("Ano de admissão não pode ser menor que o ano de nascimento")
    if salario < 0:
        raise ValueError("Salário não pode ser negativo")
    if salario < 1100:
        raise ValueError("Salário não pode ser menor que o salário mínimo")
    if salario == 0:
        raise ValueError("Salário não pode ser zero")
    if len(rg) != 10:
        raise ValueError("RG inválido")
    nome = nome.capitalize()
    sobrenome = sobrenome.capitalize()
    novo_funcionario ={
        "nome": nome,
        "sobrenome": sobrenome,
        "anoNasc": anoNasc,
        "rg": rg,
        "anoAdm": anoAdm,
        "salario": salario
    }
    return novo_funcionario
def Reajusta_dez_porcento(lista):
    listaNova = []
    listaNova = list(map(lambda x:{ **x,"salario":x["salario"] *1.10}, lista))
    return listaNova
def listarFuncionarios(lista):
    if len(lista) == 0:
        raise ValueError("Lista vazia")
    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("Nome","Sobrenome","Ano de Nascimento","RG","Ano de Admissão","Salário"))
    for i in lista:
        print("{:<20} {:<20} {:<20} {:<20} {:<20} R${:<17.2f}".format(i["nome"],i["sobrenome"],i["anoNasc"],i["rg"],i["anoAdm"],i["salario"]))

def listaMenu():
    print("")
    print("1 - Cadastrar Funcionario")
    print("2 - Fazer Reajuste de 10%")
    print("3 - Listar Funcionarios")
    print("0 - Sair")
    print("")
    print("Digite a opção desejada: ",end="")
    opcao = int(input())
    return opcao