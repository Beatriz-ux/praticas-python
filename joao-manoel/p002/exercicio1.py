def main():
    tarefas = []
    id = 1

    while True:
        print("===== Menu =====")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Marcar tarefa como realizada")
        print("4. Editar tarefa")  
        print("5. Sair")

        opcao = int(input('\nDigite a opção desejada: '))

        if opcao == 1:
            print('\nTarefas:')
            for tarefa in tarefas:
                print(f'{tarefa["id"]}. {tarefa["tarefa"]} {tarefa["status"]}')

        elif opcao == 2:
            tarefa = input('\nDigite a tarefa: ')
            tarefa = tarefa.capitalize()
            tarefa = {'id': id, 'tarefa': tarefa, 'status': '[ ]'}
            id += 1
            tarefas.append(tarefa)
            print('\nTarefa registrada!!!')

        elif opcao == 3:
            tarefaId = int(input('\nDigite o ID da tarefa: '))
            
            for tarefa in tarefas:
                if tarefaId == tarefa['id']:
                    tarefa['status'] = '[x]'
                    print('\nTarefa realizada!!!')
                    break

        elif opcao == 4:
            tarefaId = int(input('\nDigite o ID da tarefa: '))
            
            for tarefa in tarefas:
                if tarefaId == tarefa['id']:
                    tarefa['tarefa'] = input('Digite a nova tarefa: ').capitalize()
                    print('\nTarefa editada!!!')
                    break

        elif opcao == 5:
            break

        else:
            print('\nOpção inválida!!!')

        tarefas.sort(key=lambda tarefa: tarefa['id'])
        tarefas.sort(key=lambda tarefa: tarefa['status'], reverse=True)

        print()


if __name__ == '__main__':
    main()