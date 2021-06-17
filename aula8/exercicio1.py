# 01 - Crie um programa que vai gerar cinco números aleatórios 
# de 1 a 50 e colocar em uma  tupla. Depois disso, mostre a 
# listagem de números gerados e também indique o menor e o maior 
# valor que estão na tupla. Sem utilizar repetições. 
# Dica: utilizar a biblioteca random do Pytho

from random import randint

numeros = (randint(1,50), randint(1,50), randint(1,50), randint(1,50), randint(1,50))

print(numeros)
print(f'O menor é {sorted(numeros)[:1:]}.')
print(f'O maior é {sorted(numeros)[-1::]}.')

