Algoritmo "ex01-aula8"
// 
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Daniel Naiff da Costa
// Data atual  : 19/05/2023
Var
// Seção de Declarações das variáveis 
vet: vetor[1..5] de real
soma: real
x: inteiro
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
para x de 1 ate 5 faca
     escreva("Digite um número: ")
     leia(vet[x])
     se x % 2 = 1 entao
        soma <- vet[x] + soma
     fimse
     
fimpara

escreva("Soma do números", soma)

Fimalgoritmo