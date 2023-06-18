matriz = [[0 for i in range(3)] for i in range(3)]
matriz3 = [[0 for i in range(3)] for i in range(3)]
for l in range(3):
    for c in range(3):
        matriz[l][c]= int(input(f"Digite um valor para a 1º matriz[{l+1}]x[{c+1}]:"))

print('\033[1;35m-=\033[m'*30)

for l in range(3):
    for c in range(3):
        matriz3[l][c]= int(input(f"Digite um valor para a 2º matriz[{l+1}]x[{c+1}]:"))

print('\033c',end='')
print("\033[1;32mSua 1º matriz é a seguinte:\033[m")

for l in range(3):
    for c in range(3):
        print(f"[{matriz[l][c]:^5}]",end='')
    print()

print("\033[1;32mSua 2º matriz é a seguinte:\033[m")

for l in range(3):
    for c in range(3):
        print(f"[{matriz3[l][c]:^5}]",end='')
    print()

matriz2= [[0 for i in range(3)] for i in range(3)]

print("\033[1;32mA multiplicação delas é:\033[m")

for l in range(3):
    for c in range(3):
        for m in range(3):
            matriz2[l][c] += matriz[l][m]*matriz3[m][c]
        print(f"[{matriz2[l][c]:^5}]",end='')
    print()

