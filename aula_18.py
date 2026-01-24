class Tarefa:

    def __init__ (self, categoria: str, descricao: str, urgencia: str, diasRestantes: int):
        self.categoria = categoria
        self.descricao = descricao
        self.urgencia = urgencia
        self.diasRestantes = diasRestantes
        self.status = "Pendente"

    
    def __str__ (self):
        return f'{self.descricao} - {self.categoria} - {self.status}'



class Gerenciador:
    def __init__(self):
        self.listaTarefas = [
            Tarefa('casa', 'arrumar o quarto', 'leve', 2),
            Tarefa('casa', 'jogar o lixo', 'Moderado', 1),
            Tarefa('estudo', 'estudo POO', 'MUITO urgente', 1)]
            
        

    def criarTarefa(self):
        print(f'{'-'*10}Criando Tarefa{'-'*10}')
        categoria = input ('Categoria: ')
        descricao = input('Descricao: ')
        try:
            diasRestantes = int(input("Dias Restantes: "))
            urgencia = input('Urgencia')

            novaTarefa = Tarefa(categoria=categoria, descricao=descricao, urgencia=urgencia, diasRestantes=diasRestantes)
            self.listaTarefas.append(novaTarefa)
            print('Tarefa criado com Sucesso!')
        except ValueError:
            print("Erro do tipo de dado de cadastro")



    def listarTarefas(self):
        if not self.listaTarefas:
            print("Lista vazia")
        else:
            for i, tarefa in enumerate(self.listaTarefas, 1):
                print(f'Tarefa{i}: {tarefa}')


    def atualizarTarefa(self):
        self.listarTarefas()
        if self.listaTarefas:
            try:
                indice = int(input('indice da tarefa:'))
                indice -= 1
                novostatus = input('Novo Status:')
                if 0<= indice < len(self.listaTarefas):
                    self.listaTarefas[indice].status = novostatus
                else:
                    print("Indice Inválido")
            except ValueError:
                print('Digite um numero inteiro')


    def deletarTarefa(self):
        self.listarTarefas()
        if self.listaTarefas:
            try:
                indice = int(input("Indice de Tarefas"))
                indice -= 1
                if 0 <= indice < len(self.listaTarefas):
                    removido = self.listaTarefas.pop(indice)
                    print(f'Tarefa Removida: {removido.descrição}')
                else:
                    print("Indice Inválido")
            except ValueError:
                print("Digite um numero inteiro")

sistema = Gerenciador()
while True:
    print(f"\n{'='*20}\nSISTEMA GERENCIADOR DE TAREFAS\n{'='*20}\n")
    print('1 - Criar Tarefa\n2 - Listar Tarefas\n3 - Atualizar Tarefas\n4 - Delefar Tarefa\n5 - Sair')
    opcao = input('n\Escolha uma opcao: ')
    match(opcao):
        case '1':
            sistema.criarTarefa()
        case '2':
            sistema.listarTarefas()
        case '3':
            sistema.atualizarTarefa()
        case '4':
            sistema.deletarTarefa()
        case '5':
            print('Saindo do sistema..')
            break
        case _:
            print('Opção Inválida')