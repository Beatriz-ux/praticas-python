class Tarefa:
    def __init__(self, descricao, id):
        self.descricao = descricao
        self.id = id
        self.status = 0
    
    def editarTarefa(self, descricao):
        self.descricao = descricao;
        print("Edicao feita com sucesso!");

    def concluirTarefa(self):
        self.status = True;
        print("Tarefa concluida com sucesso!")

    def getDescricao(self):
        return self.descricao;

    def getId(self):
        return self.id;

    def getStatus(self):
        return self.status;
    
    def visualizarTarefa(self):
        print("{}. {} [{}]".format(self.id, self.descricao, ("x" if self.status == True else " ")))


class ListaTarefas:
    def __init__(self):
        self.tarefas = [Tarefa];
    
    def criarTarefa(self):
        descricao = input("Digite a descricao da tarefa: ");
        novaTarefa = Tarefa(descricao, (len(self.tarefas) + 1));
        self.tarefas.append(novaTarefa)
        print("Tarefa criada com sucesso!")

    def listarTarefas(self):
        for tarefa in self.tarefas:
            if tarefa.getStatus(self) == True:
                tarefa.visualizarTarefa();
        for tarefa in self.tarefas:
            if tarefa.getStatus() == False:
                tarefa.visualizarTarefa();

    def concluirTarefa(self):
        id = input("Digite o id da tarefa: ");
        for tarefa in self.tarefas:
            if tarefa.getId() == id:
                if tarefa.getStatus == True:
                    print("Essa tarefa ja foi concluida")
                else:
                    tarefa.concluirTarefa();
                    return;
        print("Id nao encontrado, digite novamente")

    def editarTarefa(self):
        id = input("Digite o id da tarefa: ");
        check = False;

        for tarefa in self.tarefas:
            if tarefa.getId() == id:
                check = True;
                exit;
        
        if check == False:
            print("Id nao encontrado, digite novamente")
            return;
    
        descricao = input("Digite a nova descricao da tarefa: ");
        tarefa.editarTarefa(descricao)

lista = ListaTarefas()
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

    match acao:
        case 0:
            print("Finalizando operacao...")
        case 1:
            lista.criarTarefa()
        case 2:
            lista.listarTarefas()
        case 3:
            lista.concluirTarefa()
        case 4:
            lista.editarTarefa()
        

    