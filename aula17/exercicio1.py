# Utilizando os conceitos de Orientação a Objetos (OO) vistos na aula anterior, 
# crie um lançador de dados e moedas em que o usuário deve escolher o objeto a 
# ser lançado. Não esqueça que os lançamentos são feitos de forma randômica

from random import choice, randint
from os import system

class Lancador:
    def __init__(self):
        pass

    def moeda(self):
        return choice(['Cara', 'Coroa'])

    def dado(self):
        return randint(1,6)

while True:
    lance = Lancador()
    print('''
    Escolha o que lançar: 

    [ 1 ] Dados
    [ 2 ] Moeda
    
    
    [ 0 ] FINALIZAR PROGRAMA

    ''')
    escolha = input('----[ ')
    while not escolha.isnumeric():
        escolha = input('----[ ')

    escolha = int(escolha)
    if escolha == 1:
        print(lance.dado())
    elif escolha == 2:
        print(lance.moeda())
    elif escolha == 0:
        break
    else:
        continue
