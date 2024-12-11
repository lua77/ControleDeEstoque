from datetime import datetime 
import pandas as pd

relatorio_df = pd.read_excel("RelatorioEstoque.xlsx")
estoque_df = pd.read_excel("CtrlEstoque.xlsx")
reserva_ok = "N"
tecnico = input("Digite sua DRT: ")
    
while reserva_ok != 'S':

    usuario = input("Insira o nome do usuario que retirou: ")
    idItem = input("Informe o ID do item retirado: ")
    qtdRetirada = input("Informe a qtd retirada: ")
    dataRetirada = datetime.now().strftime("%d/%m/%Y")

    nomeItem = estoque_df.loc[estoque_df['ID'] == int(idItem), 'Item'].iloc[0]

    reserva_ok = input(f"Você deseja retirar {qtdRetirada} '{nomeItem}' para o {usuario}? (S/N)")

novos_dados = {'Usuario':usuario, 'Item': nomeItem, 'Id': idItem, 'Qtd':qtdRetirada, 'Data':dataRetirada, 'Tecnico': tecnico}

relatorio_df = pd.concat([relatorio_df,pd.DataFrame([novos_dados])])

relatorio_df.to_excel("RelatorioEstoque.xlsx", index=False)