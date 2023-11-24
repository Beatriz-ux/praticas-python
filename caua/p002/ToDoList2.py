listaTarefas = []
fileName = "p002/ToDoList.txt"

with open(fileName) as file:
    listaTarefas = file.read().splitlines() 

acao = 1;
while(acao != 0):
    print("\n---Menu de Acoes do ToDoList---")
    print("1 - Registrar uma nova tarefa")
    print("2 - Listar todas as tarefas")
    print("3 - Marcar uma tarefa como concluida")
    print("4 - Editar uma tarefa")
    print("0 - Sair")
    acao = input("Digite uma opcao: ")
    acao = int(acao)

    print()
    match acao:
        case 0:
            print("---Finalizando operacao---\n")
        
        case 1:
            print("---Registrando uma nova tarefa---")
            descricao = input("Digite a descricao da tarefa: ").capitalize();
            novaTarefa = "{}.{} [ ]".format((len(listaTarefas) + 1), descricao)
            listaTarefas.append(novaTarefa);
            print("Tarefa registrada com sucesso!")
        
        case 2:
            print("--Lista de tarefas--")
            if len(listaTarefas) == 0:
                print("A lista de tarefas esta vazia")
                exit;

            for tarefa in listaTarefas:
                    print(tarefa);
        
        case 3:
            print("---Marcando uma tarefa---")   
            index = -1         
            check = False
            id = input("Digite o id da tarefa: ");
            for tarefa in listaTarefas:
                index+=1
                num = tarefa.split(".")[0]
                if num == id:
                    if tarefa[-3:] == "[x]":
                        print("Essa tarefa ja foi concluida")
                        check = True;
                    else:
                        listaTarefas[index] = tarefa.replace("[ ]", "[x]");
                        print("Tarefa concluida com sucesso!")
                        check = True;
                        
                        #Colocando a tarefa para o inicio
                        if index > 0:
                            listaAux = listaTarefas.copy()
                            listaTarefas[0] = listaTarefas[index]
                            for i in range(index):
                                listaTarefas[i+1] = listaAux[i]
                    break;
            
            if check == False:
                index = -1
                print("Id nao encontrado")

        case 4:
            print("---Editando uma tarefa---")
            index = -1
            check = False
            id = input("Digite o id da tarefa: ");
            for tarefa in listaTarefas:
                index += 1
                num = tarefa.split(".")[0]
                status = tarefa[-3:]
                if num == id:
                    descricao = input("Digite a nova descricao da tarefa: ").capitalize()
                    tarefa = "{}.{} {}".format(num, descricao, status)
                    listaTarefas[index] = tarefa
                    print("Tarefa editada com sucesso!")
                    check = True;
                    break;
            
            if check == False:
                print("Id nao encontrado")
        
        case _:
            print("--Erro--")
            print("Opcao invalida, digite um numero de 0 a 4")

file = open(fileName, "w");
file.close()

file = open(fileName, "a");
file.writelines(line + '\n' for line in listaTarefas)
file.close()
print("Arquivo salvo com sucesso!")