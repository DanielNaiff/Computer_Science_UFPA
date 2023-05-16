bigger = 0
lower = 0
c = 0
while True:
  c+=1
  n = int(input('Digite um número inteiro e positivo: '))
  if n >= 0:
    if c == 1:
      bigger = n
      lower = n
    else:
      if n > bigger:
        bigger = n
      if n < lower:
        lower = n
  else:
    break

print('O maior peso é ',bigger)
print('O menor peso é ',lower)