def head(lst):
    return lst[0]
   
def tail(lst):
    return lst[1:]
   
def somaPar(lst):
    if len(lst) == 0:
        return 0
       
    if head(lst) % 2 == 0:
        return head(lst) + somaPar(tail(lst))
       
    if head(lst) % 2 == 1:
        return somaPar(tail(lst))
   
lst = [1,2,3,4,8]

print(somaPar(lst))