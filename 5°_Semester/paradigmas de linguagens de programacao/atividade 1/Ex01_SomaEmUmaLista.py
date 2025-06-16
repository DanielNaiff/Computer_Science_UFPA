from funcoes import head, tail

def soma(list):
    if list == []:
        return 0
    return head(list) + soma(tail(list))

list = [1, 2, 3, 4]

print(soma(list))