senha = '123456'

lock = ''

while lock != senha:
    lock = str(input("Entre com a senha: "))
    if lock != senha:
        print("Try again!")
print('\n\nLogged!')