N = int(input("Digite o tamanho da matriz: "))

matriz = [[0] * N for _ in range(N)]

superior = 0
inferior = N - 1
esquerda = 0
direita = N - 1

numero = 1

while numero <= N * N:
    for i in range(esquerda, direita + 1):
        matriz[superior][i] = numero
        numero += 1
    superior += 1

    for i in range(superior, inferior + 1):
        matriz[i][direita] = numero
        numero += 1
    direita -= 1

    if superior <= inferior:
        for i in range(direita, esquerda - 1, -1):
            matriz[inferior][i] = numero
            numero += 1
        inferior -= 1

    if esquerda <= direita:
        for i in range(inferior, superior - 1, -1):
            matriz[i][esquerda] = numero
            numero += 1
        esquerda += 1

for linha in matriz:
    print(linha)
