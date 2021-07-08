# Desafio consite em fazer passar dois numeros para uma função e retorna o resultado
# em binario no formato string

def add_binary(a,b):
    return str(bin(a+b))[2:]

print(add_binary(51,12))

bin()