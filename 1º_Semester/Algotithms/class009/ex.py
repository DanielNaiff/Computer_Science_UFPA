vetor = []
vetor_impar = []
vetor_par = []

for i in range(0,10):
    vetor += [int(input("Digite um valor para o vetor:"))]
    if vetor[i] % 2 == 1:
        vetor_impar += [vetor[i]]
    else:
        vetor_par += [vetor[i]]
print("Vetor principal:",vetor)
print("Vetor impar:",vetor_impar)
print("Vetor par:",vetor_par)
