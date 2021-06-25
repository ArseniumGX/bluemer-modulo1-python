# DESAFIO - Data com mês por extenso. 
# Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string 
# no formato 'D de mesPorExtenso de AAAA'. 
# 
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que
# Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro
# terá 29 dias.

from datetime import date

def dateFormat(param:str = 'DD/MM/AAAA'):
    (dia, mes, ano) = param.split('/')
    meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho',
         8: 'Agosto', 9: 'Stembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
        
    # try:
    data = date(int(ano), int(mes), int(dia))
    return data.strftime('%d de {} de %Y'.format(meses[date.month()]))
    # except:
    #     return 'NULL'
    
print(dateFormat('21/12/2012'))

# Feito, mas alterei algo e não ta mais funcionando