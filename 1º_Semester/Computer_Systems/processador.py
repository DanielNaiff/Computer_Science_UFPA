f = input("Selecione a operação:")
a = int(input("Escolha o primeiro bit: "))
b = int(input("Escolha o segundo bit: "))

saida = 0

if f == '00':
    saida = a and b
    print(saida)
elif f == '01':
    saida = a or b
    print(saida)
elif f == '10':
    saida = not b
    print(saida)
else:
    saida = a + b
    print(bin(saida))