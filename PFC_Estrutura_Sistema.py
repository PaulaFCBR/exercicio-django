opcoes = ["CADASTRAR","CONSULTAR","ATUALIZAR", "REMOVER", "SAIR"]
Escol =  ["Cadastrar","Consultar","Atualizar","Remover","Sair"]
lista_carros = {'Fusca': {'Marca': 'VW', 'Ano': 1966, 'Preço': 47465.9}}
Contador = 0
while(True):
    opcao_usuario = input("O que deseja fazer? (Cadastrar/Consultar/Sair) ")
    OpcaoInvalida = 0
    if opcao_usuario.upper() == "SAIR":
        break
    for x in opcoes:
        # print("entrou no for")
        if x == opcao_usuario.upper():
            if x == "CADASTRAR":
                modelo = input("Entre o modelo: ")
                marca = input("Entre a marca do carro: ")
                ano = int(input("Entre o ano do carro: "))
                preco = float(input("Entre a preço: "))
                lista_carros.update({modelo:{"Marca":marca, "Ano":ano,"Preço":preco}})
                print(lista_carros)
            elif x == "CONSULTAR":
                consulta = input("Modelo do carro: ")
                #print(consulta)
                lista_carros[consulta]
               # print("Modelo: ", lista_carros[consulta])
                print ("Marca: ", lista_carros [consulta]["Marca"])
                print("Ano: ",lista_carros[consulta]["Ano"])
                print ("Preço: ", lista_carros[consulta]["Preço"])
                #print(lista_carros[consulta]
                # print(Contador)
                op = input("O que deseja fazer (Atualizar/Remover/Sair): ")
                print(op)
                if op == "ATUALIZAR":                   
                        modelo = input("Modelo do carro: ")
                        alterar = input("Qual campo deseja alterar? Marca/Ano/Preço " )
                        print(alterar)
                        lista_carros[modelo][alterar] = input("Entre o novo valor: ")
                        lista_carros.update(alterar)
                        print(lista_carros.update(alterar))
                    OpcaoInvalida = 0
            if Contador > len(Escol):
                Contador-=1
            print(Escol[Contador])
            break
        else: 
            OpcaoInvalida = 1
        Contador+=1
    if OpcaoInvalida ==1:
        print("Você escolheu uma opcao invalida")
    Contador =0
