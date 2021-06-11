""" Parte 1

Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.

    Parte 2

Agora implemente a funcionalidade de não aceitar o número 0, no input. (esse vai além do explicado até agora) """


numero = int(input("Digite um número: "))

# Parte 1s
if numero > 0:
    print(f'{numero} é positivo!')
elif numero < 0:
    print(f'{numero} é negativo!')
else: # Parte 2
    print(f'{numero} é inaceitável!')
