import numpy as np
import matplotlib.pyplot as plt
from resolver_sistema import resolver_sistema_LU

# Gerar dados aleatórios
np.random.seed(42)  # Para reprodutibilidade
x = np.random.uniform(0, 20, 30)  # 30 valores aleatórios entre 0 e 20
a = np.random.uniform(-5, 5, 30)  # 30 valores aleatórios entre -5 e 5
y = np.exp(x) + a  # f(x) = e^x + a

# Definição da classe para ajuste por mínimos quadrados
class MinimosQuadrados:
    def __init__(self, x, y, funcoes_base):
        self.x = x
        self.y = y
        self.funcoes_base = funcoes_base
        self.coeficientes = self.ajustar()

    def ajustar(self):
        m = len(self.funcoes_base)
        A = np.zeros((m, m))
        b = np.zeros(m)

        for i in range(m):
            for j in range(m):
                A[i, j] = sum(self.funcoes_base[i](x_k) * self.funcoes_base[j](x_k) for x_k in self.x)
            b[i] = sum(y_k * self.funcoes_base[i](x_k) for x_k, y_k in zip(self.x, self.y))

        return resolver_sistema_LU(A, b)

    def predicao(self, x_val):
        return sum(c * f(x_val) for c, f in zip(self.coeficientes, self.funcoes_base))

    def constante_ajustada(self):
        return self.coeficientes[0]  # O coeficiente da função constante é o primeiro da lista

    def plotar(self):
        x_fit = np.linspace(min(self.x), max(self.x), 100)
        y_fit = self.predicao(x_fit)
        
        plt.scatter(self.x, self.y, color='red', label='Pontos experimentais')
        plt.plot(x_fit, y_fit, color='blue', label='Curva ajustada')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Ajuste por Mínimos Quadrados')
        plt.legend()
        plt.grid()
        plt.show()

# Definição das funções base (Aproximação polinomial de 2ª ordem para capturar a curva exponencial)
funcoes_base = [
    lambda x: 1,  # Termo constante
    lambda x: x,  # Termo linear
    lambda x: np.e**x  # Termo quadrático
]

# Criando e ajustando o modelo
modelo = MinimosQuadrados(x, y, funcoes_base)
modelo.plotar()

# Exemplo de predição
novo_x = 10
pred_y = modelo.predicao(novo_x)
constante = modelo.constante_ajustada()
print(f'Para x = {novo_x}, a predição de y é {pred_y}')
print(f'A constante ajustada é {constante}')
