# retorna a soma de um entervalo entre dois numeros incluindo eles

def get_sum(a,b):
    return a or b if a == b else sum(list(range(min(a,b), max(a,b)+1)))

print(get_sum(0, -15))