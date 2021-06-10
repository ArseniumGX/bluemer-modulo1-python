""" 06
Elabore um programa que recebe dois valores inteiros e 
mostra se o primeiro valor é maior ou igual ao segundo valor

Exemplo:

Primeiro Valor = 3
Segundo Valor = 2
Resultado = True
 """
valor1 = int(input("Primeiro valor: "))
valor2 = int(input("Segundo valor: "))

resultado = valor1 >= valor2

print(f'Resultado = {resultado}')

# Operação ternária
print(f'Resultado = {resultado}') if valor1 >= valor2 else print(f'Resultado = {resultado}')

# Com if else
if valor1 >= valor2:
    print(f'Resultado = {resultado}')
else:
    print(f'Resultado: {resultado}')