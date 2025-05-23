import numpy as np
import matplotlib.pyplot as plt

# Função exponencial
def func(x, a, b):
    return a * np.exp(b * x)

# Gerar valores de x entre [0, 20]
x = np.linspace(0, 20, 50)

# Gerar valores de y = e^x + a, onde a é um ruído aleatório entre [-5, 5]
a_noise = np.random.uniform(-5, 5, size=x.shape)
y = np.exp(x) + a_noise

# Evitar valores negativos ou zero (pois aplicaremos log)
y[y <= 0] = np.min(y[y > 0])

# Transformação logarítmica
log_y = np.log(y)

# Regressão linear para encontrar os coeficientes
A = np.vstack([x, np.ones_like(x)]).T  # Matriz do sistema
b, log_a = np.linalg.lstsq(A, log_y, rcond=None)[0]  # Resolver o sistema

a = np.exp(log_a)  # Recuperar o coeficiente 'a'

# Gerar valores ajustados
x_fit = np.linspace(0, 20, 100)
y_fit = func(x_fit, a, b)

# Plot do gráfico
plt.scatter(x, y, color='red', label='Dados Originais')
plt.plot(x_fit, y_fit, color='blue', label=f'Ajuste: y = {a:.2f} * e^({b:.2f}x)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ajuste Exponencial')
plt.legend()
plt.grid()
plt.show()