""" 
Faça um programa que pergunte ao usuário um número e valide se o numero é par ou impar:

    Crie uma variável para receber o valor, com conversão para int
    Para um número ser par, a divisão dele por 2 tem que dar resto 0

"""

numero = int(input("Digite um número: "))

if numero != 0:
    if numero % 2 == 0:
        print(f'{numero} é par!')
    else:
        print(f'{numero} é impar!')
else:
    print("Número é zero!")