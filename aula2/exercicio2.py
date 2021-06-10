""" 02 - Qual o valor do troco?

    Defina uma variável para o valor de uma compra que custou R$100,98;

    Defina uma variável para o valor que o cliente pagou R$150,00;

    Defina uma variável que calcula o valor do troco e exiba-o no console com o valor final arredondado.
"""

valor_compra = 100.98
valor_pago = 150.00
troco = valor_pago - valor_compra

print(f'O seu troco é: R$ {troco:.2f}')
