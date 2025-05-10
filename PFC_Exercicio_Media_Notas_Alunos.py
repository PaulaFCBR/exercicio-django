#def MediaAlunos (x):
lista_alunos = {"Paula": {"Nota":9},"Ana":{"Nota":6}, "Joao":{"Nota":6},
                    "Julia":{"Nota":4}, "Maria":{"Nota":3}}
soma_notas = 0
for i in lista_alunos:
    print(lista_alunos[i])
    soma_notas = (int(lista_alunos[i]["Nota"] + soma_notas))
    #print(soma_notas)
print ("Media da Turma",soma_notas/5)    
