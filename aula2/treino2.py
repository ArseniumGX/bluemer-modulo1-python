""" 
Etiqueta - Elabore um programa que escreve seu nome completo na 
primeira linha, seu endereço na segunda e o CEP e telefone na terceira.
"""

nome = input("Digite seu nome completo: ")
endereco = input("Digite seu endereço: ")
cep = input("Digite seu CEP: ")
telefone = input("Digite seu telefone: ")

print(f'''
Nome: {nome}
Endereço: {endereco}
CEP: {cep}   -   Telefone: {telefone}
''')