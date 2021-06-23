# 4. Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
# e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente 
# de 0, o dicionário receberá também o ano de contratação e o salário. Calcule 
# e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. 
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
from time import localtime


pessoa = dict()

pessoa['nome'] = str(input('Nome: '))
pessoa['anoNascimento'] = int(input('Ano de nascumento: '))
pessoa['ctps'] = int(input('Número da Carteira de Trabalho: '))
pessoa['idade'] = localtime()[0] - pessoa['anoNascimento']
pessoa.setdefault('anoContratacao', 0)
pessoa.setdefault('salario', 0)


if pessoa['ctps'] > 0:
    pessoa['anoContratacao'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = float(input('Salário: '))

tempoContribuicao = localtime()[0] - pessoa['anoContratacao']
contribuicao = 35 - tempoContribuicao
vaiAposentar = pessoa['idade'] + contribuicao

print('A pessoa {} ja contibuiu por {} e vai se aposentar com {} anos.'.format(pessoa['nome'], tempoContribuicao, vaiAposentar))
