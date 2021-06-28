# 03 - Data com mês por extenso. Construa uma função que receba uma data no
# formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de
# AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
# Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo
# que nesses casos Fevereiro terá 29 dias

def mesLiteral(mes:int):
    dicio = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 
             8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
    return dicio[mes]

def dataPorExtenso(data:str):
    if len(data) != 10:
        return 'NULL'
    (dia, mes, ano) = data.split('/')
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    if mes in [1, 3, 5, 7, 8, 10, 12] and dia in range(1, 32):
        return '{} de {} de {}'.format(dia, mesLiteral(mes), ano)
    elif mes in [4, 6, 9, 11] and dia in range(1, 31):
        return '{} de {} de {}'.format(dia, mesLiteral(mes), ano)
    elif mes == 2 and dia in range(1, 29):
        return '{} de {} de {}'.format(dia, mesLiteral(mes), ano)
    elif mes == 2 and dia == 29 and ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            return '{} de {} de {}'.format(dia, mesLiteral(mes), ano)
    else:
        return 'NULL'


data = str(input('Digite uma data \'DD/MM/AAAA\': '))
print(dataPorExtenso(data))