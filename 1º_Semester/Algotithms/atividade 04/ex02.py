from random import randint
lista1 = []
lista_par = []
lista_impar = []
menor = maior = 0

for i in range(20):
    lista1 += [int(input(f"\033[1;31mDigite o {i+1}º valor:\033[m"))]#[randint(0,100)] 
    if lista1[i] % 2 == 0:
        lista_par += [lista1[i]]
    else:
        lista_impar += [lista1[i]]

n = len(lista_par)

lista2 = [0]*n

#Oi professora, após algumas horas pensando, finalmente consegui resolver a lógica do problema

#ela se baseia em primeiro achar o menor e o maior item de uma lista par ou impar(loop for) e em seguida
#adicionando esses dois números em listas secundarias(lista 2, lista 3) e logo depois removendo 
#os mesmos números das listas pares ou impares até a quantidade de números chegar a zero(loop while)
# 
# infelizmente não achei outro modo de resolver esse problema sem usar os métodos count(), remove() e o reverse()
while True:
    n = len(lista_par)

    for i in range(n):
        if i == 0:
            menor = lista_par[i]
            maior = lista_par[i]
        else:
            if lista_par[i] < menor:
                menor = lista_par[i]
            elif lista_par[i] > maior:
                maior = lista_par[i]
            lista2[0] = menor
            lista2[n-1] = maior

    if lista_par.count(maior) != 0:
        lista_par.remove(maior)
    elif lista_par.count(menor) != 0:
        lista_par.remove(menor)
    if len(lista_par) == 0:
        break

n = len(lista_impar)

lista3 = [0]*n

while True:
    n = len(lista_impar)

    for i in range(n):
        if i == 0:
            menor = lista_impar[i]
            maior = lista_impar[i]
        else:
            if lista_impar[i] < menor:
                menor = lista_impar[i]
            elif lista_impar[i] > maior:
                maior = lista_impar[i]
            lista3[0] = menor
            lista3[n-1] = maior

    if lista_impar.count(maior) != 0:
        lista_impar.remove(maior)
    elif lista_impar.count(menor) != 0:
        lista_impar.remove(menor)
    if len(lista_impar) == 0:
        break
lista3.reverse()
print("\033c",end='')
print("\033[1;32mVetor original:\033[m",lista1,"\n")
print("\033[1;33mVetor par em ordem crescente:\033[m",lista2,"\n")
print("\033[1;34mVetor impar em ordem decrescente:\033[m",lista3,"\n")
