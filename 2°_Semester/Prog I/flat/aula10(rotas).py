from flet import *

def main(page: Page):
  page.add(Text(f"Rota inicial: {page.route}"))

  def nova_rota(route):
    page.add(Text("Nova rota: {route}"))

  def rota_compras():
    page.route = "/"

  page.on_route_change = nova_rota
  page.update

app(target=main, view=WEB_BROWSER)