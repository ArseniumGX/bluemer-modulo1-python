# Faça um programa em Python com uma função que necessite de três 
# parametros, e que forneça: 
# 
# a. A soma desses três parametros através de uma função. 
# b. Seu script também deve fornecer a média dos três números, através 
# de uma segunda função que chama a primeira. 

def somaTres(a:float, b:float, c:float):
    soma = round(sum([a,b,c]), 2)
    media = mediaTodos(soma)
    return [soma, media]

def mediaTodos(x):
    return round(x / 3, 2)


params = somaTres(float(input('Valor 1: ')), float(input('Valor 2: ')), float(input('Valor 3: ')))
print('A soma dos valores é {} e a média é {}.'.format(params[0], params[1]))
