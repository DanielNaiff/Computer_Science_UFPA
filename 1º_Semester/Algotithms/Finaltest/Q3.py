matriz_original = [[0] * 3 for i in range(3)]

for l in range(0,3):
    for c in range(0,3):
        matriz_original[l][c] = int(input(f"Digite o termo {l+1} x {c+1}:"))

matriz_resultado = [[0] * 3 for i in range(3)]

for i in range(3):
    for j in range(3):
        soma = 0
        for x in range(i+1):
            for y in range(j+1):
                soma += matriz_original[x][y]
        matriz_resultado[i][j] = soma

for linha in matriz_resultado:
    print(linha)
