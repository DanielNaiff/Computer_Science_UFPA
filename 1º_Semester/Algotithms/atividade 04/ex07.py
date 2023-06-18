from random import randint
mat = []
soma_linha = soma_coluna = 0
for l in range(5):
    linha = []
    for c in range(5):
        linha += [randint(0,25)]

    matriz += [linha]
print("\033[1;32mMatriz:\033[m")
for l in range(5):
    for c in range(5):
        print(f"[{matriz[l][c]:^5}]",end='')
    print()