soma_notas = 0
quantidade_notas = 50

for i in range(0,quantidade_notas):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma_notas += nota

media = soma_notas / quantidade_notas

acima_media = 0
abaixo_media = 0

for i in range(0,quantidade_notas):
    nota = float(input(f"Digite a nota {i+1}: "))
    if nota > media * 1.1:  
        acima_media += 1
    elif nota < media * 0.9: 
        abaixo_media += 1

print("Quantidade de notas:")
print("10% acima da média:", acima_media)
print("10% abaixo da média:", abaixo_media)