import re

string = "amargo amora caio"

pattern = re.compile("[^c]")

x = re.findall(pattern, string) 

print(x)