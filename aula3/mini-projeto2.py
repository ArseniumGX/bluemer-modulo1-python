"""
    Escreva um programa que receba um ataque de espada ou sabre digitada pelo usuário;

    Caso o ataque seja "espada", exiba no console "VOCÊ AINDA NÃO MATOU O CHEFÃO";

    Caso contrário, se o ataque for "sabre", exiba no console "VOCÊ DERROTOU O CHEFÃO COM O SABRE DE LUZ";

    Caso contrário, exiba no console "ATAQUE NOVAMENTE"
"""

ataque = input("Digite seu ataque: ").lower()

if ataque == 'espada':
    print("VOCÊ AINDA NÃO MATOU O CHEFÃO")
elif ataque == 'sabre':
    print("VOCÊ DERROTOU O CHEFÃO COM O SABRE DE LUZ")
else:
    print("ATAQUE NOVAMENTE")