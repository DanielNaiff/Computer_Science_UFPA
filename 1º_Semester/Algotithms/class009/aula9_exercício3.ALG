Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o] 
// Professor    : Regiane
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Daniel Naiff
// Data atual  : 30/05/2023
Var
// Se��o de Declara��es das vari�veis 
matriz: vetor[1..4,1..4] de real
soma, media: real
i, j: inteiro

Inicio
soma <- 0
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
para i de 1 ate 4 faca
     para j de 1 ate 3 faca
          escreva("Digite o elemento", j, " da coluna",i,":")
          leia(matriz[i,j])
     fimpara
fimpara
escreval("Matriz normal: ")
para i de 1 ate 4 faca
     para j de 1 ate 3 faca
         escreva(matriz[i,j]," ")
     fimpara
     escreval("")
fimpara
escreval("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
escreval("Matriz transposta: ")
para j de 1 ate 3 faca
     para i de 1 ate 4 faca
         escreva(matriz[i,j]," ")
     fimpara
     escreval("")
fimpara
escreval("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


Fimalgoritmo