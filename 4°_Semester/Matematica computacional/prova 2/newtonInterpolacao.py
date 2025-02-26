import numpy as np
import matplotlib.pyplot as plt

# Função para calcular as diferenças divididas
def diferencas_divididas(x, y):
    n = len(x)
    tabela = np.zeros((n, n))
    tabela[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            tabela[i, j] = (tabela[i + 1, j - 1] - tabela[i, j - 1]) / (x[i + j] - x[i])

    return tabela

# Função para construir o polinômio de interpolação de Newton
def polinomio_newton(x, tabela):
    def p(x_val):
        n = len(x)
        resultado = tabela[0, 0]  # Começamos com o valor de y[0]
        produto = 1
        for i in range(1, n):
            produto *= (x_val - x[i - 1])
            resultado += tabela[0, i] * produto
        return resultado
    return p

# Função para exibir a tabela de diferenças divididas
def exibir_tabela(x, tabela):
    print("Tabela de Diferenças Divididas:")
    print("x\t\t" + "\t".join([f"Δ^{i}" for i in range(len(tabela))]))
    for i in range(len(tabela)):
        print(f"{x[i]}\t" + "\t".join([f"{tabela[i, j]:.4f}" for j in range(len(tabela))]))

# Função para testar um valor no polinômio de Newton
def testar_polinomio(polinomio, x_teste):
    return polinomio(x_teste)

# Exemplo de dados no formato (x, y)
pontos = [(-1, 4), (0, 1), (2, -1)]

# Separando os pontos em arrays x e y
x = np.array([p[0] for p in pontos])
y = np.array([p[1] for p in pontos])

# Calculando as diferenças divididas
tabela = diferencas_divididas(x, y)

# Exibindo a tabela
exibir_tabela(x, tabela)

# Gerando o polinômio interpolador
polinomio = polinomio_newton(x, tabela)

# Gerando os valores para o gráfico
x_grafico = np.linspace(min(x), max(x), 400)
y_grafico = np.array([polinomio(x_val) for x_val in x_grafico])

# Exibindo o polinômio corretamente
polinomio_str = f"P(x) = {tabela[0, 0]:.4f}"  # Começando com y[0]
for i in range(1, len(tabela)):
    produto_str = " * ".join([f"(x - {x[j]})" for j in range(i)])
    polinomio_str += f" + {tabela[0, i]:.4f} * {produto_str}"

print(f"\nPolinômio Resultante de Newton:\n{polinomio_str}")

# Plotando os pontos e o polinômio
plt.figure(figsize=(8, 6))
plt.plot(x_grafico, y_grafico, label="Polinômio de Newton", color='b')
plt.scatter(x, y, color='r', label="Pontos Dados")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolação de Newton')
plt.legend()
plt.grid(True)
plt.show()

# Solicitando ao usuário um valor de x para testar no polinômio
x_teste = 1.23
y_teste = testar_polinomio(polinomio, x_teste)

print(f"O valor de y correspondente a x = {x_teste} é: {y_teste:.4f}")
