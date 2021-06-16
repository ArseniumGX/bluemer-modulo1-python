# 04 (DESAFIO)
# Crie um jogo onde o computador vai “pensar” em um número entre
# 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido 
# até acertar, entre os palpites diga ao jogador se o número do 
# computador é maior ou menor ao que ele digitou, no final mostre 
# quantos palpites foram necessários para vencer

from random import randint

print(f'''
Um número entre 0 e 10 foi criado pelo computador. Tente adivinha-lo!
''')

computador  = randint(0, 10)
papiteQTD = 0

while True:
    palpite = int(input('Dê seu palpite: '))

    if computador > palpite:
        print('\n\nÉ maior!')
        papiteQTD += 1
    elif computador < palpite:
        print('\n\nÉ menor!')
        papiteQTD += 1
    else:
        papiteQTD += 1
        break

print(f'''
Parabéns! Em {papiteQTD} palpite(s) você conseguiu vecer a máquina.
''')

