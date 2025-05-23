import numpy as np
import matplotlib.pyplot as plt

def construir_matriz_vandermonde(x, funcoes):
    """Constrói a matriz de Vandermonde usando funções base definidas pelo usuário."""
    n = len(x)
    X = np.zeros((n, len(funcoes)))
    for i in range(n):
        for j, f in enumerate(funcoes):
            X[i, j] = f(x[i])
    return X

def resolver_sistema_linear(A, b):
    """Resolve o sistema linear Ax = b usando eliminação de Gauss e substituição regressiva."""
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    # Eliminação de Gauss
    for i in range(n):
        max_row = np.argmax(np.abs(A[i:, i])) + i
        if A[max_row, i] == 0:
            raise ValueError("Sistema sem solução ou com infinitas soluções.")
        if max_row != i:
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
        for j in range(i+1, n):
            fator = A[j, i] / A[i, i]
            A[j, i:] -= fator * A[i, i:]
            b[j] -= fator * b[i]
    
    # Substituição regressiva
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    return x

def minimos_quadrados(x, y, funcoes):
    """Implementação do método dos mínimos quadrados usando funções base fornecidas."""
    X = construir_matriz_vandermonde(x, funcoes)
    coeficientes = resolver_sistema_linear(X.T @ X, X.T @ y)
    
    def funcao_ajustada(novo_x):
        return sum(c * f(novo_x) for c, f in zip(coeficientes, funcoes))
    
    return coeficientes, funcao_ajustada

def plot_ajuste(x, y, funcao_final):
    """Plota os pontos fornecidos e a curva ajustada."""
    x_plot = np.linspace(min(x) - 2, max(x) + 2, 200)
    y_plot_ajuste = funcao_final(x_plot)

    plt.scatter(x, y, color='red', label='Pontos Originais')
    plt.plot(x_plot, y_plot_ajuste, color='blue', label='Ajuste Calculado')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Ajuste pelo Método dos Mínimos Quadrados')
    plt.legend()
    plt.grid()
    plt.show()

# --- Código principal ---
if __name__ == "__main__":
    # 🔹 Passo 1: Definir os dados de entrada
    # Lista de coordenadas (x, y)
    pontos = [(-1.0, 2.05), (-0.75, 1.153), (-0.6, 0.45), (-0.5, 0.4), 
              (0.3, 0.5), (0.0, 0.0), (0.2, 0.2), (0.4, 0.6), 
              (0.5, 0.512), (0.7, 1.2), (1.0, 2.05)]  # Pontos reais fornecidos

    # Separando os pontos em arrays x e y
    x_exemplo = np.array([p[0] for p in pontos])
    y_exemplo = np.array([p[1] for p in pontos])

    # 🔹 Passo 2: Definir as funções base para ajuste (modelo quadrático)
    
    # Exemplos de funções base para diferentes tipos de ajuste:
    
    # 1. Ajuste quadrático (modelo 2º grau)
    funcoes_base = [lambda x: x**2]

    # funcoes_base = [lambda x: 1, lambda x: x, lambda x: x**2]  # Para ajuste quadrático (modelo 2º grau)
    
    # 2. Ajuste linear (modelo 1º grau)
    # funcoes_base = [lambda x: 1, lambda x: x]  # Modelo linear
    
    # 3. Ajuste cúbico (modelo 3º grau)
    # funcoes_base = [lambda x: 1, lambda x: x, lambda x: x**2, lambda x: x**3]  # Modelo cúbico
    
    # 4. Ajuste exponencial (modelo y = ae^bx), sem transformação (funções para modelos exponenciais)
    # funcoes_base = [lambda x: 1, lambda x: np.exp(x)]  # Exponencial (modelo sem transformação)
    
    # 5. Ajuste logarítmico (modelo y = a + b * log(x))
    # funcoes_base = [lambda x: 1, lambda x: np.log(x)]  # Logarítmico (modelo sem transformação)
    
    # 6. Ajuste seno (modelo y = a * sin(x) + b * cos(x))
    # funcoes_base = [lambda x: 1, lambda x: np.sin(x), lambda x: np.cos(x)]  # Modelo senoidal
    
    # 7. Ajuste exponencial com transformação logarítmica
    # log_y = np.log(y_exemplo)  # Transformar y em log(y)
    # funcoes_base = [lambda x: 1, lambda x: x]  # Ajuste linear aos valores logarítmicos
    
    # 🔹 Passo 3: Aplicar o método dos mínimos quadrados
    coef, func_ajustada = minimos_quadrados(x_exemplo, y_exemplo, funcoes_base)

    # 🔹 Passo 4: Plotar os dados e a curva ajustada
    plot_ajuste(x_exemplo, y_exemplo, func_ajustada)

    # 🔹 Passo 5: Exibir coeficientes ajustados
    print("Coeficientes ajustados:", coef)

    # 🔹 Passo 6: Testar a função ajustada para novos valores de x
    novos_x = np.array([6, 7, 8])
    novos_y = func_ajustada(novos_x)
    print("Novos valores de x:", novos_x)
    print("Valores ajustados de y:", novos_y)
