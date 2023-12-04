import re


texto_original = "Olá! Esta é uma string com 123 caracteres e alguns símbolos como *&$#!"

texto_limpo = re.sub(r'[^a-zA-Zà-ú\s]', '', texto_original)

print("Texto original:", texto_original)
print("Texto apenas com letras e espaços:", texto_limpo)