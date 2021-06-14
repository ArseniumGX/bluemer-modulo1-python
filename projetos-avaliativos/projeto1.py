from sys import exit
from time import sleep

print("\n\n\n\nExecutando, aguarde!\n\n\n\n")
sleep(3)

print(f'''
+---=====[  DETETIVE VIRTUAL  ]=====---+
|   Você está sendo investigado em um  |
| caso de assassinato.    Responda as  |
| perguntas abaixo para ser analizado  |
| seu grau de envolvimento no caso.    |
|                                      |
|                                      |
|               Reponda                |
|          [S]Sim ou [N]Não            |
+--------------------------------------+

''')

pergunta1 = input("Você telefonou para a vítima? ").strip().upper()[0]
if pergunta1 == 'S':
    pergunta1 = 1
elif pergunta1 == 'N':
    pergunta1 = 0
else:
    print('\nVocê não respondeu a pergunta corretamente.\nExecute o programa novamente.')
    exit()

pergunta2 = input("Você esteve no local do crime? ").strip().upper()[0]
if pergunta2 == 'S':
    pergunta2 = 1
elif pergunta2 == 'N':
    pergunta2 = 0
else:
    print('\nVocê não respondeu a pergunta corretamente.\nExecute o programa novamente.')
    exit()

pergunta3 = input("Você mora perto da vítima? ").strip().upper()[0]
if pergunta3 == 'S':
    pergunta3 = 1
elif pergunta3 == 'N':
    pergunta3 = 0
else:
    print('\nVocê não respondeu a pergunta corretamente.\nExecute o programa novamente.')
    exit()

pergunta4 = input("Você devia para a vítima? ").strip().upper()[0]
if pergunta4 == 'S':
    pergunta4 = 1
elif pergunta4 == 'N':
    pergunta4 = 0
else:
    print('\nVocê não respondeu a pergunta corretamente.\nExecute o programa novamente.')
    exit()

pergunta5 = input("Você já trabalhou com a vítima? ").strip().upper()[0]
if pergunta5 == 'S':
    pergunta5 = 1
elif pergunta5 == 'N':
    pergunta5 = 0
else:
    print('\nVocê não respondeu a pergunta corretamente.\nExecute o programa novamente.')
    exit()

resultado = pergunta1 + pergunta2 + pergunta3 + pergunta4 + pergunta5

print('\n\n')
print(f'''
+----------------------------+
|       Analisando !         |
+----------------------------+
''')
sleep(1)
print(".")
sleep(1)
print("..")
sleep(1)
print("...")
sleep(1)

print("\n\n\n")

print('De acordo com nossa rede neural você é: \n\n')

if resultado == 2:
    sleep(2)
    print("\tSuspeito!")
elif resultado == 3 or resultado == 4:
    sleep(2)
    print("\tUm cúplice!")
elif resultado == 5:
    sleep(2)
    print("\tO assassino!")
else:
    sleep(2)
    print("\tInocente!")
