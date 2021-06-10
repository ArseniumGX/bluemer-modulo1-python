""" 01 
    
    E os 10% do garçom?**

    Defina uma variável para o valor de uma refeição que custou R$ 42,54;

    Defina uma variável para o valor da taxa de serviço que é de 10%;

    Defina uma variável que calcula o valor total da conta e exiba-o no console com essa
    formatação: R$ XXXX.XX.
"""

valor = 42.54
taxa = 10

total = valor + ((valor*taxa)/100)

print(f'O valor total é: R$ {total:.2f}')