decimal = int(input("Digite um número decimal: "))
contador = decimal
c,q,n=0,0,0
while contador >0:
  contador=contador // 2
  n+=1
while n>=0:
  q = q + (decimal%2)*(10**c)
  decimal=decimal // 2
  c=c+1
  n=n-1
print(q)