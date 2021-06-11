""" Reajuste salarial

As empresas @.com resolveram dar um aumento de salário aos seus colaboradores 
e lhe contrataram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo
o seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%

    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%

    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%

    salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:

    o salário antes do reajuste;

    o percentual de aumento aplicado;

    o valor do aumento;

    o novo salário, após o aumento."
"""

salario = float(input("Entre com o salário do funcionário: "))
reajuste = 0.0

if salario <= 280:
    reajuste = salario + (salario * 20) / 100
    print(f'''
    Seu salário era de R$ {salario:.2f}. 
    Foi aplicado 20% de reajuste resultando em aumento de R$ {((salario * 20) / 100):.2f}
    Seu novo salário é de R$ {reajuste:.2f}''')

elif salario > 280 and salario <= 700:
    reajuste = salario +  (salario * 15) / 100
    print(f'''
    Seu salário era de R$ {salario:.2f}. 
    Foi aplicado 15% de reajuste resultando em aumento de R$ {((salario * 15) / 100):.2f}
    Seu novo salário é de R$ {reajuste:.2f}''')

elif salario > 700 and salario <= 1500:
    reajuste = salario +  (salario * 10) / 100
    print(f'''
    Seu salário era de R$ {salario:.2f}. 
    Foi aplicado 10% de reajuste resultando em aumento de R$ {((salario * 10) / 100):.2f}
    Seu novo salário é de R$ {reajuste:.2f}''')

else:
    reajuste = salario + (salario * 5) / 100
    print(f'''
    Seu salário era de R$ {salario:.2f}. 
    Foi aplicado 5% de reajuste resultando em aumento de R$ {((salario * 5) / 100):.2f}
    Seu novo salário é de R$ {reajuste:.2f}''') 
