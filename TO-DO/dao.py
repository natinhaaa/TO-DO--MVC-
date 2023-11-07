banco_de_dados = "tarefas.txt"

class DaoAdicionarTarefa:
    def __init__(self, tarefa):
        self.tarefa = tarefa

    def AdicionarTarefa(self):
        with open(banco_de_dados, "a") as arquivo:
            arquivo.write(self.tarefa)
        return True


class DaoListarTarefa:
    def ListarTarefas(self):
        with open(banco_de_dados, "r") as arquivo:
            linhas = arquivo.readlines()
        return linhas


class DaoAlterarTarefa:
    def AlterarTarefa(self, tarefas, tarefaAtualizada):
        with open(banco_de_dados, "r") as arquivo:
            ToDo = arquivo.read()

        atualização = ToDo.replace(tarefas, tarefaAtualizada)
        with open(banco_de_dados, "w") as arquivocópia:
            arquivocópia.write(atualização)
        return True

