# Desafio: Crie um jogo onde o computador vai “pensar” em 
# um número entre 0 e 10. O jogador vai tentar adivinhar 
# qual número foi escolhido até acertar, entre os palpites 
# diga ao jogador se o número do computador é maior ou menor 
# ao que ele digitou,no final mostre quantos palpites foram 
# necessários para vencer

from random import randint
from time import sleep

print(f'''
----=====---- Meu AdVinha Bluemer ----=====----
\tEnquanto você ler essa frase, um número
aleatório entre 0 e 10 está sendo criado. Tente
adivinhar!''')

print('.', end="")
sleep(1)
print('.', end="")
sleep(1)
print('.', end="")
sleep(1)
print('.', end="")
sleep(1)
print('.')


numero = randint(0, 10)
cout = 1

print()

while True:
    chute = int(input("Adivinhe o número: "))
    if numero > chute:
        print('Mais.. tente novamente: ')
        cout += 1
    elif numero < chute:
        print("Menos.. tente novamente: ")
        cout += 1
    else:
        print("Parabéns, você acertou!")
        cout += 1
        break

print('Fim!')