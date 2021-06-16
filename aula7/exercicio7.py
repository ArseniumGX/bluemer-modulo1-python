# 03 - Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No 
# final, mostre:
# 
# A) Qual é o total gasto na compra;
# B) Quantos produtos custam mais de R$1000;
# C) Qual é o nome do produto mais barato.

total = 0.0
contMaiorMil = 0
nomeMaisCaro = ''
maisCaro = 0.0

while True:
    nome = str(input('\nNome do produto: '))
    preco = float(input('Preço do produto: '))


    total += preco

    if preco > 1000:
        contMaiorMil += 1

    if preco > maisCaro:
        nomeMaisCaro = nome


    op = str(input('\n\nDeseja continuar? [S/N]: ')).upper().strip()[0]

    while op not in 'SN':
        print('\nOpção inválida!\nTente novamente')
        op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if op == 'N':
        break

print(f'''
O total de gastos foi: {total:.2f}
O total de produtos acima de 1000 é: {contMaiorMil}
O produto mais caro é: {nomeMaisCaro}
''')