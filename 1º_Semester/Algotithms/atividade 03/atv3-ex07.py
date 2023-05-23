n = int(input("Digite o valor do fatorial: "))
mult = 1
for i in range(n,1,-1):
    mult = i*mult
print(mult)