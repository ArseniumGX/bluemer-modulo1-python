# 4. Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário
# é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha
# mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.
def calcSalario(salario:float, horaExtra:float):
    if horaExtra > 40:
        return round(salario + (salario * 1.5/100) * (horaExtra - 40), 2)
    else:
        return round(salario, 2)

salario = float(input('Informeo salário do funcionário: '))
horasExtas = float(input('Informe a quantidade de horas trabalhadas: '))
print(calcSalario(salario, horasExtas))
