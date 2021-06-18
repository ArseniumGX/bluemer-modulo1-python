# 02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.

numeros = 0
lista = list()

listaPares = list()
listaImpares = list()

while True:
    numero = int(input("Digite um número: "))
    lista.append(numero)

    if not numero % 2:
        listaPares.append(numero)
    else:
        listaImpares.append(numero)
    
    question = input('Deseja digitar mais? [S/N]').upper()[0]
    while question not in 'SN':
        question = input('Deseja digitar mais? [S/N]').upper()[0]

    if question == 'S':
        continue
    else:
        break




print(f'''
A lista: {lista}
Lista com os valores pares: {listaPares}
Lista com os valores impares: {listaImpares}

''')