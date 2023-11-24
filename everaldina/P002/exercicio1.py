import json

def buscar_tarefa(lista, id):
    for index, tarefa in enumerate(lista):
        if tarefa['id'] == id:
            return index
    return None

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
    indice = buscar_tarefa(lista, id)
    if(indice is not None): # verifica se o id existe na lista
        if(lista[indice]['finalizado']):
            return
        else:
            lista[indice]['finalizado'] = True
            lista.insert(0, lista.pop(indice)) # move o item para o topo da lista
            print("\nTarefa concluída com sucesso!")
    else:
        print("\nTarefa não encontrada!")
  
      
def editar_tarefa(lista, id):
    indice = buscar_tarefa(lista, id)
    if(indice is not None):
        descricao = input("Digite a nova descrição da tarefa: ")
        descricao = descricao.capitalize()
        lista[indice]['descricao'] = descricao
        print("\nTarefa editada com sucesso!")
    else:
        print("\nTarefa não encontrada!")

def salvar_tarefas(lista):
    with open("tarefas.json", "w") as arquivo:
        for tarefa in lista:
            json.dump(tarefa, arquivo)
            arquivo.write("\n")

def carregar_tarefas():
    lista = []
    try:
        with open("tarefas.json", "r") as arquivo:
            for linha in arquivo:
                tarefa = json.loads(linha)
                lista.append(tarefa)
    except FileNotFoundError:
        pass
    return lista
   
def main():
    lista = carregar_tarefas()
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
                salvar_tarefas(lista)
                break
            case _default:
                print("Opção inválida!")
        print()
    
    

if __name__ == '__main__':
    main()