# Jokenpô The Game
from random import choice
from os import system
from time import sleep

system('clear')

##############[PEDRA]###################
pedraPedra = '''
    {}                  {}
    _______               _______      
---'   ____)             (____   '---  
      (_____)           (_____)        
      (_____)           (_____)        
      (____)             (____)        
---.__(___)               (___)__.---  
'''

pedraPapel = '''
    {}                  {}
    _______                    _______    
---'   ____)              ____(____   '---
      (_____)            (______          
      (_____)           (_______          
      (____)             (_______         
---.__(___)                (__________.---
'''

pedraTesoura = '''
    {}                  {}
    _______                    _______    
---'   ____)              ____(____   '---
      (_____)            (______          
      (_____)           (__________       
      (____)                  (____)      
---.__(___)                    (___)__.---
'''
########################################


###############[PAPEL]##################
papelPapel = '''
    {}                  {}
    _______                    _______    
---'   ____)____          ____(____   '---
          ______)        (______          
          _______)      (_______          
         _______)        (_______         
---.__________)            (__________.---
'''

papelTesoura = '''
    {}                  {}
    _______                     _______    
---'   ____)____           ____(____   '---
          ______)         (______          
          _______)       (__________       
         _______)              (____)      
---.__________)                 (___)__.---
'''

papelPedra = '''
    {}                  {}
    _______               _______      
---'   ____)____         (____   '---  
          ______)       (_____)        
          _______)      (_____)        
         _______)        (____)        
---.__________)           (___)__.---  
'''
########################################

##############[TESOURA]#################
tesouraTesoura = '''
    {}                  {}
    _______                    _______    
---'   ____)____          ____(____   '---
          ______)        (______          
       __________)      (__________       
      (____)                  (____)      
---.__(___)                    (___)__.---
'''

tesouraPedra = '''
    {}                  {}
    _______               _______      
---'   ____)____         (____   '---  
          ______)       (_____)        
       __________)      (_____)        
      (____)             (____)        
---.__(___)               (___)__.---  
'''

tesouraPapel = '''
    {}                  {}
    _______                    _______    
---'   ____)____          ____(____   '---
          ______)        (______          
       __________)      (_______          
      (____)             (_______         
---.__(___)                (__________.---
'''
########################################

oponentes = ['Chewbacca', 'R2-D2', 'C-3PO', 'Steve Magal', 'Chuck Norris']
JanKen = ['Pedra', 'Papel', 'Tesoura']
rodadas = int()
menu = '''
-----===[ Sua Jogada ]===-----

Pedra      Papel      Tesoura
[ 1 ]      [ 2 ]       [ 3 ]

___: '''

# Nome do jogador (algo opcional de por)
player1 = input("\n\nDigite seu nome para iniciar (Opicional): ") or 'Jogador'
# Nome do oponente, achei meio mé so dizer Computador
player2 = choice(oponentes)

system('clear')

print('''
+----------=====[ JanKenPô ]=====----------+
| Olá {}!
|
|    Bem vindo(a) ao joguinho do JanKenPô. 
| Você irá jogar conta o {} aqui. 
| Quem vencerá!?
|    Antes de iniciar a diversão, diga a 
| quantidade de rodadas que deseja jogar. 
|
|                         Boa sorte!        
+-------------------------------------------
'''.format(player1, player2))

sleep(3)

while True:
    # Zerando as vitórias de ambos
    vitoriasJogador = 0
    vitoriasComputer = 0
    
    rodadas = int(input('\nQuantidade de rodadas: '))
        
    while not rodadas > 0:
        print('Você não pode jogar {} rodadas.'.format(rodadas))
        rodadas = int(input('\nQuantidade de rodadas: '))

    print('\nVamos começar!')
    sleep(2)
    system('clear')
    
    for i in range(rodadas):
        
        system('clear')
        computer = choice(JanKen)
        
        # Criação assim apenas para não quebrar o layout
        escolha = int(input(menu))
        while escolha not in [1, 2, 3]:
            print('Opção inválida!')
            escolha = int(input('___:'))
        
        jogador = JanKen[escolha-1]

        
        # Condicional em casos de empate, não faz nada além de mostrar os prints
        if computer == jogador:
            # Apenas para exiber a parte gráfica
            if computer == 'Pedra' and jogador == 'Pedra':
                print(pedraPedra.format(player1, player2))
                sleep(2)
            elif computer == 'Papel' and jogador == 'Papel':
                print(papelPapel.format(player1, player2))
                sleep(2)
            else:
                print(tesouraTesoura.format(player1, player2))
                sleep(2)
        
        # Condicional em casos de vitorias do jogador
        elif jogador == 'Pedra' and computer == 'Tesoura' or jogador == 'Papel' and computer == 'Pedra' or jogador == 'Tesoura' and computer == 'Papel':
            vitoriasJogador += 1

            # Conficional apenas para exibição gráfica
            if jogador == 'Pedra' and computer == 'Tesoura':
                print(pedraTesoura.format(player1, player2))
                sleep(2)
            elif jogador == 'Papel' and computer == 'Pedra':
                print(papelPedra.format(player1, player2))
                sleep(2)
            else:
                print(tesouraPapel.format(player1, player2))
                sleep(2)

        # Else para todos os casos de vitória do computer
        else:
            vitoriasComputer += 1

            # Conficional apenas para exibição gráfica
            if jogador == 'Pedra' and computer == 'Papel':
                print(pedraPapel.format(player1, player2))
                sleep(2)
            elif jogador == 'Papel' and computer == 'Tesoura':
                print(papelTesoura.format(player1, player2))
                sleep(2)
            else:
                print(tesouraPedra.format(player1, player2))
                sleep(2)

    # Pós rodada
    system('clear')
    print('\n\n\n\n')
    print('\tFim das rodadas!')
    print('\tVocê venceu {} rodada(s).'.format(vitoriasJogador))
    print('\t{} venceu {} rodada(s)'.format(player2, vitoriasComputer))

    # Quem venceu?
    if vitoriasJogador > vitoriasComputer:
        print("\n\n\t\tVocê venceu!")
    elif vitoriasComputer > vitoriasJogador:
        print("\n\n\t\tO {} venceu!".format(player2))
    else:
        print("\n\n\t\tJogo terminou empatado!")

    # Fechamento do programa
    fim = input('\n\nDeseja jogar novamente? [S/N]: ').upper().strip()[0]
    while fim not in 'SN':
        fim = input('\nNão entendi!\nDeseja jogar novamente? [S/N]: ').upper().strip()[0]
    
    if fim == 'S':
        system('clear')
        continue
    else:
        break
    #################

# matando as variáveis no escopo global
del [pedraPapel, pedraPedra, pedraTesoura, papelTesoura, papelPapel, papelPedra,
tesouraTesoura, tesouraPapel, tesouraPedra, oponentes, JanKen, rodadas, menu, player1, player2]

print('\n\n\n\tObrigado por jogar!\n\n\n')
sleep(3)
system('clear')
