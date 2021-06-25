# 3. Faça um programa com uma função chamada somaImposto. A função possui dois
# parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
# porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o
# valor de custo para incluir o imposto sobre vendas.
def somaImposto(taxaImposto:str, custo:float):
    return round(custo + (custo * int(taxaImposto.replace('%','')) /100), 2)
item = float(input('Digite o valor do item: '))
taxa = str(input('Digite a tava de imposta com ou o sinal de porcentagem: '))
print(somaImposto(taxa, item))
