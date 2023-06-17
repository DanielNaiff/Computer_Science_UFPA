matriz = [[0 for i in range(5)]for i in range(5)]

a = int(input("Digite um valor para a matriz ser multiplicada:"))

for l in range(5):
    for c in range(5):
        matriz[l][c] = int(input(f"Digite o elemento[{l+1}x{c+1}]:"))
        matriz[l][c] = a*matriz[l][c]
print("\033c",end='')
print("\033[1;32mMatriz multiplicada pelo fator a:\033[m")

for l in range(5):
    for c in range(5):
            print(f"[{matriz[l][c]:^5}]",end='')
    print()
