import pandas as pd
from datetime import datetime
import os

op = 0

estoque_df = pd.read_excel("CtrlEstoque.xlsx")
relatorio_df = pd.read_excel("RelatorioEstoque.xlsx")

def RelEstoque():
    print("\n\n         Estoque\n\n")
    print(estoque_df)

def RelReservas():
    print("\n\n         Reservas\n\n")
    print(relatorio_df)


#FUNCIONANDO CARAIO
def AddEstoque():
    print("     Adicionar estoque\n\n")
    estoque_df = pd.read_excel("CtrlEstoque.xlsx")
    relatorio_df = pd.read_excel("RelatorioEstoque.xlsx")
    cad_ok = 'N'

    tecnico = input("Digite sua DRT: ")

    while cad_ok != 'S':
        usuario = "Entrada"
        idItem = input("Informe o ID do item: ")
        qtdEntrada = input("Informe a qtd adicionada: ")
        dataEntrada = datetime.now().strftime("%d/%m/%Y")
        nomeItem = estoque_df.loc[estoque_df['ID'] == int(idItem), 'Item'].iloc[0]
        cad_ok = input(f"Você deseja adicionar {qtdEntrada} '{nomeItem}' para o estoque? (S/N)")

    qtdEstoque = estoque_df.loc[estoque_df['ID']==int(idItem), 'Qtd']
    qtdEstoque = qtdEstoque.item()  

    #entrada no estoque
    qtdEstoque += int(qtdEntrada)
    estoque_df.loc[estoque_df['ID']==int(idItem), 'Qtd'] = qtdEstoque
    estoque_df.to_excel("CtrlEstoque.xlsx", index=False)

    #insere no relatorio
    novos_dados = {'Usuario':usuario, 'Item': nomeItem, 'Id': idItem, 'Qtd':qtdEntrada, 'Data':dataEntrada, 'Tecnico': tecnico}
    relatorio_df = pd.concat([relatorio_df,pd.DataFrame([novos_dados])])
    os.system('cls')
    print(relatorio_df)
    print("\n\n",estoque_df)
    relatorio_df.to_excel("RelatorioEstoque.xlsx", index=False)


#FUNCIONANDO TAMEM PRR
def NovoItem():
    print("     Adicionar novo item\n\n")
    estoque_df = pd.read_excel("CtrlEstoque.xlsx")
    relatorio_df = pd.read_excel("RelatorioEstoque.xlsx")
    cad_ok = 'N'

    tecnico = input("Digite sua DRT: ")

    while cad_ok != 'S':
        usuario = "Entrada"
        idItem = estoque_df['ID'].max() + 1
        nomeItem = input("Insira o nome do item: ")
        qtdEntrada = input("Informe a qtd adicionada: ")
        dataEntrada = datetime.now().strftime("%d/%m/%Y")
        cad_ok = input(f"Você deseja adicionar {qtdEntrada} '{nomeItem}' para o estoque? (S/N)")

    #entrada no estoque
    novo_item = {'ID': idItem, 'Item': nomeItem, 'Qtd': qtdEntrada}
    estoque_df = pd.concat([estoque_df,pd.DataFrame([novo_item])])
    estoque_df.to_excel("CtrlEstoque.xlsx", index=False)

    #insere no relatorio
    novos_dados = {'Usuario':usuario, 'Item': nomeItem, 'Id': idItem, 'Qtd':qtdEntrada, 'Data':dataEntrada, 'Tecnico': tecnico}
    relatorio_df = pd.concat([relatorio_df,pd.DataFrame([novos_dados])])
    print(relatorio_df)
    print("\n\n",estoque_df)
    relatorio_df.to_excel("RelatorioEstoque.xlsx", index=False)



#FUNCIONA A PORRA TODA c validação e baixa no estoque
def Reserva():
    estoque_df = pd.read_excel("CtrlEstoque.xlsx")
    relatorio_df = pd.read_excel("RelatorioEstoque.xlsx")

    reserva_ok = "N"
    tecnico = input("Digite sua DRT: ")
    
    while reserva_ok != 'S':

        if reserva_ok == 'OverValue':
            print("O valor solicitado é maior que o estoque!\n\n")
        usuario = input("Insira o nome do usuario que retirou: ")
        idItem = input("Informe o ID do item retirado: ")
        qtdRetirada = input("Informe a qtd retirada: ")
        dataRetirada = datetime.now().strftime("%d/%m/%Y")
        nomeItem = estoque_df.loc[estoque_df['ID'] == int(idItem), 'Item'].iloc[0]
        reserva_ok = input(f"Você deseja retirar {qtdRetirada} '{nomeItem}' para o {usuario}? (S/N)")

        #validação estoque x qtd desejada
        qtdEstoque = estoque_df.loc[estoque_df['ID']==int(idItem), 'Qtd']
        qtdEstoque = qtdEstoque.item()  
        if qtdEstoque<int(qtdRetirada):
            reserva_ok = "OverValue"
    
    #baixa no estoque
    qtdEstoque -= int(qtdRetirada)
    estoque_df.loc[estoque_df['ID']==int(idItem), 'Qtd'] = qtdEstoque
    estoque_df.to_excel("CtrlEstoque.xlsx", index=False)

    #insere no relatorio
    novos_dados = {'Usuario':usuario, 'Item': nomeItem, 'Id': idItem, 'Qtd':qtdRetirada, 'Data':dataRetirada, 'Tecnico': tecnico}
    relatorio_df = pd.concat([relatorio_df,pd.DataFrame([novos_dados])])
    os.system('cls')
    print(relatorio_df)
    print("\n\n",estoque_df)
    relatorio_df.to_excel("RelatorioEstoque.xlsx", index=False)


while int(op) != 9:

    estoque_df = pd.read_excel("CtrlEstoque.xlsx")

    #Menu
    print("\n\n         Controle de Estoque TI\n\n")
    print("1. Reserva de item")
    print("2. Alteração de quantidade")
    print("3. Relatorio de estoque")
    print("4. Relatorio de reservas")
    print("5. Adicionar novo item")
    print("9.Sair\n\n")
    op = input("Selecione a operação desejada: ")

    match(int(op)):
        case 1:
            os.system('cls')
            Reserva()
        case 2:
            os.system('cls')
            AddEstoque()
        case 3:
            os.system('cls')
            RelEstoque()
        case 4:
            os.system('cls')
            RelReservas()
        case 5:
            os.system('cls')
            NovoItem()
