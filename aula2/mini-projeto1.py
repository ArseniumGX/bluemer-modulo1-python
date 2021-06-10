""" 
01 - Conversor de moedas

Crie um programa que solicite um um valor em real ao usuário e converta esse valor, para:

    DOLAR,
    EURO,
    LIBRA ESTERLINA,
    DÓLAR CANADENSE,
    PESO ARGENTINO,
    PESO CHILENO.

Para esse exercício você precisará realizar uma pesquisa para saber a cotação de cada moeda 
em real. Mostrar o resultado no formato $ XXXX.XX
"""

moeda_real = int(input("Digite o valor em reais para converter: "))

dolar = moeda_real / 5.02
euro = moeda_real / 6.13
libra = moeda_real / 7.13
dolar_canada = moeda_real / 4.16
peso_argentino = moeda_real / 0.053
peso_chileno = moeda_real / 0.007

print(f'\n\nR$ {moeda_real:.2f} convertido nas seguintes moedas\n\n')
print(f'Em dolar: US$ {dolar:.2f}')
print(f'Em euro: € {euro:.2f}')
print(f'Em libras esterlinas: £ {libra:.2f}')
print(f'Em dolar canadense: C$ {dolar_canada:.2f}')
print(f'Em peso argentino: $ {peso_argentino:.2f}')
print(f'Em peso chileno: CLP $ {peso_chileno:.2f}')