def func1(arg1, arg2):
  return arg1 * arg2

a = lambda x, y: x*y

print( a(2,2))

lista = [
  ['p1', 13],
  ['p2', 7],
  ['p3', 6],
  ['p4', 50],
  ['p5', 8],
]

# def func2(item ):
#   return item[1]

lista.sort(key=lambda i: i[1])
print(lista)