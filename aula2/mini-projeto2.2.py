""" 
Parte 2

Agora, altere sua calculadora para receber além do valor do aluguel, o percentual do reajuste no formato XX%.

Dica: Descubra uma forma de transformar o percentual recebido em um número para efetuar o cálculo.

Exemplo:

Valor do aluguel = 1000
Percentual do reajuste = 31%
Valor do aluguel reajustado = R% 1310,00
"""

valor_aluguel = int(input("Informe o valor do aluguel: "))
taxa_reajuste = int(input("Informe o percentual de reajuste: ").replace("%", ""))

novo_aluguel = valor_aluguel + (valor_aluguel*taxa_reajuste)/100

print(f'\n\nO valor do aluguel reajustado é: R$ {novo_aluguel:.2f}')