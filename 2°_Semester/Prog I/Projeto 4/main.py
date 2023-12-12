from flet import *
import time
from math import pi
import tkinter as tk
from tkinter import filedialog
import os
from tkinter import messagebox
import re
import string

eXTENSIONS_ALLOWED = ['.txt', '.csv', '.json', '.xml', '.xls', '.xlsx', '.py', '.java', '.js', '.ini', '.cfg', '.conf', '.pdf', '.docx', '.md', '.rst', '.html', '.htm', '.css', '.log']

selected_files = Text(size=14, color="#7df6dd", weight="bold")
global absolute_path, extracted_data
extracted_data = {}
absolute_path = ''
components = {
    'tabela': Ref[DataTable](),
    'tabela_qtd': Ref[DataTable](),

}


table = DataTable(
                    columns=[
                        DataColumn(Text("Nome", color = "#7df6dd", weight= "bold")),
                        DataColumn(Text("Emails", color = "#7df6dd", weight= "bold")),
                        DataColumn(Text("CPFs", color = "#7df6dd", weight= "bold")),
                        DataColumn(Text("Telefones", color = "#7df6dd", weight= "bold")),
                        DataColumn(Text("Referencia", color = "#7df6dd", weight= "bold")),
                        # ft.DataColumn(ft.Text("Upload de Foto")),
                    ],width=float('inf'),ref=components['tabela']
                ),

table_qtd = DataTable(
                    columns=[
                        DataColumn(Text("Nome", color = "#e9665a", weight= "bold")),
                        DataColumn(Text("Emails", color = "#e9665a", weight= "bold")),
                        DataColumn(Text("CPFs", color = "#e9665a", weight= "bold")),
                        DataColumn(Text("Telefones", color = "#e9665a", weight= "bold")),
                        DataColumn(Text("Referencia", color = "#e9665a", weight= "bold")),
                        # ft.DataColumn(ft.Text("Upload de Foto")),
                    ],width=float('inf'),ref=components['tabela_qtd']
                ),



def main(page: Page):

    def file_picker(e):
        root = tk.Tk()

        file_types = [
            ("Text Files", "*.txt"),
            ("CSV Files", "*.csv"),
            ("JSON Files", "*.json"),
            ("XML Files", "*.xml"),
            ("Excel Files", "*.xls;*.xlsx"),
            ("Python Files", "*.py"),
            ("Java Files", "*.java"),
            ("JavaScript Files", "*.js"),
            ("INI Files", "*.ini"),
            ("Configuration Files", "*.cfg;*.conf"),
            ("PDF Files", "*.pdf"),
            ("Word Files", "*.docx"),
            ("Markdown Files", "*.md"),
            ("RST Files", "*.rst"),
            ("HTML Files", "*.html;*.htm"),
            ("CSS Files", "*.css"),
            ("Log Files", "*.log"),
            ("All Files", "*.*")
        ]

        file_path = filedialog.askopenfilename(
            title="Escolher arquivo",
            filetypes=file_types
        )

        if file_path:
            file_extension = os.path.splitext(file_path)[1]
            if file_extension not in eXTENSIONS_ALLOWED:
                messagebox.showerror("Erro", "Tipo de arquivo não permitido!")
            else:
                # Aqui você pode fazer algo com o file_path, como exibir, processar ou armazenar
                selected_files.value = os.path.basename(file_path)
                selected_files.update()
                animate_c1(e)
                global absolute_path

                absolute_path = os.path.abspath(file_path)
                print(absolute_path)
        else:
          selected_files.value = "Nenhum arquivo selecionado"
          selected_files.update()
        root.attributes('-topmost', True) 
        root.destroy()  # Fecha a janela após a seleção do arquivo

    # Restante do seu código...

    def reset_voltar(e):
        components["tabela"].current.rows = []
        vamosComecar.offset = transform.Offset(0, 0)
        regex.offset = transform.Offset(-6, 0)
        referencia.offset = transform.Offset(6, 0)
        nome.offset = transform.Offset(-10, 0)
        email.offset = transform.Offset(-10, 0)
        fone.offset = transform.Offset(-12, 0)
        cpf.offset = transform.Offset(-14, 0)
        lista.offset = transform.Offset(10, 0)
        extrair.offset = transform.Offset(0, 10)
        card_inicio[0].offset = transform.Offset(0, 0)
        card_tabela[0].offset = transform.Offset(0, 1)
        selected_files.value = ''

        # Atualiza os elementos para aplicar as mudanças
        vamosComecar.update()
        regex.update()
        referencia.update()
        nome.update()
        email.update()
        fone.update()
        cpf.update()
        lista.update()
        extrair.update()
        selected_files.update()
        card_inicio[0].update()
        card_tabela[0].update()

    def reset_offsets(e):
        print(absolute_path)
        global extracted_data

        extracted_data = {}  # Dicionário para armazenar os itens extraídos
        extracted_data_qtd = {}

        if os.path.exists(absolute_path):
            with open(absolute_path, 'r') as file:
                content = file.read()

                if nome.content.value:                
                    regex_nome = r'\b[A-Z][a-z]{1,}(?![a-z])\b'
                    matches_nome = re.findall(regex_nome, content)
                    print("Padrão de nome encontrado:", matches_nome)
                    extracted_data['Nomes'] = matches_nome
                    extracted_data_qtd['Nomes'] = len(matches_nome)
                    nome.content.value = False
                else:
                    extracted_data['Nomes'] = []
                    extracted_data_qtd['Nomes'] = []

                if email.content.value:
                    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
                    matches_email = re.findall(regex_email, content)
                    print("Padrão de email encontrado:", matches_email)
                    extracted_data['Emails'] = matches_email
                    extracted_data_qtd['Emails'] = len(matches_email)
                    email.content.value = False

                else:
                    extracted_data['Emails'] = []
                    extracted_data_qtd['Emails'] = []

                if cpf.content.value:
                    regex_cpf = r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b'
                    matches_cpf = re.findall(regex_cpf, content)
                    print("Padrão de CPF encontrado:", matches_cpf)
                    extracted_data['CPFs'] = matches_cpf
                    extracted_data_qtd['CPFs'] = len(matches_cpf)
                    cpf.content.value = False

                else:
                    extracted_data['CPFs'] = []
                    extracted_data_qtd['CPFs'] = []

                if fone.content.value:
                    regex_fone = r'\(\d{2}\)\s?\d{4,5}-\d{4}'
                    matches_fone = re.findall(regex_fone, content)
                    print("Padrão de telefone encontrado:", matches_fone)
                    extracted_data['Telefones'] = matches_fone
                    extracted_data_qtd['Telefones'] = len(matches_fone)
                    fone.content.value = False

                else:
                    extracted_data['Telefones'] = []
                    extracted_data_qtd['Telefones'] = []

                if lista.content.value != '':
                    termos = lista.content.value.split()
                    lista_palavras = re.findall(r'\w+', content)

                    all_ocorrencias = []  # Lista para armazenar todas as ocorrências

                    for termo in termos:
                        termo_sem_pontuacao = termo.strip(string.punctuation)
                        ocorrencias = [palavra for palavra in lista_palavras if palavra.strip(string.punctuation) == termo_sem_pontuacao]
                        all_ocorrencias.extend(ocorrencias)  # Adicionando as ocorrências à lista geral

                    print(f"Todas as ocorrências: {all_ocorrencias}")
                    extracted_data['Referencias'] = all_ocorrencias
                    extracted_data_qtd['Referencias'] = [len(all_ocorrencias)]

                    lista.content.value = ''

                else:
                    extracted_data['Referencias'] = []
                    extracted_data_qtd['Referencias'] = []
        max_length = max(len(value) for value in extracted_data.values())

        for key in extracted_data.keys():
            if len(extracted_data[key]) < max_length:
                extracted_data[key].extend([''] * (max_length - len(extracted_data[key])))
        data_table(extracted_data)
        data_table_qtd(extracted_data_qtd)



        # Redefine os offsets para as posições originais
        vamosComecar.offset = transform.Offset(0, 0)
        regex.offset = transform.Offset(-6, 0)
        referencia.offset = transform.Offset(6, 0)
        nome.offset = transform.Offset(-10, 0)
        email.offset = transform.Offset(-10, 0)
        fone.offset = transform.Offset(-12, 0)
        cpf.offset = transform.Offset(-14, 0)
        lista.offset = transform.Offset(10, 0)
        extrair.offset = transform.Offset(0, 10)
        card_inicio[0].offset = transform.Offset(0, -6)
        card_tabela[0].offset = transform.Offset(0, -1)
        selected_files.value = ''

        # Atualiza os elementos para aplicar as mudanças
        vamosComecar.update()
        regex.update()
        referencia.update()
        nome.update()
        email.update()
        fone.update()
        cpf.update()
        lista.update()
        extrair.update()
        selected_files.update()
        card_inicio[0].update()
        card_tabela[0].update()


        salvar_para_csv(extracted_data)
        page.snack_bar = SnackBar(
        Text("Os Dados foram extraidos para o CSV!", size=20),
        duration=1000,
        bgcolor="#7df6dd")

        page.snack_bar.open = True

        

    def salvar_para_csv(extracted_data):
        print(extracted_data)
        with open('resultados_extraidos.csv', mode='w', newline='', encoding='utf-8') as file:
            # Escreve cabeçalhos
            file.write(','.join(['Nomes', 'Emails', 'CPFs', 'Telefones', 'Referencias']) + '\n')

            if not extracted_data:
                return

            max_length = max(len(value) for value in extracted_data.values())

            for i in range(max_length):
                row = [
                    extracted_data.get('Nomes', [])[i] if i < len(extracted_data.get('Nomes', [])) else '',
                    extracted_data.get('Emails', [])[i] if i < len(extracted_data.get('Emails', [])) else '',
                    extracted_data.get('CPFs', [])[i] if i < len(extracted_data.get('CPFs', [])) else '',
                    extracted_data.get('Telefones', [])[i] if i < len(extracted_data.get('Telefones', [])) else '',
                    extracted_data.get('Referencias', [])[i] if i < len(extracted_data.get('Referencias', [])) else ''
                ]
                file.write(','.join(row) + '\n')

    def data_line_qtd(cadastro):
        return[
            DataCell(Text(cadastro["Nomes"], weight= "bold")),
            DataCell(Text(cadastro["Emails"], weight= "bold")),
            DataCell(Text(cadastro["CPFs"], weight= "bold")),
            DataCell(Text(cadastro["Telefones"], weight= "bold")),
            DataCell(Text(cadastro["Referencias"], weight= "bold")),
        ]

    def data_table_qtd(cadastro):
        data_rows_qtd = [DataRow(cells=data_line_qtd(cadastro))]
          # Adicionar este print para verificar as linhas de dados geradas
        components["tabela_qtd"].current.rows = data_rows_qtd
        return data_rows_qtd

    def data_line(cadastro,i):
        return[
            DataCell(Text(cadastro["Nomes"][i], weight= "bold")),
            DataCell(Text(cadastro["Emails"][i], weight= "bold")),
            DataCell(Text(cadastro["CPFs"][i], weight= "bold")),
            DataCell(Text(cadastro["Telefones"][i], weight= "bold")),
            DataCell(Text(cadastro["Referencias"][i], weight= "bold")),
        ]

    def data_table(cadastro):
        data_rows = [DataRow(cells=data_line(cadastro, i)) for i in range(len(cadastro["Nomes"]))]
          # Adicionar este print para verificar as linhas de dados geradas
        components["tabela"].current.rows = data_rows
        return data_rows

    def animate_c1(e):
        # Animação para fazer o c2 aparecer da esquerda para a direita
        regex.offset = transform.Offset(0, 0)
        regex.update()
        # Animação para fazer o c3 aparecer da direita para a esquerda
        referencia.offset = transform.Offset(0, 0)
        referencia.update()
        escolher.offset = transform.Offset(-6, 0)
        escolher.update()

        return True

    def animate_regex(e):
        # Animação para fazer o c1 desaparecer para a direita
        nome.offset = transform.Offset(0, 0)
        nome.update()
        # Animação para fazer o c2 aparecer da esquerda para a direita
        email.offset = transform.Offset(0, 0)
        email.update()
        # Animação para fazer o c3 aparecer da direita para a esquerda
        fone.offset = transform.Offset(0, 0)
        fone.update()
        cpf.offset = transform.Offset(0, 0)
        cpf.update()
        extrair.offset = transform.Offset(0, 0)
        extrair.update()

    def animate_referencia(e):
        # Animação para fazer o c1 desaparecer para a direita
        lista.offset = transform.Offset(0, 0)
        lista.update()
        extrair.offset = transform.Offset(0, 0)
        extrair.update()

    def animate_escolher(e):
        escolher.offset = transform.Offset(0, 0)
        escolher.update()
        # Animação para fazer o c1 desaparecer para a direita
        vamosComecar.offset = transform.Offset(6, 0)
        vamosComecar.update()

    vamosComecar = Container(
            offset=transform.Offset(0, 0),
            animate_offset=animation.Animation(1000),
            content=ElevatedButton(
                                content=Text("Vamos começar!", size = 15, weight='bold'),
                                style=ButtonStyle(
                                    shape=RoundedRectangleBorder(radius=10),
                                    color= 'white',
                                    bgcolor= "#7df6dd",
                                ),
                                on_click=animate_escolher
                            ),
        )
    escolher = Container(
            offset=transform.Offset(-6, 0),
            animate_offset=animation.Animation(1000),
            content=ElevatedButton(
                            content=Text("Escolher arquivo", size = 15, weight='bold'),
                            style=ButtonStyle(
                                shape=RoundedRectangleBorder(radius=10),
                                color= 'white',
                                bgcolor= "#7df6dd",
                            ),
                            on_click=file_picker
                        ),
        )
    regex = Container(
            offset=transform.Offset(-6, 0),
            animate_offset=animation.Animation(1000),
            content=ElevatedButton(
                                content=Text("Regex", size = 15, weight='bold'),
                                style=ButtonStyle(
                                    shape=RoundedRectangleBorder(radius=10),
                                    color= 'white',
                                    bgcolor= "#7df6dd",
                                ),
                                on_click=animate_regex
                            ),
        )
    referencia = Container(
            offset=transform.Offset(6, 0),
            animate_offset=animation.Animation(1000),
            content=ElevatedButton(
                                content=Text("Referencia", size = 15, weight='bold'),
                                style=ButtonStyle(
                                    shape=RoundedRectangleBorder(radius=10),
                                    color= 'white',
                                    bgcolor= "#7df6dd",
                                ),
                                on_click=animate_referencia
                            ),
        )
    extrair = Container(
        offset=transform.Offset(0, 10),
        animate_offset=animation.Animation(1000),
        content=ElevatedButton(
                            content=Text("Extrair", size = 15, weight='bold'),
                            style=ButtonStyle(
                                shape=RoundedRectangleBorder(radius=10),
                                color= 'white',
                                bgcolor= "#e9665a",
                            ),
                            on_click=reset_offsets
                        ),
    )
    voltar = Container(
        offset=transform.Offset(0, 10),
        animate_offset=animation.Animation(1000),
        content=ElevatedButton(text="Voltar", icon="save", on_click=None)
    )
    nome = Container(
        offset=transform.Offset(-10, 0),
        animate_offset=animation.Animation(1000),
        content=Checkbox(label="Nome", on_change=None, value= False)
    )
    email = Container(
        offset=transform.Offset(-10, 0),
        animate_offset=animation.Animation(1000),
        content=Checkbox(label="Email", on_change=None, value= False)
    )
    fone = Container(
        offset=transform.Offset(-12, 0),
        animate_offset=animation.Animation(1000),
        content=Checkbox(label="Fone", on_change=None, value= False)
    )
    cpf = Container(
        offset=transform.Offset(-14, 0),
        animate_offset=animation.Animation(1000),
        content=Checkbox(label="CPF", on_change=None, value= False,)
    )
    lista = Container(
        offset=transform.Offset(10, 0),
        animate_offset=animation.Animation(2000),
        content=TextField(label="Referências",color="#7df6dd")
    )

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

    card_inicio = Card(
                width=400,
                height=600,
                elevation=30,
                offset=transform.Offset(0, 0),
                animate_offset=animation.Animation(3000),
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
                                spacing=0,
                                controls=[
                                    Text("Bem-vindo ao Extrator de Dados!", size=20, weight="bold"),
                                    Text("Instruções:", size=20, weight="bold"),
                                    Text('''
    -Escolha a pasta onde estão os arquivos que deseja analisar.
    -Selecione os tipos de dados que deseja extrair.
    -Escolha entre expressão regular ou lista de referência para a extração.
    -Após a extração, você poderá salvar os dados extraídos em um arquivo CSV.
    ''', size=12, weight="bold"),
                                    Column(
                                        alignment=MainAxisAlignment.CENTER,
                                        horizontal_alignment=CrossAxisAlignment.CENTER,
                                        controls=[vamosComecar,
                                                  escolher,
                                                selected_files,
                                                  Row([regex, referencia],alignment=MainAxisAlignment.CENTER),
                                                                        Row([nome, email, fone, cpf],alignment=MainAxisAlignment.CENTER),
                                                                        Row([lista],alignment=MainAxisAlignment.CENTER),
                                                                        extrair,
                                                                        voltar,
                                        ],
                                    ),
                                ]
                            ),
                        ],
                    )
                )
            ),

    card_tabela = Card(
                width=800,
                height=500,
                elevation=30,
                offset=transform.Offset(0, 1),
                animate_offset=animation.Animation(1000),
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
                                    table[0],
                                    table_qtd[0],
                                Container(
                                        content=ElevatedButton(
                                        content=Text("Voltar", size = 15, weight='bold'),
                                        style=ButtonStyle(
                                            shape=RoundedRectangleBorder(radius=10),
                                            color= 'white',
                                            bgcolor= "#e9665a",
                                        ),
                                        on_click=reset_voltar
                                    ),
                                    )
                                ]
                            ),
                        ],scroll=ScrollMode.ALWAYS,
                        expand=True,
                    )
                )
            ),


    page.title = "Sistema de extração de conteúdo"           
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.bgcolor = '#1f262f'

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

    page.add(
        card_inicio[0],
        card_tabela[0]
    )
    animate_boxes(),
    page.update(),

app(target=main)
