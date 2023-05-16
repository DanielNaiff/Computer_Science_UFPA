somador = 0
c = 0
for i in range(0,20):
  n = int(input('Digite um número:'))
  if n >= 0:
    somador = somador + n
  else:
    c += 1
print('A soma dos número positivos é:',somador)
print('A quantidade dos números negativos é:', c)
