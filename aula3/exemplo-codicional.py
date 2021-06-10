n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
n4 = float(input("Quarta nota: "))

media = (n1+n2+n3+n4) / 4

# Apenas para dois possiveis resultados
# print(f'\nMédia: {media:.1f}\nAluno aprovado!') if media >= 6 else print(f'\nMédia: {media:.1f}\nAluno reprovado!')

# OU

if media >= 6:
    print(f'\nMédia: {media:.1f}\nAluno aprovado!')
elif media >= 4 and media < 6:
    print(f'\nMédia: {media:.1f}\nAluno em recuperação.')
else:
    print(f'\nMédia: {media:.1f}\nAluno reprovado!')
