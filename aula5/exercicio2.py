""" Dada um string informada pelo usuário (incluindo espaços em branco), 
conte quantas vezes aparece as vogais a, e, i, o, u """

string = input("Digite alguma coisa: ").lower()
vogais = 0

for l in string:
    if l in 'aeiou':
        vogais += 1
    

print(f'As vogais a, e, i, o, u aparece {vogais} vezes.')