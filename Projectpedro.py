import pandas as pd

# Importar Base de dados
tabela_vendas = pd.read_excel("Vendas.xlsx")

pd.set_option("display.max_columns", None)

# Faturamento por loja
faturamento = tabela_vendas.groupby("ID Loja")["Valor Final"].sum()
print("\n=== FATURAMENTO POR LOJA ===")
print(faturamento.to_string())

print("\n" + "="*50 + "\n")

# Quantidade de produtos vendidos
quantidade = tabela_vendas.groupby("ID Loja")["Quantidade"].sum()
print("\n=== QUANTIDADE POR LOJA ===")
print(quantidade.to_string())

print("\n" + "="*50 + "\n")

# Ticket medio de produtos por loja
ticket_medio = faturamento / quantidade
print("\n=== TICKET MÉDIO POR LOJA ===")
print(ticket_medio.to_string())

print("\n" + "="*50 + "\n")

# Enviar um e-mail como relatorio