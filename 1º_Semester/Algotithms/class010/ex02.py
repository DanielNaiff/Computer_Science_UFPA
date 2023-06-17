matriz = [[0 for i in range(5)]for i in range(5)]

for l in range(5):
    for c in range(5):
        matriz[l][c] = int(input(f"Digite o elemento[{l+1}x{c+1}]:"))
print('\033c',end='')
print("\033[1;32mMatriz:\033[m")

for l in range(5):
    for c in range(5):
        print(f"[{matriz[l][c]:^5}]",end='')
    print()

print("\033[1;32mElementos da diagonal:\033[m")

for l in range(5):
    for c in range(5):
        if c == l:
            print(f"[{matriz[l][c]:^5}]",end='')
        else:
            print(f"[{0:^5}]",end='')
    print()