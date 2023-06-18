from random import randint
matriz = [[0 for c in range(5)]for l in range(5)]
diagonal = [0]*5
soma = 0

for l in range(5):
    for c in range(5):
        matriz[l][c] = randint(0,25)
        if (l+1) + (c+1) == 6:
            diagonal[c] = matriz[l][c]
            soma += diagonal[c]
print("\033[1;32mMatriz:\033[m")
for l in range(5):
    for c in range(5):
        print(f"[{matriz[l][c]:^5}]",end='')
    print()
print("\033[1;35mElementos da diagonal secundária:\033[m",diagonal)
print("\033[1;36mSoma dos elementos:\033[m",soma)