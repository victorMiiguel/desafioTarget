states = [{'estado': 1, 'valor': 67836.43},
           {'estado': 2, 'valor': 36678.66},
           {'estado': 3, 'valor': 29229.88},
           {'estado': 4, 'valor': 27165.48},
           {'estado': 5, 'valor': 19849.53}]

monthlyValue = sum(state['valor'] for state in states)
percentage = [(state['valor'] / monthlyValue) * 100 for state in states]

print(f"Valor mensal total: {monthlyValue}")
print(f"O estado de SP representa {percentage[0]:.1f}%")
print(f"O estado de RJ representa {percentage[1]:.1f}%")
print(f"O estado de MG representa {percentage[2]:.1f}%")
print(f"O estado de ES representa {percentage[3]:.1f}%")
print(f"Os outros estados representam {percentage[4]:.1f}%")
