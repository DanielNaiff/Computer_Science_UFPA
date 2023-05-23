paisa = 35000000
paisb = 48000000
t = 0
while paisa < paisb:
    paisa = (0.03*paisa) + paisa
    paisb = (0.02*paisb) + paisb
    t += 1
print(" Quantidade de tempo", t)