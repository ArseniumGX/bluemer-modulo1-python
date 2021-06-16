# 05 (DESAFIO)
# Em uma eleição presidencial existem quatro candidatos.
# Os votos são informados por meio de código. Os códigos 
# utilizados são:
# 1, 2, 3 - Votos para os respectivos candidatos(você deve montar a tabela ex: 1 - José / 2- João/ etc)
# 5 - Voto Nulo
# 6 - Voto em Branco 
# 
# Faça um programa que calcule e mostre:
# 
# 1) O total de votos para cada candidato;
# 2) O total de votos nulos;
# 3) O total de votos em branco;
# 4) A percentagem de votos nulos sobre o total de votos;
# 5) A percentagem de votos em branco sobre o total devotos.

total = 0
totalNulos = 0
totalBranco = 0
cand1 = 0
cand2 = 0
cand3 = 0


while True:
    print(f'''
    Eleição TopTop...

    1 - Morlock
    2 - Orago
    3 - Vitali

    4 - Voto Nulo
    5 - Vote em Branco

    0 - Finalizar eleição
    ''')

    op = str(input("Vote: "))

    while op not in '123450':
        print('Opção inválida!')
        op = str(input("Vote: "))

    if op == '1':
        cand1 += 1
        total += 1
    elif op == '2':
        cand2 += 1
        total += 1
    elif op == '3':
        cand3 += 1
        total += 1
    elif op == '4':
        totalNulos += 1
        total += 1
    elif op == '5':
        totalBranco += 1
        total += 1
    else:
        break



print(f'''
O candidato Morlock recebeu {cand1}
O candidato Orago recebeu {cand2}
O candidato Vitali recebeu {cand3}

O total de votos nulos foi {totalNulos} totalizando {(total - totalNulos/100)}% do total
O total de votos em branco foi {totalBranco} totalizando {total - totalBranco/100}% do total

''')