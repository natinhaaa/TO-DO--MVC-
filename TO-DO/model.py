from dao import *

class ToDo:

    def AdicionarTarefas(self, tarefa):
        DAO = DaoAdicionarTarefa(tarefa)
        return DAO.AdicionarTarefa()

    def ListarTarefa(self):
        DAO = DaoListarTarefa()
        return DAO.ListarTarefas()

    def AlterarTarefa(self, tarefas, tarefaAtualizada):
        DAO = DaoAlterarTarefa()
        return DAO.AlterarTarefa(tarefas, tarefaAtualizada)

TODO = ToDo()