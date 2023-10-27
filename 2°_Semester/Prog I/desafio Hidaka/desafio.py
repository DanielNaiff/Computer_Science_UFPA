import desafio_funcoes as f

dic = {
  "nome": "",
  "nascimento": "",
  "sexo": "",
  "CPF": "",
  "Rg": ""
}
lista_dicionarios = []

while True:
    print("1 para cadastrar os dados 2 para mostrar os dicionario ou aperte qualquer tecla para finalizar")
    opc = input("Digite uma opção:")

    if opc == "1":
        dic["nome"] = f.cadastro_nome()
        dic["nascimento"] = f.cadastro_nascimento()
        dic["sexo"] = f.cadastro_sexo()
        dic["CPF"] = f.cadastro_cpf()
        dic["Rg"] = f.cadastro_rg()
        lista_dicionarios.append(dic.copy())  

    elif opc == "2":
        try:
            f.listar_dicionario(lista_dicionarios)
            if not lista_dicionarios:
                raise Exception("O sistema ainda não possui nenhum dado cadastrado")
        except Exception as e:
            print(e)

    else:
        break
