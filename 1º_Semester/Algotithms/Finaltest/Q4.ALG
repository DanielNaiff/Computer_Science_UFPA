Algoritmo "semnome"
// 
//  
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Daniel naiff
// Data atual  : 7/11/2023
tipo reg_carros = registro
id: inteiro
marca: caractere
modelo: caractere
preco: real
fimregistro
Var
// Se��o de Declara��es das vari�veis 
vetor_carros: vetor [1..5] de reg_carros
i: inteiro
resposta: inteiro
id_a:inteiro
fator: inteiro

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
para i de 1 ate 5 faca
escreva("Digite o id do ve�culo",i,":")
leia(vetor_carros[i].id)
escreva("Digite a marca do ve�culo",i,":")
leia(vetor_carros[i].marca)
escreva("Digite o modelo do ve�culo",i,":")
leia(vetor_carros[i].modelo)
escreva("Digite o preco do ve�culo",i,":")
leia(vetor_carros[i].preco)
fimpara

 fator <- 1
 
escreval("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

enquanto fator <> 0 faca

escreval("1 - Buscar ID")
escreval("2 - Mudar o pre�o do ve�culo")
escreval(" 3 - Apagar veiculo do banco de dados")
escreva("4 - Sair do programa")
leia(resposta)

se resposta = 1 entao
escreva("Id do ve�culo para busca: ")
leia(id_a)
para i de 1 ate 5 faca
se id_a = vetor_carros[i].id entao
escreval("Marca:",vetor_carros[i].marca)
escreval("Modelo:",vetor_carros[i].modelo)
escreval("Pre�o:",vetor_carros[i].preco)
fimse
fimpara
escreval("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
fimse
se resposta = 2 entao

Escreva("Digite o id do ve�culo para mudar o pre�o:")
leia(id_a)
para i de 1 ate 5 faca
se id_a = vetor_carros[i].id entao
escreva("Novo pre�o:")
leia(vetor_carros[i].preco)
fimse
fimpara
escreval("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
fimse
se resposta = 3  entao

Escreva("Id do veiculopara apaga-lo (o id ficar� como 0000):")
leia(id_a)
para i de 1 ate 5 faca
se id_a = vetor_carros[i].id entao
vetor_carros[i].marca <- " "
vetor_carros[i].modelo <- " "
vetor_carros[i].preco <- 0.0
vetor_carros[i].id <- 0000
fimse
fimpara
escreval("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
fimse
se resposta = 4 entao

fator <- 0

fimse
fimenquanto
Fimalgoritmo