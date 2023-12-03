import re

string = 'Este é um teste de expressões teste regulares'

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'daniel', string, count = 1))

print('-=-=-=-=-=Modo economia de RAM-=-=-=-=-=')
regex = re.compile(r'teste')
print(regex.search(string))
print(regex.findall(string))
print(regex.sub('daniel', string, count = 1))