Produtos ={}

while True:
    prod = input("Nome produto: ")
    if prod == "0":
        break
    valor_prod = input("Entre valor: ")
    lote_prod = input("Entre o lote: ")
    qtd_prod = input("Entre a quantidade: ")
    categoria_prod = input("Categoria: ")
    Produtos[prod] = {prod: {"Valor":valor_prod, "Lote":lote_prod, "Quantidade":qtd_prod,
                                  "Categoria":categoria_prod}}
for i in list( Produtos.keys()):
    print(i)


