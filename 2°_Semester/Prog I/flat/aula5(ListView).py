import flet as ft

def main(page: ft.Page):
  page.title = "Aula 5 - ListView"
  lista = ft.ListView(spacing=2, expand=True)

  for i in range(100):
    lista.controls.append(ft.Text(f"Linha {i}"))
  
  page.add(
    lista
  )

ft.app(target=main, view=ft.WEB_BROWSER)