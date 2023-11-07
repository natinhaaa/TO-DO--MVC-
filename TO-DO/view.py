from controller import *
import os

sair = 0
while sair == 0:

    os.system("cls")
    print("SOFTWARE TO-DO DE TAREFAS")
    print("1 - Adicionar tarefa\n2 - Listar tarefas\n3 - Alterar tarefa\n4 - Concluir tarefa\n5 - Listar tarefas concluídas\n6 - Excluir tarefas\n7 - Sair")
    
    opcao = input("Digite a opção desejada.\n-> ")

    match opcao:

        case "1":
            os.system("cls")
            print("~~~~ Adicionar tarefa ~~~~\n")
            tarefa = input("Digite a tarefa -> ")
            adicionarnova = ControllerAdicionarTarefa(tarefa)
            os.system("pause")

        case "2":
            os.system("cls")
            print("~~~~ Lista de tarefas ~~~~\n")
            listarTarefa = ControllerListarTarefa()
            os.system("pause")

        case "3":
            os.system("cls")
            print("~~~~ Alterar tarefa ~~~~\n")
            listarTarefa = ControllerListarTarefa()
            indice = (input("Qual número da tarefa que deseja alterar? "))
            novaDescricao = input("Qual a nova descrição da tarefa? ")
            alterarTarefa = ControllerAlterarTarefa(indice, novaDescricao)
            os.system("pause")
            
        case "4":
            os.system("cls")
            print("~~~~ Concluir tarefa ~~~~\n")
            listarTarefa = ControllerListarTarefa()
            indice = (input("Qual o número da tarefa que deseja concluir? "))
            concluir = ControllerConcluirTarefa(indice)
            os.system("pause")

        case "5":
            os.system("cls")
            print("~~~~ Lista de tarefas concluídas ~~~~\n")
            concluidas = ControllerListarTarefaC()
            os.system("pause")

        case "6":
            os.system("cls")
            print("~~~~ Excluir tarefa ~~~~\n")
            listarTarefa = ControllerListarTarefa()
            indice = (input("Digite o número da tarefa que deseja excluir -> "))
            excluirTarefa = ControllerExcluirTarefa(indice)
            os.system("pause")

        case "7":
            os.system("cls")
            sair = 1

        case _:
            os.system("cls")
            print("Opção inválida")