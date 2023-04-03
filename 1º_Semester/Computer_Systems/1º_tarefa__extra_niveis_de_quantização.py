import itertools
import math

q = int(input("Digite o número de níveis de quantização:  "))
bits = int(math.log2(q))
print(f"Número de bits: {bits}")
v = [0, 1]
com_set = list(itertools.product(v, repeat = bits))
print(com_set)
