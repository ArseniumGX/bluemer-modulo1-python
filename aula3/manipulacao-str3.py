""" 
03 - Elabore um programa que recebe o seu nome, endereço e hobby e 
mostra cada uma das informações da seguinte forma:

    Nome -> Letra maiúscula
    Endereço -> Letra minúscula
    Hobby -> Primeira letra maiúscula

Exemplo Entrada:

Nome: bruno fabri
Endereço: Rua ABC
Hobby: jogar cs

Exemplo Saída:

Nome: BRUNO FABRI
Endereço: rua abc
Hobby: Jogar cs
"""

nome = input("Digite seu nome:")
endereco = input("Digite seu endereço: ")
hobby = input("Digite seu hobby: ")

print(f'''
Nome: {nome.upper()}
Endereço: {endereco.lower()}
Hobby: {hobby.capitalize()}
''')
