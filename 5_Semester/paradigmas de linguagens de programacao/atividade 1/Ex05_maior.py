def head(lst):
    return lst[0]

def tail(lst):
    return lst[1:]

def maior(lst):
    if lst == []:
        return None
    if len(lst) == 1:
        return head(lst)
    
    max_tail = maior(tail(lst))
    if head(lst) > max_tail:
        return head(lst)
    else:
        return max_tail

lst = [2, 1, 4, 3]
print(maior(lst)) 
