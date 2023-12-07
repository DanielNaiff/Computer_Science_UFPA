import flet as ft

def main(page: ft.Page):
  page.title = "Aula 2 - Textfield"

  def login(e):

    if not entrada_nome.value:
      entrada_nome.error_text = "Por favor preencha o seu nome."
      page.update()
    if not entrada_senha.value:
      entrada_senha.error_text = "Por favor digite a sua senha."
      page.update()
    else:

      nome = entrada_nome.value
      senha = entrada_senha.value
      print(f"Nome: {nome}\nSenha: {senha}")

      page.clean()
      page.add(ft.Text(f"Olá, {nome}\nSeja bem vindo a nossa aplicação"))
      pass

  entrada_nome = ft.TextField(label = "Digite o seu nome")
  entrada_senha = ft.TextField(label = "Digite a sua senha")

  page.add(
    entrada_nome,
    entrada_senha,
    ft.ElevatedButton("Clique em mim", on_click = login)
  )



ft.app(target=main)