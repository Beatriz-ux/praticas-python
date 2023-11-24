import os 
def buscarTarefa(listaDeTarefas, id):
    posicao = 0
    for cod in listaDeTarefas:
        if int(cod.split("-")[0]) == id:
            return posicao
        posicao = posicao + 1
    return -1

def limpaTela():
    print("\n" * 100)




nome_arquivo = './beatriz/P002/questao2/arquivo.txt'

if not os.path.exists(nome_arquivo):
    # Verifica se o diretório existe, se não, cria o diretório
    diretorio = os.path.dirname(nome_arquivo)
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    # Cria o arquivo vazio
    with open(nome_arquivo, 'w') as arquivo:
        pass  # Arquivo criado, mas vazio

# Restante do seu código para ler as linhas do arquivo
id = 0
listaDeTarefas = []

with open(nome_arquivo, 'r') as arquivo:
    listaDeTarefas = [linha.strip() for linha in arquivo.readlines()]

if len(listaDeTarefas) > 0:
    id = int(listaDeTarefas[-1].split("-")[0]) #pega o id da ultima tarefa

while True:
    print("----------------------------------------------------------------------------------")
    print("1- Adicionar | 2- Listar | 3- Remover | 4- Concluir | 5- Editar | 6- Salvar | 0- Sair")
    print("----------------------------------------------------------------------------------")
    opcao = int(input())

    match opcao:
        case 1:
            id = id + 1
            frase=(input("Digite a tarefa: "))
            frase=frase.strip() #remove espaços em branco no inicio e no fim 

            tarefa = str(id) + " - " + frase.capitalize() + " []"
            listaDeTarefas.append(tarefa)
        case 2:
            for i in listaDeTarefas:
                print(i)
        case 3:
            print("Qual o id da tarefa que deseja remover?")
            idRemover = int(input())
            position = buscarTarefa(listaDeTarefas, idRemover)
            if position == -1:
                print("Tarefa não encontrada")
            else:
                print("Removendo tarefa: " + listaDeTarefas[position])
                listaDeTarefas.pop(position)

        case 4:
            print("Qual o id da tarefa que deseja concluir?")
            idConcluir = int(input())
            position = buscarTarefa(listaDeTarefas, idConcluir)
            if position == -1:
                print("Tarefa não encontrada")
            else:
                listaDeTarefas[position] = listaDeTarefas[position].replace("[]", "[x]")
                print("Concluindo tarefa: " + listaDeTarefas[position])
                listaDeTarefas.insert(0, listaDeTarefas[position])
                listaDeTarefas.pop(position+1) #remove a tarefa da posição antiga
        case 5:
            print("Qual o id da tarefa que deseja editar?")
            idEditar = int(input())
            position = buscarTarefa(listaDeTarefas, idEditar)
            if position == -1:
                print("Tarefa não encontrada")
            elif listaDeTarefas[position].find("[x]") == -1: 
                print("Editando tarefa: " + listaDeTarefas[position])
                print("Correção: ",end="")
                frase=input()
                frase=frase.strip() #remove espaços em branco no inicio e no fim
                tarefa = str(idEditar) + " - " + frase.capitalize() + " []"
                listaDeTarefas[position] = tarefa
            else:
                print("Tarefa já concluída, não pode ser editada")
        case 6:
            with open(nome_arquivo, 'w') as arquivo:
                for linha in listaDeTarefas:
                    arquivo.write(linha + '\n')
            print("Arquivo salvo com sucesso!")
        case 0:
            print("Saindo...")
            with open(nome_arquivo, 'w') as arquivo:
                for linha in listaDeTarefas:
                    arquivo.write(linha + '\n')
            break
        case _:
            print("Opção inválida")

    input("Pressione enter para continuar...")
    limpaTela()


