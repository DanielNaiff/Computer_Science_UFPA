vetor = [0]*5
numero = int(input("Digite um numero alvo:"))

for i in range(0,5):
    vetor[i] = int(input("Digite um número para o vetor:"))
print(vetor)

t = 1

while True:
    for p in range(t,6):
        for s in range(t,6):
            if p + s == numero:
                t = p + 1
                print(f"A soma entre {p} e {s} é igual a {numero}")
    break