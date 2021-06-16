# 02 - Crie um programa que pergunte ao usuário um
# número inteiro e faça a tabuada desse número

numero = int(input('Informe um numero para ter a tabuada: '))

for n in range(1, 11):
    print(f'{numero} x {n} = {numero * n}')