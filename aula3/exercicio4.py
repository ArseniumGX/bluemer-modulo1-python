""" 
Crie um programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, caso escreva 
outra letra: Sexo Inválido.
"""

sexo = input("Digite F - Feminino ou M - Masculino: \n> ")[0].upper()

if sexo == 'F':
    print("\nFeminino.")
elif sexo == 'M':
    print("\nMasculino.")
else:
    print("\nSexo inválido.")