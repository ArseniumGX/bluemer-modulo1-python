""" Desenvolva um código que pergunte um número n para 
o usuário e exiba todos os seus divisores """

numero = int(input("Digite um número inteiro: "))

for i in range(1, numero):
    if not numero % i:
        print(f"O número {numero} é divisível por {i}")
