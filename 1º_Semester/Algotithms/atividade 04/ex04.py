matriz = [[0 for c in range(3)]for l in range(2)]

for l in range(2):
    for c in range(3):
        matriz[l][c] = int(input(f"Digite o elemento[{l+1}x{c+1}] da 1º matriz:"))
print("\033c",end='')

for l in range(2):
    for c in range(3):
        matriz[l][c] += int(input(f"Digite o elemento[{l+1}x{c+1}] da 2º matriz:"))
print("\033c",end='')

print("\033[1;32mA soma das matrizes é:\033[m")

for l in range(2):
    for c in range(3):
        print(f"[{matriz[l][c]:^5}]",end='')
    print()