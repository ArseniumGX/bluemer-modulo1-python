# 02 - Desenvolva um programa que leia quatro valores pelo teclado 
# e guarde-os em uma tupla. No final, mostre:
# 
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.

print('Digite 4 valores: ')
valores = (int(input()), int(input()), int(input()), int(input()))

print(f'Valor 9 digitado {valores.count(9)} vezes.')
if valores.count(3):
    print(f'Primeiro valor 3 digitado na posição {valores.index(3)}.')
else:
    print(f'Primeiro nenhum valor 3 digitado.')