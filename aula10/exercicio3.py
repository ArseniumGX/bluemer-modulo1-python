# 03 - Faça um programa que leia nome e peso de várias pessoas, 
# guardando tudo em uma lista, depois do dado inserido, pergunte 
# ao usuário se ele quer continuar, se ele não quiser pare o programa. 
# No final mostre:
#   Quantas pessoas foram cadastradas
#   Mostre o maior peso
#   Mostre o menor peso

pessoas = list()
cont = 0

while True:
    pessoas.append([str(input('Nome: ')), float(input('Peso: '))])
    cont += 1

    fim = str(input('\nDeseja cadastrar mais pessoas? [S/N]: ')).upper().strip()[0]
    while fim not in 'SN':
        fim = str(input('\nOpção inválida!\nDeseja cadastrar mais pessoas? [S/N]: ')).upper().strip()[0]

    if fim == 'S':
        continue
    else:
        break

pesos = list()

for i in pessoas:
    pesos.append(i[1])

print(pesos)
print('Foram cadastradas {} pessoas.'.format(len(pessoas)))
print('O maior peso é {}.'.format(max(pesos)))
print('O menor peso é {}.'.format(min(pesos)))
