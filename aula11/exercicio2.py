# 1. Crie um programa que leia nome, ano de nascimento e 
# carteira de trabalho e cadastre-os (com idade) em um 
# dicionário. Se por acaso a CTPS for diferente de 0, o 
# dicionário receberá também o ano de contratação e o salário. 
# Calcule e acrescente , além da idade , com quantos anos 
# a pessoa vai se aposentar. Considere que o trabalhador 
# deve contribuir por 35 anos para se aposentar.

# calculo
idadeAposentadoria = int()

cidadao = dict()

cidadao = { 'nome': str(input('Nome: ')), 
            'anoNascimento': int(input('Ano de Nascimento: ')),
            'ctps': int(input("Carteira de Trabalho: "))}
cidadao.setdefault('idade', 2021 - cidadao['anoNascimento'])
cidadao.setdefault('anoContratacao', 0)
cidadao.setdefault('salario', 0.0)

if cidadao['ctps'] > 0:
    cidadao['anoContratacao'] = int(input('Ano da contratação: '))
    cidadao['salario'] = float(input('Salário: '))

print(cidadao)
# idadeAposentadoria = 


# incompleto