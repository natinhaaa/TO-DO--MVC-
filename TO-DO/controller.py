from model import *
import random

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class ControllerAdicionarTarefa:

    def __init__(self, tarefa):
        #aqui utilizamos o método randint da biblioteca que importamos "random", para sortear um número aleatório de 4 digitos, ou seja, entre 1000 e 9999
        idtarefa = str(random.randint(1000,9999))
        statusA = "A"
        tamanholista = len(TODO.ListarTarefa())

        try:

            #confere se a lista de tarefas está vazia
            #será utilizado apenas uma vez, já que nesta parte é adicionada o cabeçalho
            if tamanholista == 0:

                if tarefa == "":
                    print("Tarefa inválida.")

                else:
                    adicionar = (f"STATUS\tID\tTAREFA\n") + (f"{statusA}\t{idtarefa}\t{tarefa}\n")

                    if TODO.AdicionarTarefas(adicionar) == True:
                        print("Tarefa adicionada!")

                    else:
                        print("Ocorreu algum erro.")
            
            #se houver itens dentro da lista
            else:

                for itens in TODO.ListarTarefa():
                    separacao = itens.split("\t", 3)
                    id_separado = separacao[1]

                    if idtarefa == id_separado:
                        idtarefa = random.randint(1000,9999)
                    
                    else:

                        if tarefa == "":
                            print("Tarefa inválida.")
                            break

                        else:
                            adicionar = f"{statusA}\t{idtarefa}\t{tarefa}\n"

                            if TODO.AdicionarTarefas(adicionar) == True:
                                print("Tarefa adicionada!")
                                break
                            
                            else:
                                print("Ocorreu algum erro.")
                                break

        except Exception as erro:
            print(erro)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ControllerListarTarefa:
    def __init__(self):
        statusA = "A"
        cont = 0

        try:

            for tarefas in TODO.ListarTarefa():
                cont += 1

                if cont > 0:
                    status_separado = tarefas[0]

                    #comparamos o status para listarmos apenas as tarefas que estejam ativas! possuam um indice "A"
                    if status_separado == statusA:
                        tarefas = tarefas[7:]
                        print(f"{cont}- {tarefas}")

                    else:
                        cont -= 1

        except Exception as erro:
            print(erro)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ControllerExcluirTarefa:
    def __init__(self, indice):
        statusA = "A"
        statusE = "E"
        listaids = []
        cont = 0

        try:
            indice = int(indice)

            if indice == str:
                print("Indice inválido, tente novamente.")
            
            elif indice <= 0:
                print("Indice inválido, tente novamente.")

            else:
                for tarefas in TODO.ListarTarefa():
                    cont += 1

                    if cont > 0:
                        status_separado = tarefas[0]

                        if status_separado == statusA:
                            separacao = tarefas.split("\t", 3)               
                            id_separado = int(separacao[1])
                            listaids.append(id_separado)

                
                if indice <= len(listaids):
                    indice -=1
                    cont = -1

                    for tarefas in TODO.ListarTarefa():
                        cont += 1

                        if cont > 0:
                            separacao = tarefas.split("\t", 3)               
                            id_separado = int(separacao[1])

                            descTarefa = tarefas[7:]

                            #aqui irá comparar o id correspondente ao indice solicitado pelo usuario com os ids dentro da lista de tarefas, até encontrar uma correspondencia
                            if id_separado == listaids[indice]:
                                # print(listaids[indice])  #teste

                                tarefaAlterada = (f"{statusE}\t{id_separado}\t{descTarefa}")
                                if TODO.AlterarTarefa(tarefas, tarefaAlterada) == True:
                                    print("Tarefa excluída.")
                                    break
                else:
                    print("Indice inválido, tente novamente.")

        except Exception as erro:
            print(erro)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ControllerAlterarTarefa:
    def __init__(self, indice, novaDescricao):
        statusA = "A"
        listaids = []
        cont = 0

        try:
            indice = int(indice)

            if novaDescricao == "":
                print("Tarefa inválida.")
            
            elif indice <= 0:
                print("Indice inválido, tente novamente.")

            else:
                for tarefas in TODO.ListarTarefa():
                    cont += 1

                    if cont > 0:
                        status_separado = tarefas[0]

                        if status_separado == statusA:
                            separacao = tarefas.split("\t", 3)               
                            id_separado = int(separacao[1])
                            listaids.append(id_separado)
                
                #aqui será analisado se o indice que o usuario deseja excluir é menor ou igual às tarefas que são ativas presentes na lista
                #se o indice for maior, por exemplo, é porque o usuario digitou uma tarefa que não há na lista
                #ex: indice = 5 e o numero de itens dentro da lista seja 3, é impossivel ter um item de indice 5 presente na lista, ja que o numero maximo de tarefas é 3
                if indice <= len(listaids):

                    #aqui diminuimos -1 no indice pois, ao contarmos os itens na lista (sempre começa no 0, então: 0,1,2,3...), o indice selecionado pelo usuario será sempre ele -1 (dentro da lista)
                    indice -=1
                    cont = -1

                    # print(indice)  #testes
                    # print(listaids)

                    for tarefas in TODO.ListarTarefa():
                        cont += 1
                        if cont > 0:
                            separacao = tarefas.split("\t", 3)               
                            id_separado = int(separacao[1])

                            if id_separado == listaids[indice]:

                                if statusA == "A":
                                    tarefaAlterada = (f"{statusA}\t{id_separado}\t{novaDescricao}\n")

                                    #irá sobrescrever todo o documento, com as tarefas que já existem e alterar uma nova
                                    if TODO.AlterarTarefa(tarefas, tarefaAlterada) == True:
                                        print("Tarefa alterada.")
                                        break

                                    else:
                                        print("Ocorreu algum erro.")

                                else:
                                    break
                else:
                    print("Indice inválido, tente novamente.")

        except Exception as erro:
            print(erro)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ControllerListarTarefaC:
    def __init__(self):
        statusC = "C"
        cont = 0

        try:
            for tarefas in TODO.ListarTarefa():
                cont += 1

                if cont > 0:
                    status_separado = tarefas[0]

                    #comparamos o status para listarmos apenas as tarefas que estejam ativas! possuam um indice "A"
                    if status_separado == statusC:
                        tarefas = tarefas[7:]
                        print(f"[✔] {tarefas}")

                    else:
                        cont -= 1

        except Exception as erro:
            print(erro)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ControllerConcluirTarefa:
    def __init__(self, indice):
        statusA = "A"
        statusC = "C"
        listaids = []
        cont = -1

        try:
            indice = int(indice)

            if indice <= 0:
                print("Indice inválido, tente novamente.")

            else:
                for tarefas in TODO.ListarTarefa():
                    cont += 1
                    if cont >= 1:
                        status_separado = tarefas[:1]
                        if status_separado == statusA:
                            separacao = tarefas.split("\t", 4)               
                            id_separado = int(separacao[1])
                            listaids.append(id_separado)

                if indice <= len(listaids):
                    indice -=1
                    cont = -1

                    for tarefas in TODO.ListarTarefa():
                        cont += 1

                        if cont >= 1:
                            separacao = tarefas.split("\t", 4)               
                            id_separado = int(separacao[1])
                            descTarefa = tarefas[7:]
                            if id_separado == listaids[indice]:
                                tarefaConcluida = (f"{statusC}\t{id_separado}\t{descTarefa}")
                                if TODO.AlterarTarefa(tarefas, tarefaConcluida) == True:
                                    print("Tarefa marcada como concluída.")
                                    break
                else:
                    print("Tarefa inválida.")

        except Exception as erro:
            print(erro)