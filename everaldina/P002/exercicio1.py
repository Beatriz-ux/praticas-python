def listar_tarefas(lista):
    if len(lista) == 0:
        print("\nLista vazia!")
        return
    print(f"\n{'LISTA DE TAREFAS':-^30}")
    for tarefa in lista:
        if tarefa['finalizado']:
            print(str(tarefa['id']) + '. ' + tarefa['descricao'] + ' [x]')
        else:
            print(str(tarefa['id']) + '. ' + tarefa['descricao'] + ' [ ]')
            
# adiciona um item diciionário na lista
# dicionario composta por id (int), descrição(string) e finalizado(bool)
def adicionar_tarefa(lista):
    descricao = input("\nDigite a descrição da tarefa: ")
    descricao = descricao.capitalize()
    
    # id é zero se a lista estiver vazia, se não, o id é o último id + 1
    id = len(lista)+1
    
    # adiciona tarefa na lista
    tarefa = {'id': id, 'descricao': descricao, 'finalizado': False}
    lista.append(tarefa)
    print("Tarefa adicionada com sucesso!")

    
def concluir_tarefa(lista, id):
    if(id <= len(lista) and id > 0): # verifica se o id existe na lista
        if(lista[id-1]['finalizado']):
            return
        else:
            lista[id-1]['finalizado'] = True
            lista.insert(0, lista.pop(id-1)) # move o item para o topo da lista
            print("\nTarefa concluída com sucesso!")
    else:
        print("\nTarefa não encontrada!")
  
      
def editar_tarefa(lista, id):
    if(id <= len(lista) and id > 0):
        descricao = input("Digite a nova descrição da tarefa: ")
        descricao = descricao.capitalize()
        lista[id-1]['descricao'] = descricao
        print("\nTarefa editada com sucesso!")
    else:
        print("\nTarefa não encontrada!")

   
def main():
    lista = []
    while True:
        print("1 - Listar tarefas")
        print("2 - Adicionar tarefa")
        print("3 - Concluir tarefa")
        print("4 - Editar tarefa")
        print("0 - Sair")
        try:
            opcao = int(input("Digite uma opção: "))
        except ValueError:
            opcao = -1
            continue
        
        # menu
        match opcao:
            case 1:
                listar_tarefas(lista)
            case 2:
                adicionar_tarefa(lista)
            case 3:
                id = int(input("\nDigite o id da tarefa: "))
                concluir_tarefa(lista, id)
            case 4:
                id = int(input("\nDigite o id da tarefa: "))
                editar_tarefa(lista, id)
            case 0:
                break
            case _default:
                print("Opção inválida!")
        print()
    

if __name__ == '__main__':
    main()