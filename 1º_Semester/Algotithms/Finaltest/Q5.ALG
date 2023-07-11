Algoritmo "semnome"
//
//
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Daniel naiff
// Data atual  : 7/11/2023
tipo reg_hospital = registro
id: inteiro
doenca: caractere
nome: caractere
idade: inteiro
fimregistro
Var
// Seção de Declarações das variáveis
vetora: vetor [1..5] de reg_hospital
i: inteiro
resposta: inteiro
id_a:inteiro
fator: inteiro
media:real
soma:inteiro

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
para i de 1 ate 2 faca
escreva("Digite o id do paciente",i,":")
leia(vetora[i].id)
escreva("Digite o nome do paciente",i,":")
leia(vetora[i].nome)
escreva("Digite a doença do paciente",i,":")
leia(vetora[i].doenca)
escreva("Digite a idade do paciente",i,":")
leia(vetora[i].idade)
fimpara

 fator <- 1

escreval("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

enquanto fator <> 0 faca

escreval("1 - Buscar ID")
escreval("2 - Atualizar a doença")
escreval(" 3 - Remover paciente")
escreval("4 - Ver a média das idades dos pacientes")
escreva("5 - Sair do programa")
leia(resposta)

se resposta = 1 entao
escreva("Id do paciente para busca: ")
leia(id_a)
para i de 1 ate 5 faca
se id_a = vetora[i].id entao
escreval("Nome:",vetora[i].nome)
escreval("Doença:",vetora[i].doenca)
escreval("Idade:",vetora[i].idade)
fimse
fimpara
escreval("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
fimse
se resposta = 2 entao

Escreva("Digite o id do paciente:")
leia(id_a)
para i de 1 ate 5 faca
se id_a = vetora[i].id entao
escreva("Nova doença:")
leia(vetora[i].doenca)
fimse
fimpara
escreval("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
fimse
se resposta = 3  entao

Escreva("Id do paciente para apaga-lo (o id ficará como 0000):")
leia(id_a)
para i de 1 ate 5 faca
se id_a = vetora[i].id entao
vetora[i].nome <- " "
vetora[i].idade <- 0
vetora[i].doenca <- " "
vetora[i].id <- 0000
fimse
fimpara
escreval("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
fimse

se resposta = 4 entao
para i de 1 ate 5 faca
soma <- soma + vetora[i].idade
fimpara
media <- soma/2
escreval("A média é",media)
escreval("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
fimse

se resposta = 5 entao

fator <- 0

fimse
fimenquanto
Fimalgoritmo