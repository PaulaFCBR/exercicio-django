atletas = []
while True:
    nome = input("Nome do atleta: ")
    if nome == "":
        break
    atleta = {
        "nome": nome,
        "saltos": [],
        "media": 0,
        "melhor_salto": 0,
        "pior_salto": 0,
    }
    #entrar com cada salto (5 saltos por atleta)
    for i in range(5):
            atleta.get("saltos").append(
            float(input(f"Distância do {i+1}º salto: "))
        )
    atleta.get("saltos").sort()  #ordena os saltos conforme as distâncias
    atleta["pior_salto"] = atleta.get("saltos").pop(0)
    atleta["melhor_salto"] = atleta.get("saltos").pop()
    atleta["media"] = sum(atleta.get("saltos")) / 3

    #print informaçoes dos saltos e do atleta
    print(
        f"\nMelhor salto: {atleta.get('melhor_salto'):.2f} m"
        f"\nPior salto: {atleta.get('pior_salto'):.2f} m"
        f"\nMédia dos demais saltos: {atleta.get('media'):.2f} m\n"
    )
    atletas.append(atleta)

print("\n\nResultado final")
for atleta in atletas:
    print(f"{atleta.get('nome')}: {atleta.get('media'):.1f} m")
