# pilula1_juros.py
# Exercício: cálculo de juros compostos

# 1) Ler dados do usuário
capital_inicial = float(input("Digite o capital inicial (por exemplo 1000): "))
taxa_percentual = float(input("Digite a taxa de juros mensal (em %, ex: 2): "))
meses = int(input("Digite a quantidade de meses: "))

# 2) Converter taxa de percentual para decimal
taxa_mensal = taxa_percentual / 100

# 3) Calcular o montante usando juros compostos
montante = capital_inicial * (1 + taxa_mensal) ** meses

# 4) Exibir resultados
print("\n=== Resultado - Juros Compostos ===")
print(f"Capital inicial: R$ {capital_inicial:,.2f}")
print(f"Taxa mensal: {taxa_percentual:.2f}%")
print(f"Prazo: {meses} meses")
print(f"Montante final: R$ {montante:,.2f}")
