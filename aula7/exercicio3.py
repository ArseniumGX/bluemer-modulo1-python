# 03 - Crie ump rograma que leia o ano de nascimento de 
# sete pessoas. No final, mostre quantas pessoas ainda não atingiram 
# a maioridade e quantas já são maiores.

anoAtual = 2021

deMaior = 0
deMenor = 0

for p in range(0, 7):
    print(f'Pessoa {p+1}')
    anoNascimento = int(input('Ano de nascimento: '))

    idade = anoAtual - anoNascimento

    if idade >= 18:
        deMaior += 1
    else:
        deMenor += 1

print(f'''
Existem {deMaior} que ja estão na maioridade e {deMenor} ainda são menor de idade.
''')