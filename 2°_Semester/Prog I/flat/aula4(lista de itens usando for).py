import flet as ft

def main(page: ft.Page):
  page.title = "Aula 4 - Lista de itens"
  for i in range(500):
    page.controls.append(ft.Text(f"Estamos na linha {i}"))

  page.scroll = "always"
  page.update()

ft.app(target=main, view=ft.WEB_BROWSER)