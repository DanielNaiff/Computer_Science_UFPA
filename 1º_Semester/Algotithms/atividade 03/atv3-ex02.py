contador = 0
soma = 0
while True:
    n = int(input("Digite um número:"))
    soma = n + soma
    contador += 1
    if n < 0:
        soma = (-1*n) + soma
        break
contador -= 1
media = soma/contador
print('Média dos valores: ',media)