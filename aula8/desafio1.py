# Desafio da noite:
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# 
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

resultado = 0
pergunta = [
    "Você telefonou para a vítima? [S/N]: ", 
    "Você esteve no local do crime? [S/N]: ",
    "Você mora perto da vítima? [S/N]: ",
    "Você devia para a vítima? [S/N]: ",
    "Você já trabalhou com a vítima? [S/N]: "
]

for n in range(0, len(pergunta)):
    resposta = str(input(pergunta[n]).upper()[0])

    while resposta not in 'SN':
        print('Respoda corretamente.')
        resposta = str(input(pergunta[n]).upper()[0])

    if resposta == 'S':
        resultado += 1
    else:
        continue

if resultado == 2:
    print("Suspeito!")
elif resultado == 3 or resultado == 4:
    print("Um cúplice!")
elif resultado == 5:
    print("O assassino!")
else:
    print("Inocente!")
