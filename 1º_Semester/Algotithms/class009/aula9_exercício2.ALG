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
     para j de 1 ate 4 faca
          escreva("Digite o elemento", j, " da coluna",i,":")
          leia(matriz[i,j])
          soma <- soma + matriz[i,j]
     fimpara
fimpara
para i de 1 ate 4 faca
     para j de 1 ate 4 faca
          se i = j entao
             escreva(matriz[i,j]," ")
          senao
               escreva("-")
          fimse
     fimpara
     escreval(" ")
fimpara
escreval("Soma:",soma)

Fimalgoritmo