def validar_cpf(cpf):
    if not cpf.isdigit() or len(cpf) < 11:
        raise Exception("CPF inválido. Digite novamente.")

def validar_rg(rg):
    if not rg.isdigit() or len(rg) < 7:
        raise Exception("RG inválido. Digite novamente.")

def obter_entrada(mensagem, validacao):
    while True:
        entrada = input(mensagem)
        try:
            validacao(entrada)
            return entrada
        except Exception as e:
            print(e)

def cadastro_nome():
    return obter_entrada("Digite o seu nome:", lambda x: not x.isdigit())

def cadastro_nascimento():
    return obter_entrada("Digite o seu nascimento (xxxx):", lambda x: x.isdigit() and int(x) >= 1903)

def cadastro_sexo():
    return obter_entrada("Digite o seu sexo (M/F):", lambda x: x.upper() in ["M", "F"])

def cadastro_cpf():
    return obter_entrada("Digite o seu CPF:", validar_cpf)

def cadastro_rg():
    return obter_entrada("Digite o seu RG:", validar_rg)

def listar_dicionario(lista):
    for dicionario in lista:
        print("-=- Dicionário -=-")
        for chave, valor in dicionario.items():
            print(f"{chave}: {valor}")
        print("-=-=-=-=-=-=-=-=-")