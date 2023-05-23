n = int(input("Digite o limite a sequencia:"))
soma = 1
for i in range(1,n):
    soma = soma + 1/(1+i)
print("Valor:", soma)