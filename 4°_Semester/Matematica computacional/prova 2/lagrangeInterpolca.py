import numpy as np
import matplotlib.pyplot as plt

# Função para calcular o polinômio de Lagrange L_i(x)
def lagrange_interpolation(pontos, x_val):
    n = len(pontos)
    resultado = 0
    for i in range(n):
        xi, yi = pontos[i]
        L = 1
        for j in range(n):
            if i != j:
                xj, _ = pontos[j]
                L *= (x_val - xj) / (xi - xj)
        resultado += yi * L
    return resultado

# Função para calcular e formatar o polinômio de Lagrange na forma tradicional (expandida)
def formatar_polinomio_expandido(pontos):
    n = len(pontos)
    polinomio = np.poly1d([0])
    
    for i in range(n):
        xi, yi = pontos[i]
        # Iniciar o polinômio L_i(x) como 1
        L = np.poly1d([1])
        
        # Construir o polinômio L_i(x) (fatores (x - xj))
        for j in range(n):
            if i != j:
                xj, _ = pontos[j]
                L = np.poly1d([1, -xj]) * L
        
        # Multiplicar pelo valor de y_i e adicionar ao polinômio total
        polinomio += yi * L
    
    return polinomio

# Função para exibir o polinômio em formato algébrico (com x^2, x, etc.)
def exibir_polinomio(polinomio):
    coeficientes = polinomio.coefficients
    grau = len(coeficientes) - 1
    termos = []
    
    # Formatação do polinômio em forma legível
    for i in range(grau, -1, -1):
        coef = coeficientes[grau - i]
        if coef != 0:
            if i == grau:
                termos.append(f"{coef:.4f}x^{i}")
            elif i == 0:
                termos.append(f"{coef:.4f}")
            else:
                termos.append(f"{coef:.4f}x^{i}")
    
    return " + ".join(termos)

# Pontos de exemplo para interpolação
pontos = [(-1, 4), (0, 1), (2, -1)]

# Calculando o polinômio de Lagrange expandido
polinomio = formatar_polinomio_expandido(pontos)

# Exibindo o polinômio no formato desejado
polinomio_str = exibir_polinomio(polinomio)
print(f"Polinômio Interpolador (Lagrange): {polinomio_str}")

# Gerando valores de x para o gráfico
x_vals = np.linspace(min(pontos, key=lambda p: p[0])[0], max(pontos, key=lambda p: p[0])[0], 100)
y_vals = [lagrange_interpolation(pontos, x) for x in x_vals]

# Plotando o gráfico
plt.plot(x_vals, y_vals, label="Polinômio Interpolador (Lagrange)", color='blue')
plt.scatter([p[0] for p in pontos], [p[1] for p in pontos], color='red', label="Pontos Dados")
plt.legend()
plt.title("Interpolação de Lagrange")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
