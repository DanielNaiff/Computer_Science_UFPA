num1 = int(input("N1: "))
num2 = int(input("N2: "))

if num1 > num2:
   maior = num1
else:
    maior = num2

while True:
    if maior % num1 == 0 and maior % num2 == 0:
        print("O MMC entre", num1, "e", num2, "é", maior)
        break
    maior += 1