# Desafio:
# Continuando o exercício 3 crie agora um boletim escolar, seu programa 
# deve receber 5 notas de 15 alunos, assim como o nome desses alunos, o 
# programa tem que calcular a média desse aluno e mostrar a situação dele, 
# seguindo os mesmos critérios apresentados no exercício 3. No final 
# apresente todosnomes, as 5 notas, as médias e as situações dos 15 alunos 
# de uma vez só.

turma = list()

for i in range(15):
    aluno = dict()
    notas = list()
    aluno['nome'] = str(input('Nome: '))
    for i in range(5):
        notas.append(float(input(f'Nota {i+1}: ')))
    media = round(sum(notas) / len(notas), 1)
    aluno['notas'] = notas.copy()
    aluno['media'] = media
    if aluno['media'] >= 7.0:
        aluno['situacao'] = 'aprovado'
    elif 5.0 <= aluno['media'] < 7.0:
        aluno['situacao'] = 'recuperação'
    else:
        aluno['situacao'] = 'reprovado'
    turma.append(aluno.copy())

for a in turma:
    print('O aluno(a) {} com média {} está {}.'.format(a['nome'], a['media'], a['situacao']))
