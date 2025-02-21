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
    return np.polyval(coeficientes[::-1], x_val)

# Função para formatar o polinômio como string
def formatar_polinomio(coeficientes):
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

# Pontos de exemplo para interpolação
pontos = [(-1, 4), (0, 1), (2, -1)]

# Resolvendo o sistema linear
coeficientes = interpolacao_linear(pontos)

# Exibindo o polinômio encontrado
polinomio = formatar_polinomio(coeficientes)
print(f"Polinômio Interpolador: {polinomio}")

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
