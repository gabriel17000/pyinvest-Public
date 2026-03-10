# pilula3_simulador.py
# Exercício: simulador simples de investimento com aportes mensais

# 1) Ler dados do usuário
capital_inicial = float(input("Digite o capital inicial (por exemplo 1000): "))
aporte_mensal = float(input("Digite o aporte mensal (por exemplo 200): "))
prazo_meses = int(input("Digite o prazo em meses (por exemplo 12): "))
taxa_mensal_percentual = float(input("Digite a taxa mensal esperada (em %, ex: 1.5): "))

# 2) Converter taxa para decimal
taxa_mensal = taxa_mensal_percentual / 100

# 3) Total investido (capital + todos os aportes)
total_investido = capital_inicial + aporte_mensal * prazo_meses

# 4) Calcular valor futuro com juros compostos e aportes mensais
# Fórmula do valor futuro com aportes mensais (anuidade):
# FV = capital * (1 + i)^n + aporte * (( (1 + i)^n - 1 ) / i)
if taxa_mensal != 0:
    valor_futuro = capital_inicial * (1 + taxa_mensal) ** prazo_meses
    valor_futuro += aporte_mensal * (((1 + taxa_mensal) ** prazo_meses - 1) / taxa_mensal)
else:
    # Se a taxa for zero, não há rendimento
    valor_futuro = total_investido

# 5) Calcular lucro e verificar se há ganho
lucro = valor_futuro - total_investido
houve_lucro = lucro > 0

# 6) Relatório final
print("\n=== Relatório do Simulador ===")
print(f"Capital inicial: R$ {capital_inicial:,.2f}")
print(f"Aporte mensal: R$ {aporte_mensal:,.2f}")
print(f"Prazo: {prazo_meses} meses")
print(f"Taxa mensal esperada: {taxa_mensal_percentual:.2f}%")
print("---")
print(f"Total investido: R$ {total_investido:,.2f}")
print(f"Valor futuro estimado: R$ {valor_futuro:,.2f}")
print(f"Lucro final: R$ {lucro:,.2f}")
print(f"Teve lucro maior que zero? {'Sim' if houve_lucro else 'Não'}")
