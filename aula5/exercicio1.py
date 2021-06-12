""" Faça um programa que mostre na tela uma contagem regressiva 
para o estouro dos fogos de artificio indo de 10 ate 0 com pause 
de 1s para cada 1 """

from time import sleep

for c in range(10, 0, -1):
    print("{}".format(c))
    sleep(1)

print("\n\nFeliz alguma coisa!")