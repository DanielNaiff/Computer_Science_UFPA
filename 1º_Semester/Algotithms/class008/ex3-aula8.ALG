Algoritmo "semnome"
// 
//  
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 19/05/2023
Var
// Se��o de Declara��es das vari�veis 
vet: vetor[1..10] de real
n: real
soma: real
maior: real
menor: real
media: real
l: logico
x: inteiro
y: inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
l <- verdadeiro
enquanto l = verdadeiro faca

         escreva("Digite um n�mero(de 1 ate 20): ")
         leia(n)
         se (n >= 1) e (n <= 20) entao
            x <- x + 1
            vet[x] <- n
            soma <- soma + vet[x]
            se x = 1 entao
               menor <- n
               maior <- n
            senao
                 se n > maior entao
                    maior <- n
                 fimse
                 se n < menor entao
                    menor <- n
                 fimse
            fimse
               
         senao
              escreval("Valor inv�lido")
         fimse
         
         se x = 10 entao
            l <- falso
         fimse

fimenquanto

media <- soma/10

escreval("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=")
para y de 1 ate 10 faca
     escreval("Valores do vetor:",vet[y])
fimpara

escreval("Maior numero: ",maior)
escreval("Menor numero:", menor)
escreval("Media:", media)
escreval("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=")
Fimalgoritmo