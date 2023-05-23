lista_12 = []
lista_secundaria = []

for i in range(0,12):
    n = int(input("Digite um valor inteiro para a lista:"))
    lista_12 += [n]

for i in lista_12:
    if i % 2 == 1:
        lista_secundaria += [lista_12[i]]
        continue

print('Vetor 1:', lista_12)
print('Vetor 2:', lista_secundaria)
