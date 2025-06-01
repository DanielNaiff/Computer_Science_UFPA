from funcoes import tail

def tamanho(list):
    if list == []:
        return 0
    return 1 + tamanho(tail(list))

list = [1, 2, 3, 4, 5]

print(tamanho(list))