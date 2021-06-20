# Parte - 01
# Crie um programa que declare uma matriz de dimensão 3×3 
# e preencha com valores lidos pelo teclado. No final, 
# mostre a matriz na tela, com essa formatação:
# 
# [  1  ][  2  ][  3  ]
# [  4  ][  5  ][  6  ]
# [  7  ][  8  ][  9  ] 

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matriz = list()

# print('Digite os valores da matriz: ')
# for l in range(3):
#     data = list()
#     for c in range(3):
#         value = int(input())
#         data.append(value)
    
#     matriz.append(data[:])

for l in matriz:
    for c in l:
        print(' [ {} ] '.format(c), end="")
    print()

# Parte - 02 
# Aprimore o desafio anterior, mostrando no final:
#    A) A soma de todos os valores pares digitados.
#    B) A soma dos valores da terceira coluna. 
#    C) O maior valor da segunda linha.

soma = 0
for l in matriz:
    soma += sum(l)
print('A soma de todos os valores da matriz é {}.'.format(soma))

somaTerceira = 0
for l in matriz:
    somaTerceira += l[2]
print('A soma dos valores da terceira coluna é {}.'.format(somaTerceira))

print('O maior valor da segunda linha é {}.'.format(max(matriz[1])))