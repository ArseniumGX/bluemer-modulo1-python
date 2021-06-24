# Funcões
# São rotinas que executam determinado procedimento
# escopo = espaço de trabalho
# parametros

def soma(a:int, b:int):
    return a + b

def media(notas:list):
    ## teste
    return round(sum(notas)/len(notas),1)

print(media([5.6, 6.9, 7.6, 9.9]))
print(media)

