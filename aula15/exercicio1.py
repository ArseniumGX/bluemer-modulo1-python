# 01 - Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
# programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
# quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
# dicionário, incluindo o total de gols feitos durante o campeonato.

aproveitamento = {'nome': str(), 'qtd-jogos': int(), 'gol-partida': list(), 'total-gols': int()}


aproveitamento['nome'] = str(input('Nome do jogador: '))
aproveitamento['qtd-jogos'] = int(input('Partidas jogadas: '))

for i in range(aproveitamento['qtd-jogos']):
    aproveitamento['gol-partida'].append(int(input('Gols na partifa {}: '.format(i+1))))

aproveitamento['total-gols'] = sum(aproveitamento['gol-partida'])

print('''
O Jogador {} jogou {} fazendo um total de {} gols.
'''.format(aproveitamento['nome'], aproveitamento['qtd-jogos'], aproveitamento['total-gols']))
