import pandas as pd

# Importar Base de dados
tabela_vendas = pd.read_excel("Vendas.xlsx")

pd.set_option("display.max_columns", None)

# Faturamento por loja
faturamento = tabela_vendas.groupby("ID Loja")["Valor Final"].sum()
print(faturamento)

print(tabela_vendas)

# Quantidade de produtos vendidos
quantidade = tabela_vendas.groupby("ID Loja")["Quantidade"].sum()
print(quantidade)

print("-"*50)

# Ticket medio de produtos por loja
ticket_medio = faturamento / quantidade
print(ticket_medio.to_string())

# Enviar um e-mail como relatorio