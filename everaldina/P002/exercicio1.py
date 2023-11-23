def ordenar_tarefas(tarefa):
    return tarefa.endswith('[x]')

def listar_tarefas(lista):
    lista.sort(key=ordenar_tarefas)
    for tarefa in lista:
        if tarefa['finalizado']:
            print(f"[x] {tarefa['descricao']}")
            
def adicionar_tarefa(lista):
    descricao = input("Digite a descrição da tarefa: ")
    descricao = descricao.capitalize()
    
    if len(lista) == 0:
        id = 0
    else:
        id = lista[-1]['id'] + 1
        
    tarefa = str(id)+descricao+'[ ]'

    print(tarefa)
    lista.append(tarefa)
    print("Tarefa adicionada com sucesso!")
    
def main():
    lista = []
    

if __name__ == '__main__':
    main()