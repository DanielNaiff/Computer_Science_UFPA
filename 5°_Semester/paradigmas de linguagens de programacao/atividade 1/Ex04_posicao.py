def head(lst):
    return lst[0]

def tail(lst):
    return lst[1:]
   
def posicao(lst, n):
    if lst == []:
        return -1
       
    if head(lst) == n:
        return 0
   
    posicao(tail(lst), n)
   
    if posicao(tail(lst), n) == -1:
        return -1
    else:
        return posicao(tail(lst), n) + 1


   
lst = [1,2,3,4]

print(posicao(lst, 3))
print(posicao(lst, 5))