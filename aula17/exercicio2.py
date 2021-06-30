# Vamos aprimorar o código: cadastro_de_jogador_de_futebol.py que foi 
# desenvolvido no CodeLab da aula14. Faça com que o seu código funcione
# para vários jogadores, incluindo um sistema de visualização de detalhes 
# de aproveitamento de cada jogador.

from os import system

class Jogador:
    def __init__(self):
        self.nome = str()
        self.quantidadePartidas = int()
        self.golsPorPartidas = list()
        self.totalGols = int()

    def novoJogador(self, nome, qtdPartidas):
        self.nome = nome
        self.quantidadePartidas = qtdPartidas

    def aproveitamento(self):
        for i in range(self.quantidadePartidas):
            self.golsPorPartidas.append(int(input('Gols na partida {}: '.format(i+1))))
        self.totalGols += sum(self.golsPorPartidas)

    def detalhes(self):
        return 'O jogador {} jogou {} partidas marcando um total de {} gols.'.format(self.nome, self.quantidadePartidas, self.totalGols)


while True:

    print('''
    ESTATICO JOGADOR

    1. Novo jogador
    2. Estatistica do jogador

    0. ENCERRAR PROGRAMA
    ''')
    opcao = input('__: ')
    while not opcao.isnumeric():
        opcao = input('__: ')
    
    opcao = int(opcao)
    if opcao == 1:
        jogador = Jogador()
        system('clear')
        nome = str(input('Nome do Jogador: '))
        qtdPartidas = int(input('Quantidade de partidas jogadas: '))
        jogador.novoJogador(nome, qtdPartidas)
        jogador.aproveitamento()
    elif opcao == 2:
        system('clear')
        print(jogador.detalhes())
    elif opcao == 0:
        system('clear')
        break
    else:
        system('clear')
        continue
