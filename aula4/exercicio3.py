""" 
Faça um programa que peça dois números, imprima o maior deles ou imprima
"Numeros iguais" se os números forem iguais.
"""

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1 > num2:
    print(f"\n{num1} é maior!")
elif num1 < num2:
    print(f"\n{num2} é maior!")
else:
    print(f"\nNúmeros iguais.")
