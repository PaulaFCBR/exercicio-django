lista_praias = []
mais_15_km = 0
while True:
    praia = input("Nome Praia: ")
    if praia == "":
        break
    dis_centro = int(input("Distancia em Km do Centro: "))
    media_veranista = int(input("Media Veranista ultima temporada: "))
    tipo_acesso = int(input("Tipo de acesso - 0-Não asfaltado / 1-Asfaltado: ")) 
    if tipo_acesso != 0 and tipo_acesso != 1:
        print("Selecionar 0 ou 1")
        tipo_acesso = input("Tipo de acesso - 0-Não asfaltado / 1-Asfaltado: ")
    praia = {
            "Nome":praia,
            "Distancia": dis_centro,
            "Tipo Acesso": tipo_acesso,
            "Media Veranista": media_veranista,
             }
    lista_praias.append(praia)    
for i in lista_praias:
    
        print(lista_praias[praia]["Nome"])
        print(int(lista_praias[praia]["Distancia"]))
        mais_15_km+= 1
print(mais_15_km)           
    