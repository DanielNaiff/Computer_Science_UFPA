import numpy as np  # Importa a biblioteca NumPy, útil para operações matemáticas como exponencial e raiz quadrada

def calcular_area_trapezio(x0: float, x1: float, num_intervalos: int, funcao) -> float:
    """
    Calcula a integral definida de `funcao` no intervalo [x0, x1] utilizando a regra do trapézio.

    A Regra do Trapézio aproxima a área sob a curva utilizando trapézios em vez de retângulos.

    Parâmetros:
    x0 (float): Limite inferior da integral.
    x1 (float): Limite superior da integral.
    num_intervalos (int): Número de subintervalos. Deve ser maior que zero.
    funcao (callable): Função a ser integrada.

    Retorna:
    float: Aproximação da integral ou None caso `num_intervalos` seja inválido.
    """

    if num_intervalos <= 0:
        print("Erro: O número de subintervalos deve ser maior que zero.")
        return None  

    h = (x1 - x0) / num_intervalos  # Calcula o tamanho do passo
    soma = (funcao(x0) + funcao(x1)) / 2  # Primeiro e último termo com coeficiente 1/2

    # Soma dos termos internos da fórmula do trapézio
    for i in range(1, num_intervalos):
        x_i = x0 + i * h  # Calcula os pontos internos
        soma += funcao(x_i)  # Adiciona os valores da função nesses pontos

    return h * soma  # Aplica a fórmula da regra do trapézio


def calcular_regra13simpson(x0: float, x1: float, num_intervalos: int, funcao) -> float:
    """
    Calcula a integral definida de `funcao` no intervalo [x0, x1] utilizando a Regra 1/3 de Simpson.

    A Regra de Simpson utiliza aproximações quadráticas para estimar a área sob a curva.

    Parâmetros:
    x0 (float): Limite inferior da integral.
    x1 (float): Limite superior da integral.
    num_intervalos (int): Número de subintervalos (deve ser par).
    funcao (callable): Função a ser integrada.

    Retorna:
    float: Aproximação da integral ou None caso `num_intervalos` seja ímpar.
    """
    
    if num_intervalos % 2 != 0:
        print("Erro: O número de subintervalos deve ser par para a Regra de Simpson.")
        return None

    h = (x1 - x0) / num_intervalos  # Tamanho do passo
    soma = funcao(x0) + funcao(x1)  # Soma inicial com os extremos

    for i in range(1, num_intervalos):
        x_i = x0 + i * h  # Calcula os pontos internos
        
        # Alterna os coeficientes 4 e 2 conforme a regra de Simpson
        coeficiente = 4 if i % 2 == 1 else 2
        soma += coeficiente * funcao(x_i)

    return (h / 3) * soma  # Aplica a fórmula da Regra de Simpson


# Definição das funções a serem integradas
def f1(x):  # e^x
    return np.exp(x)

def f2(x):  # sqrt(x)
    return np.sqrt(x)

def f3(x):  # 1/sqrt(x)
    return 1 / np.sqrt(x)


# Parâmetros das integrais
intervalos = [4, 6]  # Número de subdivisões a serem testadas
funcoes = [(1, 2, f1, "∫ e^x dx de 1 a 2"),
           (1, 4, f2, "∫ sqrt(x) dx de 1 a 4"),
           (2, 14, f3, "∫ dx / sqrt(x) de 2 a 14")]

# Loop para calcular as integrais para cada função e cada número de intervalos
for x0, x1, funcao, descricao in funcoes:
    print(f"\n{descricao}")

    for n in intervalos:
        resultado_trapezio = calcular_area_trapezio(x0, x1, n, funcao)
        resultado_simpson = calcular_regra13simpson(x0, x1, n, funcao)

        print(f"\nCom {n} subintervalos:")
        print(f"Regra do Trapézio: {resultado_trapezio:.6f}")
        print(f"Regra de Simpson: {resultado_simpson:.6f}" if resultado_simpson is not None else "Regra de Simpson não aplicável")

