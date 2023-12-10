from flet import *
import control as c
import time
from math import pi

class AnimatedBox(UserControl):
    def __init__(self, border_color, bg_color, rotate_angle):
        self.border_color = border_color
        self.bg_color = bg_color
        self.rotate_angle = rotate_angle
        super().__init__()
    def build(self):
        return Container(
            width = 48,
            height = 48,
            border=border.all(2.5, self.border_color),
            bgcolor=self.bg_color,
            border_radius=2,
            rotate=transform.Rotate(self.rotate_angle, alignment.center),
            animate_rotation=animation.Animation(700, "easeInOut"),
        )
    

def main(page: Page):        
    c.init(page)
    page.title = "Sistema "           
    page.on_route_change = route_change  
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.bgcolor = '#1f262f'

    def init(p):
        global page, telas, cadastros        
        page = p
        cadastros = []    
        telas = {
            '0': main.viewTela1()
        }

    def route_change(route):
        page.views.clear()    
        page.views.append(
            telas[page.route]
        )          
        page.update()
    def animate_boxes():
        clock_wise_rotate = pi/4
        counter_clock_wise_rotate = -pi * 2
        red_box = page.controls[0].content.content.controls[1].controls[0].controls[0]
        blue_box = page.controls[0].content.content.controls[1].controls[1].controls[0]
        counter = 0
        while True:
            if counter >= 0 and counter <= 4:
                red_box.rotate = transform.Rotate(
                    counter_clock_wise_rotate, alignment.center
                )
                blue_box.rotate = transform.Rotate(
                    clock_wise_rotate, alignment.center
                )
                red_box.update()
                blue_box.update()

                clock_wise_rotate += pi/2
                counter_clock_wise_rotate -= pi/2
                counter += 1
                time.sleep(0.7)

            if counter >= 5 and counter <= 10:
                clock_wise_rotate -= pi/2
                counter_clock_wise_rotate += pi/2    
                red_box.rotate = transform.Rotate(
                    counter_clock_wise_rotate, alignment.center
                )
                blue_box.rotate = transform.Rotate(
                    clock_wise_rotate, alignment.center
                )
                red_box.update()
                blue_box.update()
                counter += 1
                time.sleep(0.7)

            if counter > 10:
                counter = 0
    def navigate_to_escolherArquivo(e):
        page.go('0')
    page.add(
        Card(
            width=400,
            height=600,
            elevation=30,
            content=Container(
                bgcolor='#23262a',
                border_radius=6,
                content=Column(
                    horizontal_alignment = CrossAxisAlignment.CENTER,
                    controls=[
                        Divider(height=10, color='transparent'),
                        Stack(
                            controls=[
                                AnimatedBox("#e9665a", None, 0),
                                AnimatedBox("#7df6dd", "#23262a", pi/4),
                            ],
                        ),
                        Divider(height=10, color='transparent'),
                        Column(
                            alignment=MainAxisAlignment.CENTER,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=5,
                            controls=[
                                Text("Bem-vindo", size=22, weight="bold"),
                                
                            Container(
                                content=ElevatedButton(
                                    content=Text("Vamos começar!", size = 15, weight='bold'),
                                    style=ButtonStyle(
                                        shape=RoundedRectangleBorder(radius=10),
                                        color= 'white',
                                        bgcolor= "#7df6dd",
                                    ),
                                    on_click=navigate_to_escolherArquivo
                                ),
                            ),
                            ]
                        ),
                    ],
                )
            )
        ),
    )
    animate_boxes(),
    page.update(),


app(target=main)
