n = int(input("Digite o número de linhas para o Triângulo de Pascal: "))

triangulo = [[1]]

for i in range(1, n):
    linha = [1]
    linha_anterior = triangulo[i-1]
    j = 1
    while j < i:
        linha += [linha_anterior[j-1] + linha_anterior[j]]
        j += 1
    linha += [1]
    triangulo += [linha]

for linha in triangulo:
    num_espaço = n - len(linha)
    print(" " * num_espaço, end="")
    
    for numero in linha:
        print(numero, end=" ")
    
    print()