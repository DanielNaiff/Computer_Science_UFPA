def eliminacao_gauss(matriz_a):
    n = len(matriz_a)  # Obtém o número de variáveis ou equações (tamanho da matriz)
    
    # Eliminação para formar a matriz triangular superior
    for i in range(n):
        # Caso o elemento na diagonal principal seja zero, tentamos trocar linhas
        if matriz_a[i][i] == 0:
            for j in range(i + 1, n):
                # Procuramos uma linha abaixo onde o elemento na coluna i não seja zero
                if matriz_a[j][i] != 0:
                    # Troca de linhas para garantir que o pivô não seja zero
                    matriz_a[i], matriz_a[j] = matriz_a[j], matriz_a[i]
                    break

        # Normaliza a linha atual dividindo os elementos pela diagonal
        divisor = matriz_a[i][i]
        for k in range(i, n + 1):  # Inclui a última coluna (vetor de constantes)
            matriz_a[i][k] /= divisor
        
        # Eliminação das variáveis abaixo da linha i
        for j in range(i + 1, n):
            fator = matriz_a[j][i]  # Coeficiente que será subtraído da linha j
            for k in range(i, n + 1):  # Percorre as colunas da linha
                matriz_a[j][k] -= fator * matriz_a[i][k]  # Subtrai o múltiplo da linha i

    # Substituição regressiva para encontrar a solução
    solucao = [0] * n  # Inicializa a lista de soluções com zeros
    for i in range(n - 1, -1, -1):  # Percorre as linhas de baixo para cima
        solucao[i] = matriz_a[i][n]  # Começa com o valor da última coluna
        for j in range(i + 1, n):  # Subtrai os produtos dos valores já calculados
            solucao[i] -= matriz_a[i][j] * solucao[j]
    
    return solucao  # Retorna o vetor de soluções

# Exemplo de matriz aumentada (sistema linear com 4 variáveis)
matriz_a = [
    [1, 1, 0, 3, 4],  # Coeficientes da primeira equação e constante
    [2, 1, -1, 1, 1],  # Coeficientes da segunda equação e constante
    [3, -1, -1, 2, -3],  # Coeficientes da terceira equação e constante
    [-1, 2, 3, -1, 4]   # Coeficientes da quarta equação e constante
]

solucao = eliminacao_gauss(matriz_a)  # Chama a função para encontrar a solução
print("Solução:", solucao)  # Imprime a solução do sistema linear
