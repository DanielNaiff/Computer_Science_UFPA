Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o] 
// Professor    : Regiane
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Daniel Naiff
// Data atual  : 17/05/2023
Var
vet: vetor[1..20] de inteiro
menor: inteiro
x: inteiro
posicao: inteiro


Inicio
para x de 1 ate 20 faca
     escreva("Escreva um n�mero: ")
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
escreva("O menor n�mero � ", menor, " sua posicao � ", posicao )


Fimalgoritmo