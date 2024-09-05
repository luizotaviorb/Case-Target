import json

# Exemplo de dados no formato JSON
dados_json = '''
{
  "faturamento": [
    {"dia": 1, "valor": 1000},
    {"dia": 2, "valor": 2000},
    {"dia": 3, "valor": 0},
    {"dia": 4, "valor": 1500},
    {"dia": 5, "valor": 0},
    {"dia": 6, "valor": 3000},
    {"dia": 7, "valor": 100}
  ]
}
'''

# Carregando os dados JSON
dados = json.loads(dados_json)

# Extraindo apenas os valores de faturamento, ignorando dias com faturamento igual a 0
valores_faturamento = [item['valor'] for item in dados['faturamento'] if item['valor'] > 0]

# Cálculo do menor valor de faturamento
menor_faturamento = min(valores_faturamento)

# Cálculo do maior valor de faturamento
maior_faturamento = max(valores_faturamento)

# Cálculo da média mensal de faturamento
media_mensal = sum(valores_faturamento) / len(valores_faturamento)

# Número de dias com faturamento acima da média mensal
dias_acima_media = sum(1 for valor in valores_faturamento if valor > media_mensal)

# Mostrar os resultados
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")