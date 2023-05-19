Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor    : Antonio Carlos Nicolodi 
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 17/05/2023
Var
// Seção de Declarações das variáveis 
vet1: vetor[1..10] de inteiro
vet2: vetor[1..10] de inteiro
vet3: vetor[1..10] de inteiro
x: inteiro


Inicio
para x de 1 ate 10 faca
     escreva("Escreva um número: ")
     leia(vet1[x])
fimpara
para x de 1 ate 10 faca
     escreva("Escreva um número: ")
     leia(vet2[x])
fimpara
para x de 1 ate 10 faca
     vet3[x] <- vet1[x] + vet2[x]
fimpara
para x de 1 ate 10 faca
     escreva(vet3[x])
fimpara



Fimalgoritmo