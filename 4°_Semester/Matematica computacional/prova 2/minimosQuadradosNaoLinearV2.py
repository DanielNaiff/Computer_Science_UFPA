import numpy as np
from minimosQuadradosV2 import MinimosQuadrados
import matplotlib.pyplot as plt

# Dados extraídos da tabela
x = np.array([-1.0, -0.7, -0.4, -0.1, 0.2, 0.5, 0.8, 1.0])
y = np.array([36.547, 17.264, 8.155, 3.852, 1.820, 0.860, 0.406, 0.246])

# Linearização: Aplicamos logaritmo natural para transformar o modelo y = a1 * e^(-a2 * x)
# na forma ln(y) = ln(a1) - a2 * x
y_transformed = np.log(y)

# Funções base para o ajuste de mínimos quadrados
funcoes_base = [lambda x: 1, lambda x: x]

# Ajuste dos coeficientes usando Mínimos Quadrados
coef = MinimosQuadrados(x, y_transformed, funcoes_base).coeficientes

# Recuperando os coeficientes a1 e a2
a1 = np.exp(coef[0])  # Como ln(a1) = coef[0], então a1 = exp(coef[0])
a2 = -coef[1]        # Como -a2 = coef[1], então a2 = -coef[1]

# Função ajustada
funcao_ajustada = lambda x: a1 * np.exp(-a2 * x)

# Função para plotar os resultados
def plotar(x, y):
    """Plota os pontos experimentais e a curva ajustada."""
    x_fit = np.linspace(min(x), max(x), 1000)
    y_fit = funcao_ajustada(x_fit)

    plt.scatter(x, y, color='red', label='Pontos experimentais')
    plt.plot(x_fit, y_fit, color='blue', label='Curva ajustada')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Ajuste por Mínimos Quadrados')
    plt.legend()
    plt.grid()
    plt.show()

# Plotando e imprimindo os coeficientes
plotar(x, y)
print(f"Coeficiente a1 ajustado: {a1}")
print(f"Coeficiente a2 ajustado: {a2}")
