from random import randint
matriz = [[0 for c in range(4)]for l in range(4)]
soma = 0

for l in range(4):
    for c in range(4):
        matriz[l][c] = randint(0,25)
        if matriz[l][c] > 10:
            soma += 1
print("\033[1;32mMatriz:\033[m")
for l in range(4):
    for c in range(4):
        print(f"[{matriz[l][c]:^5}]",end='')
    print()
print("\033[1;32mQuantidade de elementos maiores que 10:\033[m",soma)