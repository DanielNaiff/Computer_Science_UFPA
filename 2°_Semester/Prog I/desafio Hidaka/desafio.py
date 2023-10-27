import desafio_funcoes as f

lista_dicionarios = []

for _ in range(5): 
    dic = {
        "nome": f.cadastro_nome(),
        "nascimento": f.cadastro_nascimento(),
        "sexo": f.cadastro_sexo(),
        "CPF": f.cadastro_cpf(),
        "Rg": f.cadastro_rg()
    }
    lista_dicionarios.append(dic)

try:
    listar_dicionario(lista_dicionarios)
    if not lista_dicionarios:
        raise Exception("O sistema ainda não possui nenhum dado cadastrado")
except Exception as e:
    print(e)
