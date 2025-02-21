def decomposicao_lu(A):
    """
    Decomposição LU de uma matriz quadrada A.
    Retorna as matrizes L (triangular inferior) e U (triangular superior).
    """
    n = len(A)  # Determina o tamanho da matriz A (n x n)
    
    # Inicializa a matriz L com zeros. L é triangular inferior, com diagonal igual a 1.
    L = [[0.0 for _ in range(n)] for _ in range(n)] 
    
    # Copia a matriz A para U. U será modificada durante o processo de decomposição.
    U = [row[:] for row in A]  
    
    # Loop sobre cada linha da matriz A
    for i in range(n):
        # Na matriz L, a diagonal é 1
        L[i][i] = 1

        # Para as linhas abaixo da diagonal de U
        for j in range(i + 1, n):
            # Calcula o fator de L[j][i] que será usado para eliminar os elementos abaixo da diagonal de U
            L[j][i] = U[j][i] / U[i][i]

            # Atualiza os elementos da linha j de U para "eliminar" os elementos abaixo da diagonal
            for k in range(i, n):
                U[j][k] -= L[j][i] * U[i][k]

    # Retorna as matrizes L e U resultantes da decomposição
    return L, U

def substituicao_direta(L, b):
    """
    Resolve o sistema Ly = b usando substituição direta (para matriz triangular inferior L)
    """
    n = len(L)  # Número de linhas/colunas de L (que é uma matriz quadrada)
    
    # Inicializa o vetor y com zeros (mesmo tamanho de b)
    y = [0.0] * n
    
    # Resolve o sistema Ly = b, linha por linha
    for i in range(n):
        # Calcula o valor de y[i] subtraindo as somas dos termos já calculados (L[i][j] * y[j])
        # As somas envolvem apenas elementos à esquerda de L[i][i]
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
    
    # Retorna o vetor y, solução intermediária
    return y

def substituicao_reversa(U, y):
    """
    Resolve o sistema Ux = y usando substituição reversa (para matriz triangular superior U)
    """
    n = len(U)  # Número de linhas/colunas de U (que é uma matriz quadrada)
    
    # Inicializa o vetor x com zeros (mesmo tamanho de y)
    x = [0.0] * n
    
    # Resolve o sistema Ux = y, mas de baixo para cima
    for i in range(n-1, -1, -1):
        # Calcula o valor de x[i], subtraindo os termos já calculados (U[i][j] * x[j])
        # A soma envolve apenas os elementos à direita de U[i][i]
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
    
    # Retorna o vetor x, solução final
    return x

def resolver_sistema(A, b):
    """
    Resolve o sistema linear Ax = b usando fatoração LU.
    """
    L, U = decomposicao_lu(A)  # Realiza a decomposição LU da matriz A
    y = substituicao_direta(L, b)  # Resolve Ly = b
    x = substituicao_reversa(U, y)  # Resolve Ux = y
    
    return x  # Retorna a solução x do sistema linear

# Exemplo de uso:
A = [
    [2, 3, -1],  # Matriz de coeficientes do sistema linear
    [4, 4, -3],  # Cada linha representa uma equação
    [2, -3, 1]
]

b = [5, 3, -1]  # Vetor do lado direito do sistema linear (resultados das equações)

# Chama a função para resolver o sistema
x = resolver_sistema(A, b)

# Exibe a solução do sistema Ax = b
print("Solução do sistema Ax = b:", x)
