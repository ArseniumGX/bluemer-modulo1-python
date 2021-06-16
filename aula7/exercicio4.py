# 04 - Desenvolva um programa que leia seis números inteiros e 
# mostre a soma apenas daqueles que forem pares. Se o valor digitado
# for ímpar, desconsidere-o. Mostre também quantos valores pares foram digitados

somaPares = 0
contPares = 0

for n in range(0, 6):
    print(f'Digite o {n+1}º número: ', end='')
    numero = int(input())

    if numero % 2 == 0:
        somaPares += numero
        contPares += 1

print("A soma dos valores pares digitador foi {} e a quantidade de numeros pares foram {}".format(somaPares, contPares))