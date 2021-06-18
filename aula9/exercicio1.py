# 01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

lista = list()


while True:

    valor = int(input('Digite um valor: '))

    if valor not in lista:
        lista.append(valor)

    question = input('Deseja digitar mais? [S/N]: ').upper()[0]
    while question not in 'SN':
        question = input('Deseja digitar mais? [S/N]: ').upper()[0]

    if question == 'S':
        continue
    else:
        break


lista.sort()
print(lista)
