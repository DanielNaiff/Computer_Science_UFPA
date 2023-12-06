import flet as ft

def main(page: ft.Page):
  page.title = "Aula 1"
  page.vertical_alignment = ft.MainAxisAlignment.CENTER

  ola = ft.Text(value = "Olá, mundo!", size = 30)# variavel
  # page.controls.append(ola)# adicionou no controle da pagina a variavel ola
  # page.update()

  page.add(
        ft.Row(
            [
              ola
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)