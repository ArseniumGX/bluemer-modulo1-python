""" 
Menu - Elabore um programa que mostre o seguinte menu na tela:

Cadastro de Clientes
0 - Fim
1 - Inclui
2 - Altera
3 - Exclui
4 - Consulta
Digite uma opção: 

Ao digitar um valor para a opção, o programa exibe qual opção foi escolhida.

Você escolheu a opção '0'.
"""

print(f'''
0 - Fim
1 - Inclui
2 - Altera
3 - Exclui
4 - Consulta
''')

opcao = int(input('Digite uma opção: '))

print(f'\nVocê escolheu a opção \'{opcao}\'.')
