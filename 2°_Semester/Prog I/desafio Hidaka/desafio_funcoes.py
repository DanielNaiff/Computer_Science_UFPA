def validar_nome(nome):
    if not nome.isalpha():
        raise ValueError("Nome inválido. Deve conter apenas letras.")

def validar_ano(ano):
    if not ano.isdigit() or int(ano) < 1903:
        raise ValueError("Ano inválido. Deve ser igual ou maior que 1903.")

def validar_sexo(sexo):
    if sexo.upper() not in ["M", "F"]:
        raise ValueError("Sexo inválido. Digite 'M' ou 'F'.")

def validar_cpf(cpf):
    if not cpf.isdigit() or len(cpf) < 11:
        raise ValueError("CPF inválido. Deve conter apenas números e ter no mínimo 11 dígitos.")

def validar_rg(rg):
    if not rg.isdigit() or len(rg) < 7:
        raise ValueError("RG inválido. Deve conter apenas números e ter no mínimo 7 dígitos.")

def obter_entrada(mensagem, validacao, mensagem_erro):
    while True:
        entrada = input(mensagem)
        try:
            validacao(entrada)
            return entrada
        except ValueError as ve:
            print(mensagem_erro)

def cadastro_nome():
    mensagem = "Digite o seu nome: "
    mensagem_erro = "Nome inválido. Deve conter apenas letras."
    return obter_entrada(mensagem, validar_nome, mensagem_erro)

def cadastro_nascimento():
    mensagem = "Digite o seu nascimento (xxxx): "
    mensagem_erro = "Ano inválido. Deve ser igual ou maior que 1903 e conter apenas números."
    return obter_entrada(mensagem, validar_ano, mensagem_erro)

def cadastro_sexo():
    mensagem = "Digite o seu sexo (M/F): "
    mensagem_erro = "Sexo inválido. Digite 'M' ou 'F'."
    return obter_entrada(mensagem, validar_sexo, mensagem_erro)

def cadastro_cpf():
    mensagem = "Digite o seu CPF: "
    mensagem_erro = "CPF inválido. Deve conter apenas números e ter no mínimo 11 dígitos."
    return obter_entrada(mensagem, validar_cpf, mensagem_erro)

def cadastro_rg():
    mensagem = "Digite o seu RG: "
    mensagem_erro = "RG inválido. Deve conter apenas números e ter no mínimo 7 dígitos."
    return obter_entrada(mensagem, validar_rg, mensagem_erro)

def listar_dicionario(lista):
  for dicionario in lista:
    print(f"-=-Dicionario-=-")
    for chave, valor in dicionario.items():
      print(f"{chave}:{valor}")
      print("-=-=-=-=-=-=-=-=-=-=-=")
  return