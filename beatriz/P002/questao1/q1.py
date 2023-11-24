def buscarTarefa(listaDeTarefas, id):
    posicao = 0
    for cod in listaDeTarefas:
        if int(cod.split("-")[0]) == id:
            return posicao
        posicao = posicao + 1
    return -1
def limpaTela():
    print("\n" * 100)
