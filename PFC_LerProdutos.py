#menu com opções
ops = ["1", "2", "SAIR"]
while(True):
    op_user = input("O que deseja fazer?: ")
    if op_user == "1":
        print("Escolheu 1")
    elif op_user == "2":
        print("Escolheu 2")
    elif op_user.upper() == "SAIR":
        print("Escolheu SAIR")
        break
    else: print("Opção inválida")

        

    