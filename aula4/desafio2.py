""" Jogo da adivinhação

Escreva um programa que faça o computador “pensar” em 
um número inteiro entre 0 e 10 e peça para o usuário 
tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu. """

import random

print(f'''
-====- Advinhação nossa de cada dia -====-

Um valor aleatório entre 0 e 10 foi gerado
enquanto você leu esse texto.

Sua missão: Adinhe qual o número, você so 
tem uma chance. Boa sorte!
''')

aleatorio = random.randint(0, 10)
# print(aleatorio)

valor = int(input("Entre com um valor entre 0 e 10\n> "))

if valor == aleatorio:
    print("\n\nParabéns!\nVocê superou a máquina.")
else:
    print("\n\n:(\nVocê não conseguiu.")
