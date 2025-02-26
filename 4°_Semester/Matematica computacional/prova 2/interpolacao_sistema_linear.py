import numpy as np
import matplotlib.pyplot as plt

# Função para resolver a interpolação usando sistema linear
def interpolacao_linear(pontos):
    # Extraindo as coordenadas dos pontos
    n = len(pontos)
    x = np.array([p[0] for p in pontos])
    y = np.array([p[1] for p in pontos])
    
    # Montando a matriz do sistema linear
    A = np.vander(x, increasing=True)  # Matriz de Vandermonde
    b = y
    
    # Resolvendo o sistema linear para encontrar os coeficientes
    coeficientes = np.linalg.solve(A, b)
    
    return coeficientes

# Função para avaliar o polinômio para um valor x
def avaliar_polinomio(coeficientes, x_val):
    """Avalia o polinômio interpolador para um valor de x."""
    return np.polyval(coeficientes[::-1], x_val)

# Função para formatar o polinômio como string
def formatar_polinomio(coeficientes):
    """Formata o polinômio como uma string, exibindo seus coeficientes."""
    termos = []
    grau = len(coeficientes) - 1
    for i, coef in enumerate(coeficientes):
        if coef != 0:
            if grau - i == 0:
                termos.append(f"{coef:.4f}")
            elif grau - i == 1:
                termos.append(f"{coef:.4f}x")
            else:
                termos.append(f"{coef:.4f}x^{grau - i}")
    return " + ".join(termos)

# Função para testar um valor específico de x no polinômio
def testar_valor_x(coeficientes, x_val):
    """Testa um valor x no polinômio interpolador."""
    return avaliar_polinomio(coeficientes, x_val)

# Pontos de exemplo para interpolação
# pontos = [ (0,-2.78), (0.5,-2.241), (1,-1.65), (1.5, -0.594), (2,1.34), (2.5,4.564)]
pontos = [(-1, 4), (0, 1), (2, -1)]

# Resolvendo o sistema linear
coeficientes = interpolacao_linear(pontos)

# Exibindo o polinômio encontrado
polinomio = formatar_polinomio(coeficientes)
print(f"Polinômio Interpolador: {polinomio}")

# Testando o valor de x = 1.2 no polinômio
x_test = 1.23
y_test = testar_valor_x(coeficientes, x_test)
print(f"Valor do polinômio para x = {x_test}: y = {y_test:.4f}")

# Gerando valores de x para o gráfico
x_vals = np.linspace(min(pontos, key=lambda p: p[0])[0], max(pontos, key=lambda p: p[0])[0], 100)
y_vals = [avaliar_polinomio(coeficientes, x) for x in x_vals]

# Plotando o gráfico
plt.plot(x_vals, y_vals, label="Polinômio Interpolador", color='blue')
plt.scatter([p[0] for p in pontos], [p[1] for p in pontos], color='red', label="Pontos Dados")
plt.legend()
plt.title("Interpolação Polinomial Usando Sistema Linear")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
