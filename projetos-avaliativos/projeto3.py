# Dado-a-Dados Game
from random import randint
from time import sleep
from os import system

rodadas = int()
empates = int()
vencedor = None

while True:
    player1 = {'Jogador': 'Jogador 1', 'dados': [], 'vitorias': int()}
    player2 = {'Jogador': 'Jogador 2', 'dados': [], 'vitorias': int()}
    player3 = {'Jogador': 'Jogador 3', 'dados': [], 'vitorias': int()}
    player4 = {'Jogador': 'Jogador 4', 'dados': [], 'vitorias': int()}
    empates = 0
    jogos = None

    rodadas = int(input('QTD Rodadas: '))

    while not rodadas > 0:
        print('Você não pode jogar {} rodada.'.format(rodadas))
        rodadas = int(input('QTD Rodadas: '))

    for i in range(rodadas):
        dadoP1 = randint(1,6)
        dadoP2 = randint(1,6)
        dadoP3 = randint(1,6)
        dadoP4 = randint(1,6)

        if dadoP1 > dadoP2 and dadoP1 > dadoP3 and dadoP1 > dadoP4:
            player1['vitorias'] += 1
        elif dadoP2 > dadoP1 and dadoP2 > dadoP3 and dadoP2 > dadoP4:
            player2['vitorias'] += 1
        elif dadoP3 > dadoP1 and dadoP3 > dadoP2 and dadoP3 > dadoP4:
            player3['vitorias'] += 1
        elif dadoP4 > dadoP1 and dadoP4 > dadoP2 and dadoP4 > dadoP3:
            player4['vitorias'] += 1
        else:
            empates += 1

        player1['dados'].append(randint(1,6))
        player2['dados'].append(randint(1,6))
        player3['dados'].append(randint(1,6))
        player4['dados'].append(randint(1,6))

        player1['dados'].sort(reverse=True)
        player2['dados'].sort(reverse=True)
        player3['dados'].sort(reverse=True)
        player4['dados'].sort(reverse=True)

        print('Jogador 1: {} no dado.'.format(dadoP1))
        # sleep(1)
        print('Jogador 2: {} no dado.'.format(dadoP2))
        # sleep(1)
        print('Jogador 3: {} no dado.'.format(dadoP3))
        # sleep(1)
        print('Jogador 4: {} no dado.'.format(dadoP4))
        # sleep(1)

        system('clear')

    jogos = (player1.copy(), player2.copy(), player3.copy(), player4.copy())

    for i in jogos:
        print(i)
    
    if jogos[0]['vitorias'] > jogos[1]['vitorias'] and jogos[0]['vitorias'] > jogos[2]['vitorias'] and jogos[0]['vitorias'] > jogos[3]['vitorias']:
        print('O vencendor foi o Jogador 1 com {} vitórias'.format(jogos[0]['vitorias']))
    elif jogos[1]['vitorias'] > jogos[0]['vitorias'] and jogos[1]['vitorias'] > jogos[2]['vitorias'] and jogos[1]['vitorias'] > jogos[3]['vitorias']:
        print('O vencendor foi o Jogador 2 com {} vitórias'.format(jogos[1]['vitorias']))
    elif jogos[2]['vitorias'] > jogos[0]['vitorias'] and jogos[2]['vitorias'] > jogos[1]['vitorias'] and jogos[2]['vitorias'] > jogos[3]['vitorias']:
        print('O vencendor foi o Jogador 3 com {} vitórias'.format(jogos[2]['vitorias']))
    elif jogos[3]['vitorias'] > jogos[0]['vitorias'] and jogos[3]['vitorias'] > jogos[1]['vitorias'] and jogos[3]['vitorias'] > jogos[2]['vitorias']:
        print('O vencendor foi o Jogador 4 com {} vitórias'.format(jogos[3]['vitorias']))
    else:
        print('Ninguém venceu, empates!')
        
    print('Ao todo foram jogadas {} rodadas.'.format(rodadas))
    print('{} empates no total.'.format(empates))
    print('Fim de jogo!')
    print('')
        
    # Instruções de encerramento de jogo
    fim = str(input('Deseja jogar mais partidas? [S/N]: ')).upper().strip()[0]
    while fim not in 'SN':
        print('Opção inválida!')
        fim = str(input('Deseja jogar mais partidas? [S/N]: ')).upper().strip()[0]
    if fim == 'N':
        break
    else:
        continue
