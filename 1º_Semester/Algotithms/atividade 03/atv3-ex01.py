contador = 0
while True:
    n = int(input("Digite um número:"))
    contador += 1
    if n < 0:
        break
print("A quantidade de números foi", contador-1) 
