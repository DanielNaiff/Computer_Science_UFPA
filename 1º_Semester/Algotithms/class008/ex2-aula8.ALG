Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor    : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 17/05/2023
Var
// Seção de Declarações das variáveis 
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