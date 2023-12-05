from app import *
from utils import *
def main():
    nome_arquivo = './empregados.txt'
    abrirArquivo(nome_arquivo)
    opcao = None
    codigoSemente = 0
    listaEmpregados = []
    try:
        listaEmpregados = lerArquivo(nome_arquivo)
    except ValueError as e:
        print("Arquivo vazio")
    while(True):
        match listaMenu():
            case 1:
                try:
                    salario = 0
                    nome = ""
                    sobrenome = ""
                    print("Digite o nome completo do empregado: ",end="")
                    nomeCompleto = input()
                    nomeCompleto = nomeCompleto.strip() #remove espaços em branco no inicio e no fim
                    try:
                        nome , sobrenome = nomeCompleto.split(" ",1)

                    except ValueError as e:
                        print("Informe nome e sobrenome")
                        continue
                    
                    print("Digite o salário do empregado: ",end="")
                    try:
                        salario = float(input())
                    except ValueError as e:
                        print("Salário inválido")
                    
                    print("Digite o ano de nascimento: ",end="")
                    anoNasc = int(input())
                    print("Digite o RG: ",end="")
                    rg = input()
                    print("Digite o ano de admissão: ",end="")
                    anoAdm = int(input())
                    try:
                        listaEmpregados.append(cadastrarFuncionario(nome, sobrenome, anoNasc,rg,anoAdm,salario))
                        atualizarArquivo(listaEmpregados,"./empregados.txt")
                    except ValueError as e:
                        print(e)
                except ValueError as e:
                    print(e)

                
            case 2:
                try:
                    listaEmpregados = Reajusta_dez_porcento(listaEmpregados)
                    atualizarArquivo(listaEmpregados,"./empregados.txt")
                except ValueError as e:
                    print(e)
            case 3:
                try:
                    listarFuncionarios(listaEmpregados)
                except ValueError as e:
                    print(e)
            case 0:
                print("Saindo...")
                exit()
            case _:
                print("Opção inválida")
    
if __name__ == '__main__':
    main()