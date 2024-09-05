# Valores de faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Cálculo do faturamento total
faturamento_total = sum(faturamento_estados.values())

# Cálculo do percentual de cada estado e exibição dos resultados
percentuais_estados = {estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()}

# Exibir o percentual de cada estado
for estado, percentual in percentuais_estados.items():
    print(f"{estado}: {percentual:.2f}%")
