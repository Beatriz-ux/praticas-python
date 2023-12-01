from empresa import * 

def main():
    pass


if __name__ == "__main__":
    main()

fileName = "p003/exe2/funcionarios.txt"
listaFuncionarios = []

listaAux = []
funcAux = {"nome": '', "sobrenome": '', 'anoNascimento': '', 'rg': '', "anoAdmissao": '', 'salario': ''} 
with open(fileName) as file:
    listaAux = file.read().splitlines() 
file.close()

for i in range(len(listaAux)):
    match i%6:
        case 0:
            funcAux['nome'] = listaAux[i]
        case 1:
            funcAux['sobrenome'] = listaAux[i]
        case 2:
            funcAux['anoNascimento'] = int(listaAux[i])
        case 3:
            funcAux['rg'] = listaAux[i]
        case 4:
            funcAux['anoAdmissao'] = int(listaAux[i])
        case 5:
            funcAux['salario'] = float(listaAux[i])
            listaFuncionarios.append(funcAux)
            funcAux = {"nome": '', "sobrenome": '', 'anoNascimento': '', 'rg': '', "anoAdmissao": '', 'salario': ''} 

    

acao = ''

while(acao != '0'):
    print("\n---Menu da Empresa---")
    print("1 - Cadastrar um novo funcionario")
    print("2 - Remover um funcionario")
    print("3 - Listar todos os funcionarios")
    print("4 - Consultar dados de um funcionario")
    print("5 - Reajustar salario em 10%")
    print("0 - Sair")
    acao = input("Digite uma opcao: ")

    print()
    match acao:
        case '0': 
            print("---Finalizando sessao---")

        case "1":
            cadastrarFuncionario(listaFuncionarios)
            
        case '2':
            removerFuncionario(listaFuncionarios)
            
        case '3':
            listarFuncionario(listaFuncionarios)
            
        case '4':
            consultarFuncionario(listaFuncionarios)
        
        case '5':
            Reajusta_dez_porcento(listaFuncionarios)
        
        case _:
            print("--Erro--")
            print("Opcao invalida, digite um numero de 0 a 4")
            

file = open(fileName, "w");

for i in listaFuncionarios:
    file.write("{}\n".format(i['nome']))
    file.write("{}\n".format(i['sobrenome']))
    file.write("{}\n".format(str(i['anoNascimento'])))
    file.write("{}\n".format(i['rg']))
    file.write("{}\n".format(str(i['anoAdmissao'])))
    file.write("{}\n".format(str(i['salario'])))


file.close()
print("Arquivo salvo com sucesso!")

'''
for i in listaFuncionarios:
    file.write(i['nome'], '/n')
    file.write(i['sobrenome'],'/n')
    file.write(str(i['anoNascimento']),'/n')
    file.write(i['rg'])
    file.write(str(i['anoAdmissao']),'/n')
    file.write(str(i['salario']), '/n')
'''