import numpy as np
import matplotlib.pyplot as plt

# Função que define o modelo original não linear: y = ae^(bx)
def modelo(x, a, b):
    return a * np.exp(b * x)

# Dados fornecidos
x_dados = np.array([-1.0, -0.75, -0.6, -0.5, 0.3, 0.0, 0.2, 0.4, 0.5, 0.7, 1.0])
y_dados = np.array([36.547, 17.264, 8.155, 3.852, 1.820, 0.860, 0.406, 0.246, 1.2, 2.05, 1.5])

# Aplicando a transformação logarítmica: ln(y) = C1 + C2 * x
ln_y_dados = np.log(y_dados)

# Resolução da regressão linear (mínimos quadrados) para C1 e C2
A = np.vstack([x_dados, np.ones_like(x_dados)]).T
C2, C1 = np.linalg.lstsq(A, ln_y_dados, rcond=None)[0]

# Agora, recuperamos a e b
a = np.exp(C1)  # a = exp(C1)
b = C2          # b = C2

# Coeficientes encontrados
print(f'Coeficiente a ajustado: {a}')
print(f'Coeficiente b ajustado: {b}')

# Gerando valores de y para o ajuste com os parâmetros encontrados
x_ajuste = np.linspace(min(x_dados), max(x_dados), 1000)
y_ajuste = modelo(x_ajuste, a, b)

# Plotando os dados reais e a curva ajustada
plt.scatter(x_dados, y_dados, color='red', label='Dados reais')
plt.plot(x_ajuste, y_ajuste, label=f'Ajuste: y = {a:.2f}e^({b:.2f}x)', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Ajuste de Curva Não Linear')
plt.grid(True)
plt.show()

# Testando o modelo ajustado com alguns valores
x_test = np.array([-0.8, 0.1, 0.6])
y_test = modelo(x_test, a, b)
print("\nTestando com novos valores de x:")
for x_t, y_t in zip(x_test, y_test):
    print(f"x = {x_t}, y ajustado = {y_t:.2f}")
