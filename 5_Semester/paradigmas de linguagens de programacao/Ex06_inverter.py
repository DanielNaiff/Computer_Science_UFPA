def head(lst):
    return lst[0]

def tail(lst):
    return lst[1:]

def inverter(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [head(lst)]

    return inverter(tail(lst)) + [head(lst)]

lst = [1, 2, 3, 4]
print(inverter(lst)) 