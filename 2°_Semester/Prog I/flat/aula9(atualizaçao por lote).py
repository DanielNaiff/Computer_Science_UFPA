from flet import *

def main(page: Page):
  lv = ListView(expand=1, spacing=10, item_extent=50)
  page.add(lv)

  for i in range(1000):
    lv.controls.append(Text(f"Linha {i}"))

    # if i % 1000 == 0:
    #     page.update()
    
  page.update()

  app(target=main, view=WEB_BROWSER)