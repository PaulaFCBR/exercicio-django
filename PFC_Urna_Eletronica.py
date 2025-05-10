#urna eletrônica
opcoes = {1:"Confirmar [1]", 2:"Corrigir [2]", 3:"Cancelar [3]", 4:"Encerrar"}
votos_branco = 0
votos_validos = 0
votos_nulos = 0
candidatos = {10:{"Nome":"André", "Partido":"PSS", "Votos": 0},
               15:{"Nome":"Paula", "Partido":"PWQ", "Votos": 0},
               25:{"Nome":"Carlos", "Partido":"PTC", "Votos": 0}
              }
votar = ["Confirmar", "Corrigir", "Cancelar", "Encerrar"]

while True:
    voto = int(input("Informe seu voto: "))
    if voto == 0:
        votos_branco+=1
        print("Voto em branco")
    else:
        if voto in list(candidatos.keys()):
            print(voto)
            print(candidatos[voto]["Nome"])
            print(candidatos[voto]["Partido"])
            print("Confirmar [1] / Corrigir [2] / Cancelar [3] / Encerrar [4]")
            votos_maior = 0 
            opcao = int(input("Selecione uma opção: "))
            if opcao == 1: ## confirma
                votos_validos+=1
                print("voto confirmado")
                candidatos[voto]["Votos"]+=1
                
            elif opcao == 2 or opcao == 3: #corrigir/cancelar
                voto = int(input("Informe seu voto: "))
                print(voto)
                print(candidatos[voto]["Nome"])
                print(candidatos[voto]["Partido"])
                print("Confirmar [1] / Corrigir [2] / Cancelar [3] / Encerrar [4]")
                if opcao == 3:
                    votos_nulos+= 1
                    print("Voto nulo")
            elif opcao == 4: #encerrar votação
                break                                
#print(candidatos)
print("Total de votos:",votos_branco + votos_nulos + votos_validos)
print("Votos válidos: ", votos_validos)
print("Votos em branco: ", votos_branco)
print("Votos nulos: ", votos_nulos)
for i in candidatos:
    if candidatos[voto]["Votos"] > votos_maior:
        votos_maior = i
        votos_maior = candidatos[voto]["Votos"] 
vencedor = candidatos[voto]["Nome"]
votos_vencedor = candidatos[voto]["Votos"]
print(f"Vencedor: {vencedor} - Votos: {votos_vencedor}")
            


