celula=['00000000', '00000000','00000000','00000000','00000000','00000000','00000000','00000000','00000000','00000000','00000000','00000000','00000000','00000000','00000000','00000000']

while True:
  print('\033[0;35m-=\033[m'*30)
  print("\033[1mOpções:\033[m")
  print("1 - Escrever na memória")
  print("2 - Ler da memória")
  print("3 - Olhar os conteúdos da memória")
  print("4 - Sair do programa")
  print('\033[0;35m-=\033[m'*30)

  escolha = int(input("\033[1mEscolha uma opção (1-4):\033[m "))

  print('\033[0;35m-=\033[m'*30)

  if escolha == 1:

    endereço = input("\033[1;32mDigite o endereço da célula(ex: 0101):\033[m")
    celula_endereço = endereço
    endereço = int(endereço)
    n = len(str(endereço))
    decimal = 0
    i = 0

    while n>=0:

      resto=endereço%10
      decimal = decimal + (resto*(2**i))
      n -= 1
      i += 1
      endereço = endereço // 10

    if len(celula_endereço) < 4 or len(celula_endereço)> 4:

      print('\033[0;35m-=\033[m'*30)
      print("\033[31mEndereço inválido!\033[m")
      print('\033[0;35m-=\033[m'*30)
      continue

    dado = input("\033[1;32mDigite o dado para armazenar(ex: 01010111):\033[m")

    if len(dado) < 8 or len(dado) > 8:

      print('\033[0;35m-=\033[m'*30)
      print("\033[31mDado inválido!\033[m")
      print('\033[0;35m-=\033[m'*30)
      continue

    print('\033[0;35m-=\033[m'*30)
    celula[decimal] = dado
    
  elif escolha == 2:

    endereço = input("\033[1;32mDigite o endereço da célula(ex: 0101):\033[m")
    celula_endereço = endereço
    endereço = int(endereço)
    n = len(str(endereço))
    decimal = 0
    i = 0

    while n>=0:
      resto=endereço%10
      decimal = decimal + (resto*(2**i))
      n -= 1
      i += 1
      endereço = endereço // 10

    if len(celula_endereço) < 4 or len(celula_endereço)> 4:

      print('\033[0;35m-=\033[m'*30)
      print("\033[31mEndereço inválido!\033[m")
      print('\033[0;35m-=\033[m'*30)
      continue

    print(f"\033[1;32mCélula {celula_endereço}:\033[m {celula[decimal]}")
    print('\033[0;35m-=\033[m'*30)

  elif escolha == 3:

    print(f'\033[1;32mCélulas:\033[m{celula}')
    print('\033[0;35m-=\033[m'*30)

  elif escolha == 4:

    break

print("\033[1;32mPrograma finalizado!\033[m")
