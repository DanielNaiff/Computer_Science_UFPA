from funcoes import head, tail

def existe(list, x):
    if list == []:
        return False
    
    if head(list) == x:
        return True
    
    return existe(tail(list), x)
    
list = [1, 2, 3, 4, 5]

print(existe(list, 6))
