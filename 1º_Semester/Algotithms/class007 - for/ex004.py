cachorro_quente = 0
bauru_simples = 0
bauru_ovo = 0
hamburguer = 0
cheeseburguer = 0
refrigerante = 0
while True:
  pedido = input('Digite o seu pedido(100,101,102,103,104,105):')
  if pedido == '100':
    cachorro_quente += 1
  elif pedido == '101':
    bauru_simples += 1
  elif pedido == '102':
    bauru_ovo += 1
  elif pedido == '103':
    hamburguer = 0
  elif pedido == '104':
    cheeseburguer += 1
  elif pedido == '105':
    refrigerante += 1
  elif pedido == '000':
    break
print(f'Total a pagar: {cachorro_quente*1.2 + bauru_simples*1.3 + bauru_ovo*1.5 + hamburguer*1.2 + cheeseburguer*1.3 + refrigerante}')