matriz = [[0 for i in range(3)] for i in range(3)]
for l in range(3):
    for c in range(3):
        matriz[l][c]= int(input(f"Digite um valor para matriz[{l+1}]x[{c+1}]:"))
print(matriz)

print('\033c',end='')
print("\033[1;32mSua matriz é a seguinte:\033[m")

for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]:^5}]",end='')
    print()
print("\033[1;32mA matriz anterior ao quadrado é:\033[m")

matriz2= [[0 for i in range(3)] for i in range(3)]

for l in range(3):
    for c in range(3):
        for m in range(3):
            matriz2[l][c] += matriz[l][m]*matriz[m][c]
        print(f"[{matriz2[l][c]:^5}]",end='')
    print()
