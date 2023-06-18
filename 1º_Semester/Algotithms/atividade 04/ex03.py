from random import randint
vetor1 = []
vetor2 = []
vetor_diferenca = []
vetor_soma = []
vetor_multiplicacao = []

for i in range(10):
    vetor1 += [randint(0,10)]
    vetor2 += [randint(0,10)]
    vetor_diferenca += [vetor1[i]-vetor2[i]]
    vetor_soma += [vetor1[i]+vetor2[i]]
    vetor_multiplicacao += [vetor1[i]*vetor2[i]]
print("\033[1;33mVetor 1:\033[m",vetor1)
print("\033[1;33mVetor 2:\033[m",vetor2,"\n")
print("\033[1;32mVetor diferença:\033[m",vetor_diferenca)
print("\033[1;32mVetor soma:\033[m",vetor_soma)
print("\033[1;32mVetor multiplicação:\033[m",vetor_multiplicacao)