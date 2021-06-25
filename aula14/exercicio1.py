# 1. Faça um programa, com uma função que necessite de três argumentos, e que forneça a
# soma desses três argumentos.
def somaTres(values:list):
    return sum(values)
numeros = [int(input('Value 1: ')), int(input('Value 2: ')), int(input('Value 3: '))]
print(somaTres(numeros))
 