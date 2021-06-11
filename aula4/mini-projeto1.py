""" 
    Escreva um programa que receba uma string digitada pelo usuário;
    Caso a string seja "medieval", exiba no console "espada";
    Caso contrário, se a string for "futurista", exiba no console "sabre de luz";
    Caso contrário, exiba no console "Tente novamente"
"""

entrada = input("Digite algo: ").lower().strip()

if entrada == 'medieval':
    print("Espada.")
elif entrada == 'futurista':
    print("Sabre de luz.")
else:
    print("Tente novamente!")
