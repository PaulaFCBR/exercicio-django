import os
ListaOp = {1:"Nova Tarefa [1]", 2:"Remover [2]",3:"Exibir tarefas [3]",4:"Sair [4]"}
lista_tarefas = {}
while(True):
    print("Selecione o comando pelo numero: ")
    for i in ListaOp:
        print(ListaOp[i])
    comando = int(input("> ")) 
    if comando == 1:
        tarefa = input("Entre o nome da tarefa (mínimo de 10 chars): ")
        while len(tarefa)<10:
            tarefa = input("O nome tem menos de 10 chars. Entre um nome com 10 ou mais chars: ")
        responsavel = input("Entre com o responsável: ")
        lista_tarefas[tarefa] = {"Responsável": responsavel}
        input("> Final de comando    ")
    elif comando == 2:
            del lista_tarefas[input("Excluir tarefa: ")] 
            print(lista_tarefas)
            input("> Final de comando    ")
    elif comando == 3:
                print(lista_tarefas)  
                input("> Final de comando    ")  
    elif comando == 4:
        break        
    os.system("cls")     
