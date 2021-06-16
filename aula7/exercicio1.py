# 01 - Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0.0
menor = 0.0

for p in range(0,5):
    peso = float(input("Digite o peso: "))

    if peso >= maior:
        maior = peso
    else:
        menor = peso

print(f'''
O maior peso informador foi {maior} e o menor foi {menor}
''')

    
