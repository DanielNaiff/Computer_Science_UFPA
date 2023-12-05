import re
def tres_vogais(arquivo):
  with open(arquivo, 'r', encoding='utf-8') as f:
    arquivo_lido = f.read()
    palavras = re.findall(r'[\w]+', arquivo_lido)
  for palavra in palavras:
            procurar3Vogais = re.search(r'.*[aeiouAEIOU].*[aeiouAEIOU].*[aeiouAEIOU].*', palavra)
            if procurar3Vogais:
                with open('respostaQuestao03.txt', 'a', encoding='utf-8') as resposta:
                    resposta.write(f'{procurar3Vogais}\n')
  return len(palavras), 'respostaQuestao03.txt'
   
print(tres_vogais('Operadores.html'))