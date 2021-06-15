# 01 - Faça um programa que leia o sexo biológico de 
# uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso 
# esteja errado, peça a digitação novamente até ter um 
# valor correto.

sexo = str(input("Digite seu sexo biológico [M/F]: ")).upper().strip()

while sexo != 'M' and sexo != 'F':
    print('Opção inválida!')
    sexo = str(input("Digite seu sexo biológico [M/F]: ")).upper().strip()

print("Fim!")
