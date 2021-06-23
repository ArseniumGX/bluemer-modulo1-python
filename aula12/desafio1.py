# DESAFIO: 
# Crie um programa que leia nome, sexobiologico e idade de várias pessoas, 
# guardando os dados de cada pessoa em um dicionário e todos os dicionários 
# em uma lista. No final, mostre:
# 
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# 
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando 
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.

povoado = list() or []
povo = dict() or {'nome': None, 'idade': None, 'sexoBiologico': None}

while True:
    povo['nome'] = str(input('Nome da Pessoa: ')).strip()
    povo['idade'] = int(input('Idade da Pessoa: '))
    povo['sexoBiologico'] = str(input('Sexo biológico. [M/F]: ')).strip().upper()[0]

    while povo['sexoBiologico'] not in 'MF':
        print('Digite apenas M(masculino) ou F(feminino).')
        povo['sexoBiologico'] = str(input('Sexo biológico. [M/F]: ')).strip().upper()[0]

    povoado.append(povo.copy())

    fim = str(input('\n\nDeseja cadastra mais gente? [S/N]: ')).upper().strip()[0]
    while fim not in 'SN':
        print('\n\nOpção inválida!')
        fim = str(input('Deseja cadastra mais gente? [S/N]: ')).upper().strip()[0]
    if fim == 'N':
        break
    else:
        continue

# A) Quantas pessoas estão cadastradas.
print('Foi cadastrado ao todo {} pessoa(s)'.format(len(povoado)))

# B) A média da idade.
media = 0
for i in povoado:
    media += i['idade']
media //= len(povoado)
print('A média de idade das pessoas é {} anos.'.format(media))

# C) Uma lista com as mulheres.
mulheres = list()
for i in povoado:
    if i['sexoBiologico'] == 'F':
        mulheres.append(i['nome'][:])
print(mulheres)

# D) Uma lista com as idades que estão acima da média.
idadesAcima = list()
for i in povoado:
    if i['idade'] > media:
        idadesAcima.append(i['idade'])
print(idadesAcima)