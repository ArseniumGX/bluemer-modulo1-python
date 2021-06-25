# 5. # Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha
# 1,68 e pese 75kg.
def IMC(altura:float, peso:str):
    return round(int(peso.replace('kg', '')) / altura ** 2, 2)

# altura = float(input('Informe o altura: '))
altura = 1.68
# peso = str(input('Digite o peso: '))
peso = '75kg'
print(IMC(altura, peso))
