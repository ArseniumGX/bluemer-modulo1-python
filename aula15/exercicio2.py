#02 - Crie um programa que leia nome, gênero e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em
# uma lista. No final, mostre:
# 
#   A) Quantas pessoas foram cadastradas;
#   B) A média de idade;
#   C) Uma lista de pessoas com idade acima da média;
#   D) Uma lista com todos os dados cadastrados de todas as pessoas.
from os import system

pessoas = list()

while True:
    individuo = {'nome': str(), 'genero': str(), 'idade': int()}

    nome = str(input('Nome: ')).strip().title()
    genero = str(input('Gênero [M/F]: ')).upper().strip()[0]
    while genero not in 'MF':
        print('\nInválido!')
        genero = str(input('Gênero [M/F]: ')).upper().strip()[0]
    idade = str(input('Idade: ')).strip()
    while not idade.isnumeric():
        print('\nInválido! Apenas número.')
        idade = str(input('Idade: ')).strip()
    idade = int(idade)

    individuo['nome'] = nome
    individuo['genero'] = genero
    individuo['idade'] = idade

    pessoas.append(individuo.copy())

    fim = str(input('Deseja cadastrar mais pessoas ? [S/N]: ')).upper().strip()[0]
    while fim not in 'SN' or fim == '':
        fim = str(input('Deseja cadastrar mais pessoas ? [S/N]: ')).upper().strip()[0]
    if fim == 'N':
        break
    else:
        continue

system('clear')

#   A) Quantas pessoas foram cadastradas;
print('foram cadastradas {} pessoas.'.format(len(pessoas)))

#   B) A média de idade;
media = int()
for i in range(len(pessoas)):
    media += pessoas[i]['idade']
media //= len(pessoas)
print('A média de idade das pessoas é {} anos.'.format(media))

#   C) Uma lista de pessoas com idade acima da média;
acimaMedia = list()
for i in range(len(pessoas)):
    if pessoas[i]['idade'] > media:
        acimaMedia.append(pessoas[i])
print('Lista de pessoas acima da média de idade: ')
print(acimaMedia)

#   D) Uma lista com todos os dados cadastrados de todas as pessoas.
for i in range(len(pessoas)):
    print('\nNome: {}'.format(pessoas[i]['nome']))
    print('Idade: {}'.format(pessoas[i]['idade']))
    print('Genero: {}'.format(pessoas[i]['genero']))