Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor    : Regiane
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Daniel Naiff
// Data atual  : 17/05/2023
Var
vet: vetor[1..20] de inteiro
menor: inteiro
x: inteiro
posicao: inteiro


Inicio
para x de 1 ate 20 faca
     escreva("Escreva um número: ")
     leia(vet[x])
     se x = 1 entao
        menor <- vet[x]
        posicao <- x
     senao
          se vet[x] < menor entao
             menor <- n
             posicao <- x
          fimse
     fimse



fimpara
escreva("O menor número é ", menor, " sua posicao é ", posicao )


Fimalgoritmo