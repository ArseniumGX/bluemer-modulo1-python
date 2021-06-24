# Faça um programa, com uma função que necessite de um parametro. 
# A função retorna o valor de caractere ‘P’, se seu argumento for 
# positivo, e ‘N’, se seu argumento for zero ou negativo. 

def sinalizacao(number:int = 0):
    if number > 0:
        return 'P'
    elif number < 0:
        return 'N'
    else:
        return 0


arg = sinalizacao(int((input('Digite um número: '))))
print(arg)