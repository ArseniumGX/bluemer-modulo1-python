# Faça um programa que leia nome e média de um aluno, guardando 
# também a situação em um dicionário. No final, mostre o conteúdo 
# da estrutura na tela. A média para aprovação é 7. Se o aluno 
# tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.

aluno = {'name': input("Nome do aluno: "), 'media': float(input('Média do aluno: '))}
aluno.setdefault('situacao', None)

if aluno['media'] >= 7.0:
    aluno['situacao'] = 'Aprovado'
elif 5.0 <= aluno['media'] < 7.0:
    aluno['situacao'] = 'Em recuperação'
else:
    aluno['situacao'] = 'Reprovado'

print('O aluno(a) {} com média {} está {}.'.format(aluno['name'], aluno['media'], aluno['situacao']))