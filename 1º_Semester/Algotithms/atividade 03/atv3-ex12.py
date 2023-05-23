alturas = [0]*50
alturas_ordenadas = []
soma_alturas = 0
subtracao_quadrada = 0
contagem_alturas = 0

for i in range(0,50):
    n = float(input("Digite a altura: "))
    alturas += [n]
    soma_alturas += n

media = soma_alturas/50

print("-="*30)
print("A média das alturas é:", media)

for i in range(0,50):
    subtracao_quadrada += ((alturas[i] - media)**2) 

desvio_padrao = ((subtracao_quadrada)/50)**(1/2)

print("O desvio padrão é:",desvio_padrao)

frequencias = {}

for altura in alturas:
    if altura in frequencias:
        frequencias[altura] += 1
    else:
        frequencias[altura] = 1

moda = None
frequencia_maxima = 0

for altura in frequencias:
    frequencia = frequencias[altura]
    if frequencia > frequencia_maxima:
        moda = altura
        frequencia_maxima = frequencia

print("Moda das alturas:", moda)

alturas_ordenadas = []

for altura in alturas:
    inserido = False

    for i in range(len(alturas_ordenadas)):
        if altura < alturas_ordenadas[i]:
            alturas_ordenadas.insert(i, altura)
            inserido = True
            break

    if not inserido:
        alturas_ordenadas.append(altura)

indice_mediana = len(alturas_ordenadas) // 2
mediana = alturas_ordenadas[indice_mediana]

if len(alturas_ordenadas) % 2 == 0:
    mediana = (mediana + alturas_ordenadas[indice_mediana - 1]) / 2

print("Mediana das alturas:", mediana)
