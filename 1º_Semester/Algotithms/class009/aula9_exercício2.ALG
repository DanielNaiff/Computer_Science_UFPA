Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor    : Regiane
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Daniel Naiff
// Data atual  : 30/05/2023
Var
// Seção de Declarações das variáveis 
matriz: vetor[1..4,1..4] de real
soma, media: real
i, j: inteiro

Inicio
soma <- 0
// Seção de Comandos, procedimento, funções, operadores, etc... 
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