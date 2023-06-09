from random import randint
mat = [[0 for c in range(5)]for l in range(5)]

for l in range(5):
    soma_linha = 0
    for c in range(5):
        mat[l][c] = randint(0,25)
        soma_linha += mat[l][c]
        if soma_linha % 2 == 0:
            paridade = 'Par'
        else:
            paridade = 'Impar'
    print(f"\033[1;32mSoma da {l+1}º linha:\033[m",soma_linha,f"\033[1;34m- {paridade}\033[m")

for l in range(5):
    soma_coluna = 0
    for c in range(5):
        soma_coluna += mat[c][l]
        if soma_coluna % 2 == 1:
            paridade = 'Impar'
        else:
            paridade = 'Par'
    print(f"\033[1;33mSoma da {l+1}º coluna:\033[m",soma_coluna,f"\033[1;34m- {paridade}\033[m")

print("\033[1;36m\nMatriz:\033[m")
for l in range(5):
    for c in range(5):
        print(f"[{mat[l][c]:^5}]",end='')
    print()