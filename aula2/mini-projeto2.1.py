""" 
Calculadora de aumento de aluguel

Vamos construir um programa que irá calcular o aumento anual do seu aluguel em duas partes:
Parte 1

A sua calculadora vai receber o valor do aluguel e calcular o aumento baseado no IGPM de 31%. 
A calculadora deve apresentar o aluguel reajustado no formato R$ XXXX.XX

Exemplo: ``` Valor do aluguel = 1000 Valor do aluguel reajustado = R$ 1310,00
"""

valor_aluguel = int(input("Informe o valor do aluguel: "))

novo_aluguel = valor_aluguel + (valor_aluguel*31)/100

print(f'\n\nO valor do aluguel reajustado é: R$ {novo_aluguel:.2f}')
