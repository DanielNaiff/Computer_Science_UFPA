Algoritmo "ex01-aula8"
// 
//  
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Daniel Naiff da Costa
// Data atual  : 19/05/2023
Var
// Se��o de Declara��es das vari�veis 
vet: vetor[1..5] de real
soma: real
x: inteiro
Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
para x de 1 ate 5 faca
     escreva("Digite um n�mero: ")
     leia(vet[x])
     se x % 2 = 1 entao
        soma <- vet[x] + soma
     fimse
     
fimpara

escreva("Soma do n�meros", soma)

Fimalgoritmo