def gauss_jacobi(A, b, x_init=None, tol=1e-6, max_iter=50000):
    """
    Método de Gauss-Jacobi para resolver o sistema linear Ax = b.
    
    A: Matriz dos coeficientes (matriz n x n)
    b: Vetor do lado direito do sistema (vetor de tamanho n)
    x_init: Aproximação inicial (opcional). Se não fornecido, inicia com zero.
    tol: Tolerância para o erro, determina quando o método deve parar.
    max_iter: Número máximo de iterações permitidas.
    
    Retorna:
        x_new: A solução do sistema após a convergência ou o número máximo de iterações.
        k: O número de iterações realizadas até a convergência.
    """
    
    n = len(A)  # Número de equações (ou o tamanho da matriz A)
    
    # Se x_init não for fornecido, inicializa com um vetor de zeros
    if x_init is None:
        x = [0] * n  # Aproximação inicial x = [0, 0, ..., 0]
    else:
        x = x_init  # Se fornecido, usa o vetor de aproximação inicial fornecido
    
    x_new = [0] * n  # Vetor que armazenará a nova aproximação em cada iteração
    
    # Inicia o loop de iteração (máximo de max_iter iterações)
    for k in range(max_iter):
        # Loop sobre as equações (linhas da matriz A)
        for i in range(n):
            soma = b[i]  # Começa com o valor do lado direito b[i]
            
            # Subtrai os termos já calculados (A[i][j] * x[j]) onde j ≠ i
            for j in range(n):
                if i != j:
                    soma -= A[i][j] * x[j]  # A[i][j] * x[j] é o termo já conhecido
            x_new[i] = soma / A[i][i]  # Calcula o novo valor de x_new[i]
        
        # Calcula o erro entre as soluções antigas (x) e novas (x_new)
        erro = sum(abs(x_new[i] - x[i]) for i in range(n))  # Soma das diferenças absolutas
        
        # Se o erro for menor que a tolerância, significa que a solução convergiu
        if erro < tol:
            return x_new, k + 1  # Retorna a solução e o número de iterações realizadas
        
        # Atualiza x para a nova solução calculada para a próxima iteração
        x = x_new[:]  # Copia os valores de x_new para x
    
    # Se o número máximo de iterações for atingido sem convergência
    return x_new, max_iter  

# Definindo a matriz A e o vetor b para o exemplo
A = [
    [10, 2, 1],  # Primeira equação: 10x + 2y + z = 7
    [1, 5, 1],   # Segunda equação: x + 5y + z = -8
    [2, 3, 10]   # Terceira equação: 2x + 3y + 10z = 6
]

b = [7, -8, 6]  # Valores do lado direito das equações

# Aproximação inicial (pode ser qualquer vetor, aqui começamos com [0, 0, 0])
x_init = [0, 0, 0]

# Chamando a função de Gauss-Jacobi
solucao, iteracoes = gauss_jacobi(A, b, x_init)

# Exibindo a solução e o número de iterações
print("Solução encontrada:", solucao)
print("Número de iterações:", iteracoes)
