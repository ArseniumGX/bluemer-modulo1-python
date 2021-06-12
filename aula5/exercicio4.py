""" Escreva um programa onde o usuário digita uma frase 
e essa frase retorna sem vogal """

frase = input("Digite uma frase:\n > ").lower()
nova = ''

print(frase.replace('a','').replace('e','').replace('i','').replace('o','').replace('u',''))

for c in frase:
    # if c != 'a' and c != 'e' and c != 'i' and c != 'o' and c != 'u':
    if c not in 'aeiou':
        nova = nova + c

print(nova)