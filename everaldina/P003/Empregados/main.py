import json

def reajusta_dez_porcento(empregados):
    pass

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

def salva_empregados(empregados):
    with open("empregados.json", "w") as arquivo:
        for e in empregados:
            empregados.dump(e, arquivo)
            arquivo.write("\n")

def imprime_empregados(empregados):
    pass

def main():
    pass

if __name__ == "__main__":
    main()