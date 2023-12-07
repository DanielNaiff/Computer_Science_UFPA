import flet as ft

def main(page: ft.Page):
  page.title= "Aplicaão teste"  

  page.theme_mode = ft.ThemeMode.LIGHT
  page.update()

ft.app(target=main) 