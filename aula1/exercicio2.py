""" 02 
Elabore um programa que escreve seu nome completo na primeira linha, 
seu endereço na segunda e o CEP e telefone na terceira.

Exemplo:

Nome: Bruno Fabri
Endereço: Rua ABC
CEP: 002220-010
"""
nome = input("Digite seu nome: ")
endereco = input("Digite seu endereço: ")
cep = input("Digite seu CEP: ")

print(f'''
Nome: {nome}
Endereço: {endereco}
CEP: {cep}
''')