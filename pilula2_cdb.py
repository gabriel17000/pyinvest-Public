# pilula2_cdb.py
# Exercício: simular um investimento em CDB com base no CDI

# 1) Ler dados do usuário
capital_inicial = float(input("Digite o capital inicial (por exemplo 1000): "))
aporte_mensal = float(input("Digite o aporte mensal (por exemplo 200): "))
prazo_meses = int(input("Digite o prazo em meses (por exemplo 12): "))
cdi_anual_percentual = float(input("Digite o CDI anual (em %, ex: 13.15): "))
percentual_cdi = float(input("Digite o percentual do CDI que o CDB paga (em %, ex: 100): "))

# 2) Conversão de porcentagem para decimal
cdi_anual = cdi_anual_percentual / 100
percentual_cdi_decimal = percentual_cdi / 100

# 3) Converter CDI anual para CDI mensal (juros compostos)
cdi_mensal = (1 + cdi_anual) ** (1/12) - 1

# 4) Calcular taxa mensal do CDB
taxa_cdb_mensal = cdi_mensal * percentual_cdi_decimal

# 5) Calcular total investido
total_investido = capital_inicial + aporte_mensal * prazo_meses

# 6) Calcular valor bruto final (considerando aportes mensais feitos ao final de cada mês)
valor_bruto = capital_inicial
for mes in range(1, prazo_meses + 1):
    # aplicar rendimento do mês
    valor_bruto *= (1 + taxa_cdb_mensal)
    # adicionar aporte mensal após o rendimento
    valor_bruto += aporte_mensal

# 7) Calcular lucro, imposto e valor líquido
lucro = valor_bruto - total_investido
imposto = 0
if lucro > 0:
    imposto = lucro * 0.15  # imposto de 15% sobre o lucro
valor_liquido = valor_bruto - imposto

# 8) Mostrar resultados
print("\n=== Simulação CDB ===")
print(f"Total investido: R$ {total_investido:,.2f}")
print(f"Valor bruto final: R$ {valor_bruto:,.2f}")
print(f"Lucro (antes do imposto): R$ {lucro:,.2f}")
print(f"Imposto (15% sobre lucro): R$ {imposto:,.2f}")
print(f"Valor líquido após imposto: R$ {valor_liquido:,.2f}")
