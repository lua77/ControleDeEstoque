import pandas as pd
from datetime import datetime

op = 0

estoque_df = pd.read_excel("CtrlEstoque.xlsx")
relatorio_df = pd.read_excel("RelatorioEstoque.xlsx")

def RelEstoque():
    print(estoque_df)

def AddEstoque():
    print("add estoque")

def SubEstoque():
    print("sub estoque")


#FUNCIONA A PORRA TODA MENOS ABAIXAR O ESTOQUE
def Reserva():
    estoque_df = pd.read_excel("CtrlEstoque.xlsx")
    relatorio_df = pd.read_excel("RelatorioEstoque.xlsx")

    reserva_ok = "N"
    tecnico = input("Digite sua DRT: ")
    
    while reserva_ok != 'S':

        usuario = input("Insira o nome do usuario que retirou: ")
        idItem = input("Informe o ID do item retirado: ")
        qtdRetirada = input("Informe a qtd retirada: ")
        dataRetirada = datetime.now().strftime("%d/%m/%Y")

        nomeItem = estoque_df.loc[estoque_df['ID'] == int(idItem), 'Item'].iloc[0]

        reserva_ok = input(f"Você deseja retirar {qtdRetirada} '{nomeItem}' para o {usuario}? (S/N)")

    qtdEstoque = estoque_df.loc[estoque_df["ID"] == idItem, 'Qtd']
    #qtdEstoque = pd.to_numeric(estoque_df['Qtd'], errors='coerce')
    qtdEstoque = qtdEstoque - int(qtdRetirada)
    
    novos_dados = {'Usuario':usuario, 'Item': nomeItem, 'Id': idItem, 'Qtd':qtdRetirada, 'Data':dataRetirada, 'Tecnico': tecnico}

    relatorio_df = pd.concat([relatorio_df,pd.DataFrame([novos_dados])])
    
    
    
    estoque_df.loc[estoque_df["ID"] == idItem, 'Qtd'] = qtdEstoque
    
    estoque_df.to_excel("CtrlEstoque.xlsx", index=False)
    
    print("\n", relatorio_df)

    relatorio_df.to_excel("RelatorioEstoque.xlsx", index=False)

# while int(op) != 9:

#     estoque_df = pd.read_excel("CtrlEstoque.xlsx")

#     #Menu
#     print("         Estoque TI\n\n")
#     print("1. Reserva de item")
#     print("2. Alteração no estoque")
#     print("3. Relatorio de estoque")
#     print("4. Relatorio de reservas\n")
#     op = input("Selecione a operação desejada: ")


print(estoque_df)
Reserva()
