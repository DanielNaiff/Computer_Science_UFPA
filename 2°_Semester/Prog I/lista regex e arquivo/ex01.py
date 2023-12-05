import re

def ler_arquivo(arquivo):
  with open(arquivo, 'r', encoding="utf-8") as f:
    arquivolido = f.read()
    palavras = re.findall(r'\b[aeiouAEIOU][a-zA-Z]*[aeiouAEIOU]\b', arquivolido)
    return palavras
  
def escrever_arquivo():
  lista_palavras = ler_arquivo('Operadores.html')
  with open('respostaQuestao01.txt', 'w', encoding="utf-8") as f:
    for palavra in lista_palavras:
      f.write(f'{palavra}\n')
    return len(lista_palavras), 'respostaQuestao01.txt'
  
print(escrever_arquivo())