""" 
Crie um programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, caso escreva 
outra letra: Sexo Inválido.
"""

sexo = input("Qual seu sexo biológico? [F/M]: ").upper().strip()[0]

""" if sexo == 'F':
    print("\nFeminino.")
elif sexo == 'M':
    print("\nMasculino.")
else:
    print("\nSexo biológico inválido.") """

# Diferentão

if sexo == 'M' or sexo == 'F':
    print("\nMasculino") if sexo == 'M' else print('\nFeminino')
else:
    print("\nSexo biológico inválido.")
