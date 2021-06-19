# Crie uma lista composta que recebe 5 nomes e 5 
# idades de clientes, utilizando o for e o if, 
# verifique quais clientes são maiores de idade e 
# quais são menores de idade e mostre na tela a 
# seguinte frase para cada um deles: 'Fulano é maior 
# de idade' ou 'Fulana é menor de idade' e também 
# quantos são maiores e quantos são menores de idade. 

clients = list()
maior = int() 
menor = int()

for i in range(5):
    pessoa = list

    pessoa = [str(input('Digite o nome: ')), int(input('Digite a idade: '))]
    clients.append(pessoa[:])

print('\n')

for i in clients:
    if i[1] >= 18:
        print('{} é maior de idade;'.format(i[0]))
        maior += 1
    else:
        print('{} é menor de idade;'.format(i[0]))
        menor += 1

print("\nAo todo {} são de maior e {} são de menor.".format(maior, menor))


