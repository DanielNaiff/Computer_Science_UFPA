Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o] 
// Professor    : Antonio Carlos Nicolodi 
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 17/05/2023
Var
// Se��o de Declara��es das vari�veis 
vet: vetor[1..50] de real
soma: real
divisor: real
x: inteiro


Inicio
soma <- 1
para x de 1 ate 50 faca
     divisor <- vet[x] + (2*x)
     soma <- 1/divisor + soma

fimpara
escreva(soma)


Fimalgoritmo