while True:
    b = int(input("Digite um valor para B (deverá ser maior ou igual a 2):"))
    if b < 2:
        print('Valor inválido!')
    else:
        break
while True:
    n = int(input("Digite um valor para N(deverá ser maior do que 1):"))
    if n < 1:
        print("Valor inválido!")
    else:
        break
q = b**n
print("Valor:", q)
