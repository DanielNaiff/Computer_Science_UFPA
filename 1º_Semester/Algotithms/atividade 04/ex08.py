from random import randint
matriz = [[0 for c in range(10)]for l in range(10)]
diagonal = [0]*10
for l in range(10):
    for c in range(10):
        matriz[l][c] = randint(0,100)
        if l == c:
            diagonal[c] = matriz[l][c]
print("\033[1;32mMatriz:\033[m")
for l in range(10):
    for c in range(10):
        print(f"[{matriz[l][c]:^5}]",end='')
    print()
print("\033[1;32mVetor:\033[m",diagonal)