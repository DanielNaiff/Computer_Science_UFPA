menores = 0
maiores = 0
while True:
    n = int(input('Digite a idade(digite -1 para parar):'))
    if n > 60:
        maiores += 1
    elif n >= 18 and n <= 60:
        continue 
    elif n > 0 and n < 18:
        menores += 1
    else:
        break
print('A quantidade de pessoas menores que 18: ', menores)
print('A quantidade de pessoas maiores que 60: ', maiores)    
