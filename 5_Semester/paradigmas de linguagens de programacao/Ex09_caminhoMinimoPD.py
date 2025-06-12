def menorCaminho(matriz, i, j, memo):
    n = len(matriz)

    if i >= n or j >= n:
        return float('inf')

    if i == n - 1 and j == n - 1:
        return matriz[i][j]

    if (i, j) in memo:
        return memo[(i, j)]

    direita = menorCaminho(matriz, i, j + 1, memo)
    baixo = menorCaminho(matriz, i + 1, j, memo)

    memo[(i, j)] = matriz[i][j] + min(direita, baixo)
    return memo[(i, j)]

memo = {}
   
matriz = [
        [5,8,0,7,4,9,6],
        [3,1,3,6,1,3,4],
        [5,2,9,2,5,0,3],
        [8,4,0,0,6,1,5],
        [0,9,0,8,4,9,3]
    ]
   
print(menorCaminho(matriz,0,0, memo))