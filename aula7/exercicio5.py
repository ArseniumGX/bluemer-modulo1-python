# 01 - Crie um programa que leia dois valores e mostreum menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# 
# Seu programa deverá realizar a operação solicita da em cada caso.
# (utilizar while sem break)

opcao = 0
valor1 = int(input('Valor 1: '))
valor2 = int(input('Valor 2: '))

while opcao != 5:
    print(f'''
    Escolha uma opção:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    opcao = int(input('____> '))

    if opcao == 1:
        print(f'\n3A soma de {valor1} + {valor2} é {valor1+valor2}')
    elif opcao == 2:
        print(f'\nA multiplicação de {valor1} x {valor2} é {valor1*valor2}')
    elif opcao == 3:
        if valor1 > valor2:
            print('\t\n{} é maior.'.format(valor1))
        elif valor1 < valor2:
            print('\t\n{} é maior.'.format(valor2))
        else:
            print('\t\nValores são iguals.')
    elif opcao == 4:
        valor1 = int(input('Digite um novo valor 1: '))
        valor2 = int(input('Digite um novo valor 2: '))
    elif opcao == 5:
        print('\t\nPrograma encerrado!')
    else:
        print("\t\nopção inválida")


            
