import os
from funcs.Rotinas import Cadastrar_Prod, Modificar_dado, Remover_Prod, Consulta_Lote, Relatorio_prod
from pyfiglet import Figlet
from colorama import Fore, Back, Style
f = Figlet(font='slant')
print(f.renderText('Sis Dados'))

ListaOp = {1:"Cadastrar Produto [1]",2:"Modificar Produto [2]",
              3:"Excluir produto [3]",4:"Consulta em Lote [4]",5:"Relatório [5]",6:"Sair [6]"}
print("Sistema de Gerenciamento de Dados")
Nome_User = input("Qual o seu nome? ")
os.system("cls")
print(f"Seja Bem vindo(a) {Nome_User}")
Produtos = {'Caderno': {'Preço': '10', 'Quantidade': '100', 'Marca': 'cc', 'Lote': 'xx'}, 'Lapis': {'Preço': '44', 'Quantidade': '300', 'Marca': 'ww', 'Lote': 'cc'}, 'Caneta': {'Preço': '22', 'Quantidade': '222', 'Marca': 'xx', 'Lote': 'cc'}}
while True:
    print("Selecione o comando pelo numero: ")
    for i in ListaOp:
        print(ListaOp[i])
    comando = int(input("> ")) 
    if comando == 1:
        Cadastrar_Prod(Produtos)
        print(Produtos)
        input("> Final de comando    ")
    elif comando == 2:
        Modificar_dado(Produtos)
        print(Produtos)
        input("> Final de comando    ")
    elif comando == 3:
        Remover_Prod(Produtos)
        print(Produtos)
        input("> Final de comando    ")
    elif comando == 4:
        categoria = input("Buscar por qual categoria: ")
        valor_lote = input("Qual valor deseja buscar: ")
        Consulta_Lote(Produtos,categoria, valor_lote)
        input("> Final de comando    ")
    elif comando == 5:
        Relatorio_prod(Produtos)
        input("> Final de comando    ")
    elif comando == 6:
        break
    os.system("cls")   
