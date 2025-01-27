import numpy as np

# Define as funções do sistema
def f(x):
    # Sistema de equações não lineares
    return np.array([x[0] + x[1] - 5, x[0]**2 + x[1]**2 - 25])

# Define a matriz Jacobiana
def jacobian(x):
    return np.array([[1, 1], [2*x[0], 2*x[1]]])

# Método de Newton para sistemas não lineares
def newton_method(f, jacobian, x0, tol=1e-6, max_iter=100):
    x = np.array(x0, dtype=float)  # ponto inicial
    for i in range(max_iter):
        fx = f(x)
        J = jacobian(x)
        
        # Verifica se a matriz Jacobiana é singular
        if np.linalg.det(J) == 0:
            print("Jacobiana singular! Tentando com outro ponto inicial.")
            return None
        
        # Solução do sistema J * Δx = -f(x)
        delta_x = np.linalg.solve(J, -fx)
        
        # Atualiza o valor de x
        x = x + delta_x
        
        # Checa a condição de parada (tolerância)
        if np.linalg.norm(delta_x) < tol:
            print(f"Solução encontrada após {i+1} iterações")
            return x
        
    raise ValueError("Método de Newton não convergiu!")

# Ponto inicial
x0 = [-1, 6]

# Resolver o sistema
solucao = newton_method(f, jacobian, x0)
if solucao is not None:
    print("Solução do sistema:", solucao)
