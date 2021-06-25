# 7. Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles
# forem iguais, imprima que eles são iguais.
def deMenor(a, b):
    if a > b:
        return b
    elif b > a:
        return a
    else:
        return 'Números iguais'

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
print(deMenor(a, b))
