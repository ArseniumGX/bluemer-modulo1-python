""" 05
Elabore um programa que receba 4 notas de um aluno e calcule a média dele.

Exemplo:

Primeiro Nota = 7
Segundo Nota = 8
Terceiro Nota = 10
Quarto Nota = 6
 
Média = 7,75
"""

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
n4 = float(input("Quarta nota: "))

media = (n1+n2+n3+n4)/4

print(f'\nMédia = {media:.2f}')