
lista_praias = {}
mais_15_km = 0
soma_media = 0
contador = 0
lista = []
while True:
    nome = input("Nome Praia: ")
    if nome == "":
        break
    dis_centro = int(input("Distancia em Km do Centro: "))
    media_veranista = int(input("Media Veranista ultima temporada: "))
    tipo_acesso = int(input("Tipo de acesso - 0-Não asfaltado / 1-Asfaltado: ")) 

    if tipo_acesso != 0 and tipo_acesso != 1:
        print("Selecionar 0 ou 1")
        tipo_acesso = input("Tipo de acesso - 0-Não asfaltado / 1-Asfaltado: ")
    
    lista_praias[nome] = {
        "Distancia": dis_centro,
        "TipoAcesso": tipo_acesso,
        "MediaVeranista": media_veranista
             }


for i in lista_praias.keys():
    #print(lista_praias)
    
    if lista_praias[i]["Distancia"] > 15:
        mais_15_km+= 1
    
    contador+= 1    
    if lista_praias[i]["TipoAcesso"] == 0:
        soma_media = soma_media + lista_praias[i]["MediaVeranista"]  

    if lista_praias[i]["TipoAcesso"] == 1 and lista_praias[i]["MediaVeranista"] < 1000:
        lista.append(i["Distancia"]) #tem que ser dicionario
        print(lista)
      

print(f"Praias com distancia maior do que 15km: ",mais_15_km)
print(f"Média Veranistas na ultima temporada de praias com acesso não asfaltado: ", (soma_media/contador))         

