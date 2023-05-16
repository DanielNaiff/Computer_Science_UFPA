candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
candidato5 = 0
candidato6 = 0
while True:
  voto = int(input('Escolha os candidatos(1,2,3,4, 5 - nulo e 6 - branco):'))
  if voto > 7:
    print('Voto inválido')
  elif voto == 1:
    candidato1 += 1
  elif voto == 2:
    candidato2 += 1
  elif voto == 3:
    candidato3 += 1
  elif voto == 4:
    candidato4 += 1
  elif voto == 5:
    candidato5 += 1
  elif voto == 6:
    candidato6 += 1
  elif voto == 0:
    break
print('Quantidade de votos do candidato 1:', candidato1)
print('Quantidade de votos do candidato 2:', candidato2)
print('Quantidade de votos do candidato 3:', candidato3)
print('Quantidade de votos do candidato 4:', candidato4)
print('Quantidade de votos nulos:', candidato5)
print('Quantidade de votos em branco:', candidato6)