import re

def extrairConteudoDaTag(nomeArquivo):
    with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            conteudo = re.search('(?<=<td>).+(?=</td>)', linha)
            if conteudo:
                with open('respostaQuestao04.txt', 'a', encoding='utf-8') as arquivoEscrito:
                    arquivoEscrito.write(f'{conteudo.group()}\n')
    return 'respostaQuestao04.txt'

extrairConteudoDaTag('Operadores.html')