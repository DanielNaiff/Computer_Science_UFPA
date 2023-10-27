def cadastro_nome():
  while True:
    try:
      nome = input("Digite o seu nome:")

      if nome.isdigit():
        raise Exception("Nome inválido. Tente novamente")
      
    except Exception as e:
      print(e)

    else:
      return nome
      

def cadastro_nascimento():
  while True:
    try:
      nascimento = input("Digite o seu nascimento(xxxx):")

      if not nascimento.isdigit():
        raise Exception("Ano inválido. Tente novamente")
      elif int(nascimento) < 1903:
        raise Exception("Digite apenas número. Tente novamente")
      
    except Exception as e:
      print(e)

    else:
      return nascimento

def cadastro_sexo():
  while True:
    try:
      sexo = input("Digite o seu sexo(M/F):")

      if sexo not in ["F", "M", 'f', 'm']:
        raise Exception("Digite um sexo válido")
      
    except Exception as e:
      print(e)

    else:
      return sexo.upper()

def cadastro_cpf():
  while True:
    try:
      cpf = input("Digite o seu cpf:")

      if not cpf.isdigit():
        raise Exception("Digite um cpf válido. Digite novamente")

      elif len(cpf) < 11:
        raise Exception("CPF muito curto. Digite novamente")
      
    except Exception as e:
      print(e)

    else:
      return cpf

def cadastro_rg():
  while True:
    try:
      rg = input("Digite o seu Rg:")

      if not rg.isdigit():
        raise Exception("Digite um Rg válido. Digite novamente")

      elif len(rg) < 7:
        raise Exception("Rg muito curto. Digite novamente")
      
    except Exception as e:
      print(e)

    else:
      return rg

def listar_dicionario(lista):
  for dicionario in lista:
    print(f"-=-Dicionario-=-")
    for chave, valor in dicionario.items():
      print(f"{chave}:{valor}")
      print("-=-=-=-=-=-=-=-=-=-=-=")
  return