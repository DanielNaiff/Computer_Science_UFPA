lista1 = []
lista2 = []
for i in range(10):
    lista1 += [int(input(f"\033[1;31mDigite um valor inteiro:\033[m"))]
    if i % 2 == 0:
        lista2 += [lista1[i]/2]
    else:
        lista2 += [lista1[i]*3]
print("\033c",end='')
print(f"\033[1;32mVetor 1:\033[m",lista1)
print(print(f"\033[1;32mVetor 2:\033[m",lista2))
