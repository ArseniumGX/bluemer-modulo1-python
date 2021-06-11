""" Caixa eletrônico

Faça um Programa para um caixa eletrônico. O programa 
deverá perguntar ao usuário a valor do saque e depois 
informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de 
notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o 
    programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

    Exemplo 2: Para sacar a quantia de 399 reais, o 
    programa fornece três notas de 100, uma nota de 50, 
    quatro notas de 10, uma nota de 5 e quatro notas de 1. """

print(f'''
-==={{ Bem vindo a banco SeuDinheiroSeu }}===-
Aqui seu dinheiro não rende, mas está seguro.
Temos as notas de 1, 5, 10, 50 e 100 disponíveis
Valor mínimo de saque: R$ 10,00
valor máximo de saque: R$ 600,00
''')

valor = int(input("Informe o valor a sacar: "))

nota100 = valor // 100
nota50 = (valor%100) // 50
nota10 = ((valor%100)%50) // 10
nota5 = (((valor%100)%50)%10) // 5
nota1 = ((((valor%100)%50)%10)%5) // 1

if valor >= 10 and valor <= 600:
    print(f'''
    Seu saque será de {valor} será com:
    {nota100} nota(s) de 100
    {nota50} nota(s) de 50
    {nota10} nota(s) de 10
    {nota5} nota(s) de 5
    {nota1} nota(s) de 1
    ''')
else:
    print("Valor muito baixo.") if valor < 10 else print("Valor muito alto.")