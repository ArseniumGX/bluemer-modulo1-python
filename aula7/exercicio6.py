# 02 - Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
# 
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

contHomens = 0
contMaior18 = 0
contMulherMenos20 = 0

while True:
    idade = int(input('\nInforme a idade da pessoa: '))
    sexo = str(input('Informe o sexo bilógico da pessoa. [M/F]: ')).strip().upper()[0]

    if idade > 18:
        contMaior18 += 1
    if sexo == 'M':
        contHomens += 1
    elif sexo == 'F' and idade < 20:
        contMulherMenos20 += 1


    op = str(input('\n\nDeseja Cadastrar mais pessoas [S/N]: ')).upper().strip()[0]
    while op not in 'SN':
        print('\nOpção inválida!\nTente novamente.\n')
        op = str(input('\n\nDeseja Cadastrar mais pessoas [S/N]: ')).upper().strip()[0]

    if op == 'N':
        break

print(f'''
Existem {contMaior18} pessoas com mais de 18 anos;
{contHomens} são homens e {contMulherMenos20} é/são mulher(es) com menos de 20 anos.
''')