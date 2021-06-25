# 6. Escreva uma função que, dado um número nota representando a nota de um estudante, 
# converte o valor de nota para um conceito (A, B, C, D, E e F). 
# Nota Conceito
# >=9.0 A
# >=8.0 B
# >=7.0 C
# >=6.0 D
# <=4.0 F7.
def conceito(nota:float):
    if 9.0 <= nota <= 10.0:
        return 'A'
    elif 8.0 <= nota < 9.0:
        return 'B'
    elif 7.0 <= nota < 8.0:
        return 'C'
    elif 6.0 <= nota < 7.0:
        return 'D'
    elif 5.0 <= nota < 6.0:
        return 'E'
    elif 0.0 <= nota < 5.0:
        return 'F'
    else:
        return 'Fora de parâmetro'

print(conceito(10))
