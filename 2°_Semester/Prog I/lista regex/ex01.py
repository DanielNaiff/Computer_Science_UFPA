import re

strings = ["A","AA", "AAA", "AAAA", "AAAAA", "AAAAAA"]

regex= r'^(AA)*$'

for string in strings:
    if re.match(regex, string):
        print(f"A string '{string}' é uma sequência de letras 'A' de tamanho par.")
    else:
        print(f"A string '{string}' não é uma sequência de letras 'A' de tamanho par.")
