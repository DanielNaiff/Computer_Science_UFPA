Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o] 
// Professor    : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 17/05/2023
Var
// Se��o de Declara��es das vari�veis 
vet1: vetor[1..10] de inteiro
vet2: vetor[1..10] de inteiro
vet3: vetor[1..10] de inteiro
x: inteiro


Inicio
para x de 1 ate 10 faca
     escreva("Escreva um n�mero: ")
     leia(vet1[x])
fimpara
para x de 1 ate 10 faca
     escreva("Escreva um n�mero: ")
     leia(vet2[x])
fimpara
para x de 1 ate 10 faca
     vet3[x] <- vet1[x] + vet2[x]
fimpara
para x de 1 ate 10 faca
     escreva(vet3[x])
fimpara



Fimalgoritmo