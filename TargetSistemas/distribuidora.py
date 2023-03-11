import json

with open('dados.json', 'r') as file:
    earningsData = json.load(file)

totalEarning = sum(day['valor'] for day in earningsData if day['valor'] > 0)
daysEarned = sum(1 for day in earningsData if day['valor'] > 0)
earningsAverage = totalEarning / daysEarned

earning_values = [day['valor'] for day in earningsData if day['valor'] != 0]
lowestValue = min(earning_values)
highestValue = max(earning_values)

daysAboveAverage = sum(1 for day in earningsData if day['valor'] > earningsAverage)

print(f"Média de faturamento mensal: R${earningsAverage:.2f}")
print(f"Menor valor de faturamento em um dia do mês: R${lowestValue:.2f}")
print(f"Maior valor de faturamento em um dia do mês: R${highestValue:.2f}")
print(f"Este mês foram {daysAboveAverage} dias com faturamento acima da média mensal!")
