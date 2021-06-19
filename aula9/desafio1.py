# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

print(f'''
+---------=========[ Brega Sena ]=========---------+
|  Seu palpite de bolso a apenas um click de sorte |
| para ganhar 1 milho grande!                      |
|                                                  |
|    Para iniciar o trampo indique abaixo quantos  |
| Jogos deseja gera.                               |
|                         Boa sorte!               |
|                             Ou não!              |
+-================================================-+
''')

jogos = list()
numeroJogos = int(input('\n\nQTD Jogos: '))

for l in range(numeroJogos):
    cont = 0
    jogo = list()
    while True:
        numero = randint(1,60)
        if numero not in jogo:
            jogo.append(numero)
            cont += 1
        if cont == 6:
            break
    
    jogo.sort()
    jogos.append(jogo)

print(f'''\n\n
Seus número da sorte (ou não) são...
------------------------------------
''')
for (i, v) in enumerate(jogos):
    print('{} Jogo: {}'.format(i+1, v))
