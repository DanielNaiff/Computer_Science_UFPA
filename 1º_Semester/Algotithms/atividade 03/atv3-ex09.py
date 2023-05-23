num1 = int(input("N1: "))
num2 = int(input("N2: "))

if num1 < num2:
   menor = num1
else:
    menor = num2

mdc = 1

for divisor in range(2, menor + 1):
    if num1 % divisor == 0 and num2 % divisor == 0:
        mdc = divisor

print("O MDC entre", num1, "e", num2, "é", mdc)
