Algoritmo "ex7"
// 
// Professor   : Regiane
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 17/05/2023
Var
n: inteiro
vetm: vetor[1..99] de real
vetd: vetor[1..99] de real
media: real
x: inteiro
soma: real
divisor: inteiro
diferenca: real
parada: inteiro

Inicio
divisor <- 0
parada <- 0
enquanto parada = 0 faca
   escreva("Escreva o tamanho do vetor:")
   leia(n)
   se n < 99 entao
      para x de 1 ate n faca
           escreva("Escreva um número:")
           leia(vetm[x])
           soma <- soma + vetm[x]
           divisor <- divisor + 1
      fimpara
      escreval("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
      para x de 1 ate n faca
           media <- soma/divisor
           diferenca <- vetm[x] - media
           vetd[x] <- diferenca
           escreval("Valores do vetor diferenca(em ordem): ", vetd[x])
      fimpara
      parada <- 1

   senao
        escreval("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        escreval("Boa tentativa! Valor muito alto!!!")
        escreval("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
   fimse
fimenquanto



Fimalgoritmo