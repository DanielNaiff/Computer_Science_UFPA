import flet as ft

def main(page: ft.page):

  def tecla(e: ft.KeyboardEvent):
    page.add(
      ft.Text(f"Tecla pressionada: {e.key}, Shift: {e.shift}, Alt: {e.alt}, Meta: {e.meta}")
    )
  page.on_keyboard_event = tecla
  page.add(
    ft.Text("Pressione qualquer tecla ou uma combinação de teclas(CTRL, SHIFT, ALT, META)...")
  )

ft.app(target = main)