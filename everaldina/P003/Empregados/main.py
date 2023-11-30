import json

# reajusta o salário de todos os empregados em 10%
def reajusta_dez_porcento(empregados):
    for e in empregados:
        e['salario'] = e['salario'] * 1.1

# carrega os empregados do arquivo empregados.json em uma lista de dicionários
def carrega_empregados():
    lista = []
    try:
        with open("empregados.json", "r") as arquivo:
            for linha in arquivo:
                e = json.loads(linha)
                lista.append(e)
    except FileNotFoundError:
        pass
    return lista

# salva os empregados no arquivo empregados.json
def salva_empregados(empregados): 
    with open("empregados.json", "w") as arquivo:
        for e in empregados:
            json.dump(e, arquivo)
            arquivo.write("\n")

# imprime os empregados da lista
def imprime_empregados(empregados):
    for e in empregados:
        print("Nome: " + e['nome'] + ' ' + e['sobrenome'] +" | RG: " + e['rg'])
        print(" - Ano de Nascimento: " + str(e['ano_nascimento']))
        print(" - Salário: R$" + "{:.2f}".format(e["salario"]))
        print(" - Ano de Admissão: " + str(e['ano_admissao']))
        print()

def main():
    empregados = carrega_empregados()
    
    print("Antes do reajuste:")
    imprime_empregados(empregados)
    
    reajusta_dez_porcento(empregados)
    print("Depois do reajuste:")
    imprime_empregados(empregados)
    
    salva_empregados(empregados)
    

if __name__ == "__main__":
    main()