# 01 - Dada a lista l = [5, 7, 2, 9, 4, 1, 3], escreva um programa 
# que imprima as seguintes informações:
# 
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

l = [5, 7, 2, 9, 4, 1, 3]

soma = 0

cresc = l[:]
cresc.sort()

desc = l[:]
desc.sort()
desc.reverse()


for n in range(0, len(l)):
    soma += l[n]



print(f'''
Lista {l}

Tamanho da lista: {len(l)}
Maior valor da lista: {max(l)}
Menor valor da lista: {min(l)}
Soma de todos os elementos da lista: {soma}
Lista em ordem crescente: {cresc}
Lista em ordem decrescente: {desc}
''')