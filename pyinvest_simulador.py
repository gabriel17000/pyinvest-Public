import math
import random
import datetime
import statistics
import locale


locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")

agora = datetime.datetime.now()

capital_inicial = float(input("Capital inicial (R$): "))
aporte_mensal = float(input("Aporte mensal (R$): "))
prazo_meses = int(input("Prazo (meses): "))
cdi_anual = float(input("CDI anual (%): ")) / 100
percentual_cdb = float(input("Percentual CDI CDB (%): ")) / 100
percentual_lci = float(input("Percentual CDI LCI/LCA (%): ")) / 100
taxa_fii = float(input("Rentabilidade mensal FII (%): ")) / 100
meta_financeira = float(input("Meta financeira (R$): "))

cdi_mensal = (1 + cdi_anual) ** (1 / 12) - 1
taxa_cdb = cdi_mensal * percentual_cdb
taxa_lci = cdi_mensal * percentual_lci
taxa_poupanca = 0.005

total_investido = capital_inicial + (aporte_mensal * prazo_meses)
data_resgate = agora + datetime.timedelta(days=prazo_meses * 30)

valor_futuro = lambda principal, aporte, taxa, meses: (
    principal * (1 + taxa) ** meses
    + aporte * ((((1 + taxa) ** meses) - 1) / (taxa + (taxa == 0))) * (1 + (taxa == 0) * meses)
)

valor_bruto_cdb = valor_futuro(capital_inicial, aporte_mensal, taxa_cdb, prazo_meses)
lucro_cdb = valor_bruto_cdb - total_investido
imposto_cdb = lucro_cdb * 0.15
valor_final_cdb = valor_bruto_cdb - imposto_cdb

valor_final_lci = valor_futuro(capital_inicial, aporte_mensal, taxa_lci, prazo_meses)
valor_final_poupanca = valor_futuro(capital_inicial, aporte_mensal, taxa_poupanca, prazo_meses)

variacao_1 = random.uniform(-0.03, 0.03)
variacao_2 = random.uniform(-0.03, 0.03)
variacao_3 = random.uniform(-0.03, 0.03)
variacao_4 = random.uniform(-0.03, 0.03)
variacao_5 = random.uniform(-0.03, 0.03)

fii_1 = valor_futuro(capital_inicial, aporte_mensal, taxa_fii + variacao_1, prazo_meses)
fii_2 = valor_futuro(capital_inicial, aporte_mensal, taxa_fii + variacao_2, prazo_meses)
fii_3 = valor_futuro(capital_inicial, aporte_mensal, taxa_fii + variacao_3, prazo_meses)
fii_4 = valor_futuro(capital_inicial, aporte_mensal, taxa_fii + variacao_4, prazo_meses)
fii_5 = valor_futuro(capital_inicial, aporte_mensal, taxa_fii + variacao_5, prazo_meses)

simulacoes_fii = [fii_1, fii_2, fii_3, fii_4, fii_5]
media_fii = statistics.mean(simulacoes_fii)
mediana_fii = statistics.median(simulacoes_fii)
desvio_padrao_fii = statistics.stdev(simulacoes_fii)

meta_atingida = media_fii >= meta_financeira

formatar_moeda = lambda valor: locale.currency(valor, grouping=True)
blocos = lambda valor: "█" * math.floor(valor / 1000)

print("\n" + "=" * 60)
print("PYINVEST - SIMULADOR DE INVESTIMENTOS")
print("=" * 60)
print(f"Data da simulacao: {agora.strftime('%d/%m/%Y %H:%M:%S')}")
print(f"Data estimada de resgate: {data_resgate.strftime('%d/%m/%Y')}")
print(f"Total investido: {formatar_moeda(total_investido)}")
print("-" * 60)
print(f"CDB: {formatar_moeda(valor_final_cdb)}")
print(f"LCI/LCA: {formatar_moeda(valor_final_lci)}")
print(f"Poupanca: {formatar_moeda(valor_final_poupanca)}")
print(f"FII (media): {formatar_moeda(media_fii)}")
print("-" * 60)
print("Estatisticas do FII")
print(f"Media: {formatar_moeda(media_fii)}")
print(f"Mediana: {formatar_moeda(mediana_fii)}")
print(f"Desvio padrao: {formatar_moeda(desvio_padrao_fii)}")
print("-" * 60)
print(f"Meta atingida: {meta_atingida}")
print("-" * 60)
print("Grafico de barras ASCII")
print(f"CDB      | {blocos(valor_final_cdb)} {formatar_moeda(valor_final_cdb)}")
print(f"LCI/LCA  | {blocos(valor_final_lci)} {formatar_moeda(valor_final_lci)}")
print(f"Poupanca | {blocos(valor_final_poupanca)} {formatar_moeda(valor_final_poupanca)}")
print(f"FII      | {blocos(media_fii)} {formatar_moeda(media_fii)}")
print("=" * 60)
