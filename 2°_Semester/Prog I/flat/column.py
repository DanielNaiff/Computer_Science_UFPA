import flet as ft

def main(page: ft.Page):
  page.title = "Aula 1"
  page.vertical_alignment = ft.MainAxisAlignment.CENTER

  ola = ft.Text(value = "Olá, mundo!", size = 30)# variavel
  # page.controls.append(ola)# adicionou no controle da pagina a variavel ola
  # page.update()

  page.add(
        ft.Column(
                        [
                            ft.Container( content=ft.Text("Cadastro", size=20)),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Text('werwerewrewr'),
                            ft.Row(
                                [
                                    ft.Container(
                                            content= ft.ElevatedButton(
                                                        text="Cadastrar", 
                                                        icon="save", 
  
                                                    )#ElevatedButton   
                                    ),#Container                                    
                                ],
                                alignment=ft.MainAxisAlignment.END
                            ),#Row
                        ],
                        scroll=ft.ScrollMode.ALWAYS,
            expand=True,
                    ),
    )

ft.app(target=main)