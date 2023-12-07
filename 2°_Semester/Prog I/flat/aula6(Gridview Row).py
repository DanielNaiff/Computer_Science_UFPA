import flet as ft
import os

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page: ft.Page):
  page.title = "Aula 6 - GridView with Row"
  linha = ft.Row(wrap=True, scroll="always", expand=True)
  page.add(linha)

  for i in range(1000):
    linha.controls.append(
      ft.Container(ft.Text(f"Item numero {i}", color="pink600"), 
                   width=100, 
                   height=100, 
                   alignment=ft.alignment.center,
                   bgcolor=ft.colors.AMBER_100,
                   border=ft.border.all(2, ft.colors.AMBER_600),
                   border_radius=ft.border_radius.all(8)
                   )
    )
  page.update()

ft.app(target=main, view=ft.WEB_BROWSER)