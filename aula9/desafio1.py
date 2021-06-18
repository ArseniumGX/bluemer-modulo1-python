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
numeroJogos = int(input('\n\n___QTD Jogos: '))

for l in range(numeroJogos):
    jogo = list()
    for c in range(6):
        jogo.insert(c, randint(1,60))
    
    jogos.insert(l, jogo)

print(f'''
Seus número da sorte (ou não) são...
------------------------------------
''')
for l in range(len(jogos)):
    print(jogos[l])
