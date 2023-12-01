import random

def main():
    empregados = []

    with open("empregados.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.split(";")

            empregado = {
                "nome": dados[0],
                "sobrenome": dados[1],
                "ano_nascimento": dados[2],
                "rg": dados[3],
                "ano_admissao": dados[4],
                "salario": dados[5]
            }

            empregados.append(empregado)
    
    # gerarEmpregados(empregados)
    menu(empregados)

def menu(empregados: list):
    while True:
        print("1. Reajustar salário de todos os empregados")
        print("2. Listar todos os empregados")
        print("3. Adicionar um novo empregado")
        print("4. Salvar alterações")
        print("0. Sair")

        op = int(input("Digite uma opção: "))

        if op == 1:
            reajustaDezPorcento(empregados)
            print()
        elif op == 2:
            listaEmpregados(empregados)
            print()
        elif op == 3:
            adcionarEmpregado(empregados)
            print()
        elif op == 4:
            salvarAlteracoes(empregados)
            print()
        elif op == 0:
            salvarAlteracoes(empregados)
            exit()
        else:
            print("Opção invalida")

def reajustaDezPorcento(empregados: list):
    for empregado in empregados:
        empregado['salario'] = float(empregado['salario']) * 1.1

    print("Salário reajustado com sucesso")

def listaEmpregados(empregados: list):
    print("---------------------------------------------------------------------------------------------")
    print("Empregados:")

    for empregado in empregados:
        print(f"Nome: {empregado['nome']}")
        print(f"Sobrenome: {empregado['sobrenome']}")
        print(f"Ano de nascimento: {empregado['ano_nascimento']}")
        print(f"RG: {empregado['rg']}")
        print(f"Ano de admissão: {empregado['ano_admissao']}")
        print(f"Salário: {empregado['salario']}")
        print()

    print("---------------------------------------------------------------------------------------------")


def gerarEmpregados(empregados: list):
    for i in range(25):
        nome = "Empregado " + str(i)
        sobrenome = "Sobrenome " + str(i)
        ano_nascimento = random.randint(1900, 2020)
        rg = random.randint(1000000, 9999999)
        ano_admissao = random.randint(1900, 2020)
        salario = random.randint(1000, 10000)

        empregado = {
            "nome": nome,
            "sobrenome": sobrenome,
            "ano_nascimento": ano_nascimento,
            "rg": rg,
            "ano_admissao": ano_admissao,
            "salario": salario
        }

        empregados.append(empregado)

def adcionarEmpregado(empregados: list):
    nome = input("Digite o nome do empregado: ")
    sobrenome = input("Digite o sobrenome do empregado: ")
    ano_nascimento = input("Digite o ano de nascimento do empregado: ")
    rg = input("Digite o RG do empregado: ")
    ano_admissao = input("Digite o ano de admissão do empregado: ")
    salario = input("Digite o salário do empregado: ")

    empregado = {
        "nome": nome,
        "sobrenome": sobrenome,
        "ano_nascimento": ano_nascimento,
        "rg": rg,
        "ano_admissao": ano_admissao,
        "salario": salario
    }

    addEmpregado(empregado, empregados)

def addEmpregado(empregado: dict, empregados: list):
    empregados.append(empregado)


def salvarAlteracoes(empregados: list):
    with open("empregados.txt", "w") as arquivo:
        for empregado in empregados:
            arquivo.write(f"{empregado['nome']};{empregado['sobrenome']};{empregado['ano_nascimento']};{empregado['rg']};{empregado['ano_admissao']};{empregado['salario']}\n")

if __name__ == "__main__":
    main()